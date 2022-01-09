import streamlit as st
import pandas as pd

from data import TAXES_BY_PROVINCES, QUANTITY_NAME, IBI
from cost_calculator import get_buy_cost_breakdown
from investment_calculator import plot_investment, calculate_yearly_gains

st.title("Calculadora para inversiones en inmuebles")

# -------------- Buying parameters -------------- #

st.subheader("Parámetros de la compra")

f1col1, f1col2, f1col3 = st.columns([1, 1, 1])
initial_cost = f1col1.number_input(
    label='Precio bruto del inmueble:',
    min_value=0,
    max_value=100000000,
    value=100000,
    help="Precio del inmueble sin tener en cuenta los impuestos o mantenimiento asociado"
)

province = f1col2.selectbox(
    label="Comunidad autónoma:",
    options=TAXES_BY_PROVINCES.keys(),
)

new_option = f1col3.radio(
    label="Seleccione el tipo de inmueble:",
    options=("Nuevo", "Segunda mano")
)
is_new = new_option == "Nuevo"

if TAXES_BY_PROVINCES[province] != None:
    bc = get_buy_cost_breakdown(
        initial_cost,
        iaj=TAXES_BY_PROVINCES[province].iaj,
        itp=0 if is_new else TAXES_BY_PROVINCES[province].itp,
        iva=TAXES_BY_PROVINCES[province].iva if is_new else 0
    )

    breakdown_df = pd.DataFrame(bc.data)
    total_inverted = int(breakdown_df[QUANTITY_NAME].iat[-1])
    breakdown_df[QUANTITY_NAME] = breakdown_df[QUANTITY_NAME].apply(
        lambda x: f"€ {int(x)}")

    with st.expander("Desglose del precio de compra del inmueble", expanded=False):
        st.dataframe(breakdown_df)
    st.write(f"Precio total de compra: {total_inverted} €")

# -------------- Rent parameters -------------- #

st.subheader("Parámetros del alquiler")

f2col1, f2col2, f2col3 = st.columns([1, 1, 1])
rent_price = f2col1.number_input(
    label='Precio del alquiler mensual:',
    min_value=0,
    max_value=10000,
    value=500,
    help="Precio al que se alquilará el inmueble"
)

months_until_first_rent = f2col2.number_input(
    label='Meses hasta alquilar',
    min_value=0,
    max_value=100,
    value=1,
    help="Número de meses hasta que se alquile el inmueble"
)

rent_percentage = f2col3.slider(
    label="Porcentaje de tiempo alquilado",
    min_value=0,
    max_value=100,
    value=90,
    step=1,
)

# --------------- Other parameters --------------- #

st.subheader("Otros parámetros")

f3col1, f3col2, f3col3 = st.columns([1, 1, 1])

insurance = f3col1.number_input(
    label='Coste anual del seguro:',
    min_value=0,
    max_value=10000,
    value=100,
)

reform = f3col2.number_input(
    label='Coste de la reforma:',
    min_value=0,
    max_value=100000,
    value=1000,
)

other_monthly_expenses = f3col3.number_input(
    label='Gastos mensuales:',
    min_value=0,
    max_value=10000,
    value=200,
    help="Costes por mantenimiento (luz, agua, gas...)"
)

monthly_gains = rent_price - other_monthly_expenses

if TAXES_BY_PROVINCES[province] != None:
    st.subheader("Recuperación de la inversión")
    yearly_gains = calculate_yearly_gains(
        monthly_gains=monthly_gains,
        rent_percentage=rent_percentage,
        insurance=insurance,
        ibi=IBI
    )
    st.write(
        f"Tardarás {int(total_inverted/yearly_gains)} años en recuperar la inversión")
    st.plotly_chart(plot_investment(total_inverted, yearly_gains))

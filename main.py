import streamlit as st
import pandas as pd

from data import TAXES_BY_PROVINCES, QUANTITY_NAME
from cost_calculator import get_cost_breakdown


st.title("Calculadora para inversiones en inmuebles")

col1, col2, col3 = st.columns([1, 1, 1])
initial_cost = col1.number_input(
    label='Precio bruto del inmueble:',
    min_value=1000,
    max_value=100000000,
    value=100000,
    help="Precio del inmueble sin tener en cuenta los impuestos o mantenimiento asociado"
)

province = col2.selectbox(
    label="Comunidad autónoma:",
    options=TAXES_BY_PROVINCES.keys(),
)

new_option = col3.radio(
    label="Seleccione el tipo de inmueble:",
    options=("Nuevo", "Segunda mano")
)
is_new = new_option == "Nuevo"

if TAXES_BY_PROVINCES[province] != None:
    bc = get_cost_breakdown(
        initial_cost,
        iaj=TAXES_BY_PROVINCES[province].iaj,
        itp=0 if is_new else TAXES_BY_PROVINCES[province].itp,
        iva=TAXES_BY_PROVINCES[province].iva if is_new else 0
    )

    breakdown_df = pd.DataFrame(bc.data)
    breakdown_df[QUANTITY_NAME] = breakdown_df[QUANTITY_NAME].apply(
        lambda x: f"€ {int(x)}")

    with st.expander("Desglose del precio de compra del inmueble", expanded=True):
        st.dataframe(breakdown_df)

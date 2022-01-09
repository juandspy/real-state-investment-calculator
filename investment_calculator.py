from datetime import date
import plotly.graph_objects as go


def calculate_yearly_gains(monthly_gains, rent_percentage, insurance, ibi):
    return rent_percentage/100*monthly_gains*12-insurance-ibi


def plot_investment(initial_investment, yearly_gains):

    years_to_retrieve_initial_investment = int(
        initial_investment/yearly_gains)

    this_year = date.today().year
    last_year = this_year + years_to_retrieve_initial_investment

    years = [year for year in range(this_year, last_year)]
    list_gains_by_year = []
    last_gain = 0
    for _ in years:
        last_gain += yearly_gains
        list_gains_by_year.append(last_gain)

    fig = go.Figure([go.Bar(x=years, y=list_gains_by_year)])
    fig.add_hline(y=initial_investment, line_width=1,
                  line_dash="dash", line_color="grey")

    return fig

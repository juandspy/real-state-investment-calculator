from data import TYPE_NAME, PERCENTAGE_NAME, QUANTITY_NAME


class BreakdownCosts:
    def __init__(self):
        self.data = {
            TYPE_NAME: [],
            PERCENTAGE_NAME: [],
            QUANTITY_NAME: []
        }

    def add_cost(self, _type, percentage, quantity):
        self.data[TYPE_NAME] += [_type]
        self.data[PERCENTAGE_NAME] += [percentage]
        self.data[QUANTITY_NAME] += [quantity]


def calculate_taxes(bc: BreakdownCosts(), initial_cost, iaj, itp, iva):
    """Returns a dictionary with the cost of each tax."""
    tax_names = [
        "Impuesto de Actos Jurídicos",
        "Impuesto de Transferencia del Patrimonio",
        "IVA"
    ]
    tax_values = [iaj, itp, iva]
    for i in range(len(tax_names)):
        bc.add_cost(
            _type=tax_names[i],
            percentage=f"{tax_values[i]*100:.1f}%",
            quantity=initial_cost * tax_values[i]
        )
    return bc


def calculate_maintenance(bc: BreakdownCosts()):
    """To be done."""
    return bc


def calculate_risks(bc: BreakdownCosts()):
    """To be done."""
    return bc


def calculate_total(bc: BreakdownCosts()):
    """Aggregates all the costs in the dictionary"""
    bc.add_cost(
        _type="Total",
        percentage="",
        quantity=sum(bc.data[QUANTITY_NAME])
    )
    return bc


def get_cost_breakdown(initial_cost, iaj, itp, iva):
    bc = BreakdownCosts()
    bc.add_cost("Coste inicial", "100%", initial_cost)

    bc = calculate_taxes(
        bc,
        initial_cost,
        iaj,
        itp,
        iva
    )

    bc = calculate_total(bc)

    return bc

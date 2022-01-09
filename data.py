
TYPE_NAME = "Tipo"
PERCENTAGE_NAME = "Porcentaje"
QUANTITY_NAME = "Cantidad"


class Taxes:
    def __init__(self, iaj, itp, iva):
        self.iaj = iaj/100
        self.itp = itp/100
        self.iva = iva/100


IVA = 10
IBI = 0.7  # Goes from 0.4 to 1.1 depending on the city

TAXES_BY_PROVINCES = {
    "Seleccione una provincia": None,
    "Andalucía":            Taxes(1.5, 8., IVA),
    "Aragón":               Taxes(1.5, 8., IVA),
    "Asturias":             Taxes(1.2, 8., IVA),
    "Baleares":             Taxes(1.2, 8., IVA),
    "Canarias":             Taxes(1.0, 6.5, 6.5),
    "Cantabria":            Taxes(1.5, 10., IVA),
    "Castilla-La Mancha":   Taxes(1.25, 9., IVA),
    "Castilla y León":      Taxes(1.5, 8., IVA),
    "Cataluña":             Taxes(1.5, 10., IVA),
    "Ceuta":                Taxes(0.5, 6., IVA),
    "Comunidad Valenciana": Taxes(1.5, 10., IVA),
    "Extremadura":          Taxes(1.5, 8., IVA),
    "Galicia":              Taxes(1.5, 10., IVA),
    "La Rioja":             Taxes(1.0, 7., IVA),
    "Comunidad de Madrid":  Taxes(0.75, 6., IVA),
    "Melilla":              Taxes(0.5, 6., IVA),
    "Murcia":               Taxes(1.5, 8., IVA),
    "Navarra":              Taxes(0.5, 6., IVA),
    "País Vasco":           Taxes(0.5, 7., IVA),
}

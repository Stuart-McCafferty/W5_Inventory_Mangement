class Product:
    def __init__(self, _name, _quantity, _cost, _selling_price, low_stock, supplier, meal, _id = None):
        self.name = _name
        self.quantity = _quantity
        self.cost = _cost
        self.selling_price = _selling_price
        self.low_stock = low_stock
        self.supplier = supplier
        self.meal = meal
        self.id = _id

        
class Product:
    def __init__(self, _name, _quantity, _cost, _selling_price, supplier, id = None):
        self.name = _name
        self.quantity = _quantity
        self.cost = _cost
        self.selling_price = _selling_price
        self.supplier = supplier
        self.id = _id
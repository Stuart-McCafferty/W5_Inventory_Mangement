from db.run_sql import run_sql
from models.product import Product
from models.supplier import Supplier

def save(product):
    sql = "INSERT INTO products(name, quantity, cost, selling_price, supplier_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [product.name, product.quantity, product.cost, product.selling_price, product.supplier.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product
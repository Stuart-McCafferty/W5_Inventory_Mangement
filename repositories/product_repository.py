from db.run_sql import run_sql
from models.product import Product
from models.supplier import Supplier
import supplier_repository


# works
def save(product):
    sql = "INSERT INTO products(name, quantity, cost, selling_price, supplier_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [product.name, product.quantity, product.cost, product.selling_price, product.supplier.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product


def select_all():
    products = []
    sql = "SELECT * FROM products"
    results =run_sql(sql)
    for row in results:
        supplier = supplier_repository.select(row[supplier.id])
        product = Product(row['name'], row['quantity'], row['cost'], row['selling_price'], supplier, row['id'])
        products.append(product)
    return products


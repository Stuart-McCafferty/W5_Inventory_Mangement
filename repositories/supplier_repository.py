from db.run_sql import run_sql
from models.product import Product
# from models.product import Product
from models.supplier import Supplier

# works
def save(supplier):
    sql = "INSERT INTO suppliers (name, link, phone) VALUES (%s, %s, %s) RETURNING *"
    values = [supplier.name, supplier.link, supplier.phone]
    results = run_sql(sql, values)
    id = results[0]['id']
    supplier.id = id
    return supplier

# works
def select_all():
    suppliers = []
    sql = "SELECT * FROM suppliers"
    results = run_sql(sql)

    for row in results:
        supplier = Supplier(row['name'], row['link'], row['phone'], row['id'])
        suppliers.append(supplier)
    return suppliers

# works
def delete_all():
    sql = "DELETE FROM suppliers"
    run_sql(sql)


# works
def select(id):
    supplier = None
    sql = "SELECT * FROM suppliers WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        supplier = Supplier(result['name'], result['link'], result['phone'], result['id'])
    return supplier


# works
def delete(id):
    sql = "DELETE  FROM suppliers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# works
def update(supplier):
    sql = "UPDATE suppliers SET (name, link, phone) = (%s, %s, %s) WHERE id = %s"
    values = [supplier.name, supplier.link, supplier.phone, supplier.id]
    run_sql(sql, values)

def products(supplier):
    products = []

    sql = "SELECT * FROM products WHERE supplier_id = %s"
    values = [supplier.id]
    results = run_sql(sql, values)

    for row in results:
        product = Product(row['name'], row['quantity'], row['cost'], row['selling_price'], supplier, row['id'])
        products.append(product)
    return products

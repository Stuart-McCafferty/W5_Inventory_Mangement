from db.run_sql import run_sql
from models.product import Product
from models.supplier import Supplier
import repositories.supplier_repository as supplier_repository


# works
def save(product):
    sql = "INSERT INTO products(name, quantity, cost, selling_price, supplier_id) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [product.name, product.quantity, product.cost, product.selling_price, product.supplier.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product


# works
def select_all():
    products = []
    sql = "SELECT * FROM products"
    results =run_sql(sql)
    for row in results:
        supplier = supplier_repository.select(row['supplier_id'])
        product = Product(row['name'], row['quantity'], row['cost'], row['selling_price'], supplier, row['id'])
        products.append(product)
    return products

# works
def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)
    
# works
def delete(id):
    sql = "DELETE  FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# works
def update(product):
    sql = "UPDATE products SET (name, quantity, cost, selling_price, supplier_id) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [product.name, product.quantity, product.cost, product.selling_price, product.supplier.id, product.id]
    run_sql(sql,values)


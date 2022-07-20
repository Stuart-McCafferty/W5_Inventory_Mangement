from db.run_sql import run_sql
from models.product import Product
from models.supplier import Supplier
from models.meal import Meal
import repositories.supplier_repository as supplier_repository
import repositories.meal_repository as meal_repository


# works
def save(product):
    sql = "INSERT INTO products(name, quantity, cost, selling_price, low_stock, supplier_id, meal_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [product.name, product.quantity, product.cost, product.selling_price, product.low_stock, product.supplier.id, product.meal.id]
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
        meal = meal_repository.select(row['meal_id'])
        product = Product(row['name'], row['quantity'], row['cost'], row['selling_price'], row['low_stock'], supplier, meal, row['id'])
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
    sql = "UPDATE products SET (name, quantity, cost, selling_price, low_stock, supplier_id, meal_id) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [product.name, product.quantity, product.cost, product.selling_price, product.low_stock, product.supplier.id, product.meal.id, product.id]
    run_sql(sql,values)

def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        supplier = supplier_repository.select(result['supplier_id'])
        meal = meal_repository.select(result['meal_id'])
        product = Product(result['name'], result['quantity'], result['cost'], result['selling_price'], result['low_stock'], supplier, meal, result['id'])
    return product


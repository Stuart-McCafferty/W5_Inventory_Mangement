from db.run_sql import run_sql
from models.product import Product
from models.meal import Meal
from models.supplier import Supplier
import repositories.supplier_repository as supplier_repository


def save(meal):
    sql = "INSERT INTO meals (name, in_stock) VALUES (%s, %s) RETURNING *"
    values = [meal.name, meal.in_stock]
    results = run_sql(sql, values)
    id = results[0]['id']
    meal.id = id
    return meal


def delete_all():
    sql = "DELETE FROM meals"
    run_sql(sql)

def select_all():
    meals = []
    sql = "SELECT * FROM meals"
    results = run_sql(sql)

    for row in results:
        meal = Meal(row['name'], row['in_stock'], row['id'])
        meals.append(meal)
    return meals

def select(id):
    meal = None
    sql = "SELECT * FROM meals WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        meal = Meal(result['name'], result['in_stock'], result['id'])
    return meal

def delete(id):
    sql = "DELETE  FROM meals WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(meal):
    sql = "UPDATE meals SET (name, in_stock) = (%s, %s) WHERE id = %s"
    values = [meal.name, meal.in_stock, meal.id]
    run_sql(sql, values)

def select_products_of_meal(id):
    products = []
    sql = "SELECT products.* FROM products INNER JOIN meals_products ON meals_products.product_id = products.id WHERE meals_products.meal_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        supplier = supplier_repository.select(result['supplier_id'])
        product = Product(result['name'], result['quantity'], result['cost'], result['selling_price'], result['low_stock'], supplier, result['id'])
        products.append(product)
    return products

    
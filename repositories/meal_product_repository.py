from db.run_sql import run_sql
from models.product import Product
from models.meal import Meal
from models.meal_product import Meal_Product
import repositories.meal_repository as meal_repository
import repositories.product_repository as product_repository

def save(meal_product):
    sql = "INSERT INTO meals_products (meal_id, product_id) VALUES (%s, %s) RETURNING *"
    values = [meal_product.meal_id.id, meal_product.product_id.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    meal_product.id = id
    return meal_product


def select_all():
    meals_products = []
    sql = "SELECT * FROM meals_products"
    results = run_sql(sql)
    for result in results:
        meal = meal_repository.select(result["meal_id"])
        product = product_repository.select(result["product_id"])
        meal_product = Meal_Product(meal, product, result["id"])
        meals_products.append(meal_product)
    return meals_products

def select(id):
    meal_product = None 
    sql = "SELECT * FROM meals_products WHERE id = %s"
    values = [id]

    results = run_sql(sql, values)

    if results:
        result = results[0]
        meal = meal_repository.select(result["meal_id"])
        product = product_repository.select(result["product_id"])
        meal_product = Meal_Product(meal, product, result["id"])
    return meal_product


def delete_all():
    sql = "DELETE FROM meals_products"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM meals_products WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(meal_product):
    sql = "UPDATE meals_products SET (meal_id, product_id) = (%s, %s) WHERE id = %s"
    values = [meal_product.meal_id, meal_product.product_id, meal_product.id]
    run_sql(sql, values)


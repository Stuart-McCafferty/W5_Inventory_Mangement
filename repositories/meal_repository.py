from db.run_sql import run_sql
from models.product import Product
from models.meal import Meal


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

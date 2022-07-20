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


def select_all():
    meals = []
    sql = "SELECT * FROM meals"
    results = run_sql(sql)

    for row in results:
        meal = Meal(row['name'], row['in_stock'])
        meals.append(meal)
    return meals

# works
def delete_all():
    sql = "DELETE FROM meals"
    run_sql(sql)


# works
def select(id):
    meal = None
    sql = "SELECT * FROM meals WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        meal = Meal(result['name'], result['in_stock'])
    return meal


# works
def delete(id):
    sql = "DELETE  FROM meals WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# works
def update(meal):
    sql = "UPDATE meals SET (name, in_stock) = (%s, %s) WHERE id = %s"
    values = [meal.name, meal.in_stock]
    run_sql(sql, values)
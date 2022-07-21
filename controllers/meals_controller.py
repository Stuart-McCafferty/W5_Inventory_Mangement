from flask import Flask, render_template, Blueprint, request, redirect
import repositories.product_repository as product_repository
import repositories.meal_repository as meal_repository
from models.product import Product
from models.supplier import Supplier


meals_blueprint = Blueprint("meals", __name__)
#INDEX
@meals_blueprint.route("/meals")
def meals():
    meals = meal_repository.select_all()
    return render_template("meals/index.html", all_meals=meals)

# SHOW
@meals_blueprint.route("/meals/<id>")
def show_meal(id):
    products = meal_repository.select_products_of_meal(id)
    meal = meal_repository.select(id)
    return render_template("meals/show.html", products=products, meal=meal)

# DELETE
@meals_blueprint.route("/meals/<id>/delete", methods=["POST"])
def delete_meal(id):
    meal_repository.delete(id)
    return redirect("/meals")

# # NEW
# @zombies_blueprint.route("/zombies/new")
# def new_zombie():
#     zombie_types = zombie_type_repository.select_all()
#     return render_template("zombies/new.html", zombie_types=zombie_types)


# # CREATE
# @zombies_blueprint.route("/zombies", methods=["POST"])
# def create_zombie():
#     name = request.form["name"]
#     zombie_type_id = request.form["zombie_type_id"]
#     zombie_type = zombie_type_repository.select(zombie_type_id)
#     new_zombie = Zombie(name, zombie_type)
#     zombie_repository.save(new_zombie)
#     return redirect("/zombies")


# # EDIT
# @zombies_blueprint.route("/zombies/<id>/edit")
# def edit_zombie(id):
#     zombie = zombie_repository.select(id)
#     zombie_types = zombie_type_repository.select_all()
#     return render_template('zombies/edit.html', zombie=zombie, zombie_types=zombie_types)


# # UPDATE
# @zombies_blueprint.route("/zombies/<id>", methods=["POST"])
# def update_zombie(id):
#     name = request.form["name"]
#     zombie_type_id = request.form["zombie_type_id"]
#     zombie_type = zombie_type_repository.select(zombie_type_id)
#     zombie = Zombie(name, zombie_type, id)
#     zombie_repository.update(zombie)
#     return redirect("/zombies")



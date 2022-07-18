from flask import Flask, render_template, Blueprint, request, redirect
from repositories import product_repository
from repositories import supplier_repository
from models.product import Product
from models.supplier import Supplier

products_blueprint = Blueprint("tasks", __name__)

@products_blueprint.route("/products")
def products():
    #GET the tasks from the DB
    products = product_repository.select_all()
    #Pass the tasks to the template
    return render_template("products/index.html", all_products = products)

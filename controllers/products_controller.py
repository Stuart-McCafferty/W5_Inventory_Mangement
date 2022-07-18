from flask import Flask, render_template, Blueprint, request, redirect
import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository
from models.product import Product
from models.supplier import Supplier


products_blueprint = Blueprint("products", __name__)


# INDEX GET'/tasks'
@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", all_products = products)

# NEW
# Get '/products/new'
@products_blueprint.route("/products/new", methods=['GET'])
def new_product():
    suppliers = supplier_repository.select_all()
    return render_template("products/new.html", all_suppliers = suppliers)


# CREATE 
# POST '/products'
@products_blueprint.route("/products",  methods=['POST'])
def create_product():
    name = request.form['name']
    quantity     = request.form['quantity']
    cost    = request.form['cost']
    selling_price   = request.form['selling_price']
    supplier_id = request.form['supplier_id']
    supplier        = supplier_repository.select(supplier_id)
    product        = Product(name, quantity, cost, selling_price, supplier)
    product_repository.save(product)
    return redirect('/products')

# SHOW
# GET '/products/<id>'
@products_blueprint.route("/products/<id>")
def show(id):
    product = product_repository.select(id)
    return render_template("products/show.html", product=product)


# EDIT
# GET '/products/<id>/edit'

# UPDATE 
# PUT '/tasks/<id>

# DELETE
# DELETE '/tasks/<id>
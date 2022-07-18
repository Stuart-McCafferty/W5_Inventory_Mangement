from flask import Flask, render_template, Blueprint, request, redirect
import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository
from models.product import Product
from models.supplier import Supplier


suppliers_blueprint = Blueprint("suppliers", __name__)


# INDEX GET'/tasks'
@suppliers_blueprint.route("/suppliers")
def suppliers():
    suppliers = supplier_repository.select_all()
    return render_template("suppliers/index.html", all_suppliers = suppliers)

# NEW
# Get '/products/new'
@suppliers_blueprint.route("/suppliers/new", methods=['GET'])
def new_product():
    suppliers = supplier_repository.select_all()
    return render_template("suppliers/new.html", all_suppliers = suppliers)


# CREATE 
# POST '/products'
@suppliers_blueprint.route("/suppliers",  methods=['POST'])
def create_supplier():
    name = request.form['name']
    link     = request.form['link']
    phone    = request.form['phone']
    supplier = Supplier(name, link, phone)
    supplier_repository.save(supplier)
    return redirect('/suppliers')

# SHOW
# GET '/products/<id>'


# EDIT
# GET '/products/<id>/edit'

# UPDATE 
# PUT '/tasks/<id>

# DELETE
# DELETE '/tasks/<id>
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
# GET '/suppliers/<id>'
@suppliers_blueprint.route("/suppliers/<id>", methods=['GET'])
def show_supplier(id):
    supplier = supplier_repository.select(id)
    return render_template('suppliers/show.html', supplier = supplier)

# EDIT
# GET '/suppliers/<id>/edit'
@suppliers_blueprint.route("/suppliers/<id>/edit", methods=['GET'])
def edit_supplier(id):
    supplier = supplier_repository.select(id)
    return render_template('suppliers/edit.html', supplier = supplier)

# UPDATE
# PUT '/suppliers/<id>'
@suppliers_blueprint.route("/suppliers/<id>", methods=['POST'])
def update_supplier(id):
    name = request.form['name']
    link     = request.form['link']
    phone    = request.form['phone']
    supplier = Supplier(name, link, phone)
    supplier_repository.save(supplier)
    return redirect('/suppliers')

# DELETE
# DELETE '/suppliers/<id>'
@suppliers_blueprint.route("/suppliers/<id>/delete", methods=['POST'])
def delete_supplier(id):
    supplier_repository.delete(id)
    return redirect('/suppliers')
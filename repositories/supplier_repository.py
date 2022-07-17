from db.run_sql import run_sql
from models.supplier import Supplier

def save(supplier):
    sql = "INSERT INTO suppliers (name, link, phone) VALUES (%s, %s, %s) RETURNING *"
    values = [supplier.name, supplier.link, supplier.phone]
    results = run_sql(sql, values)
    id = results[0]['id']
    supplier.id = id
    return supplier

def select_all():
    suppliers = []
    sql = "SELECT * FROM suppliers"
    results = run_sql(sql)

    for row in results:
        supplier = Supplier(row['name'], row['link'], row['phone'], row['id'])
        suppliers.append(supplier)
    return suppliers

def delete_all():
    sql = "DELETE FROM suppliers"
    run_sql(sql)
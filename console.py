import pdb 
from models.supplier import Supplier
from models.product import Product
import repositories.supplier_repository as supplier_repository
import repositories.product_repository as product_repository

supplier_repository.delete_all()
product_repository.delete_all()

supplier1 = Supplier("Brakes", "https://www.brake.co.uk/", "0345606 9090")
supplier_repository.save(supplier1)

supplier2 = Supplier("Mark Murphy", "https://www.brake.co.uk/", "0345606 9090")
supplier_repository.save(supplier2)

supplier3 = Supplier("Campbells", "https://www.brake.co.uk/", "0345606 9090")
supplier_repository.save(supplier3)

product1 = Product("Burger", 0, 0.7, 8, supplier1)
product_repository.save(product1)

product2 = Product("Fish", 0, 0.7, 8, supplier3)
product_repository.save(product2)

product3 = Product("Bacon", 0, 0.7, 8, supplier1)
product_repository.save(product3)

product4 = Product("Black Pudding", 0, 0.7, 8, supplier1)
product_repository.save(product4)




# TESTING

result = supplier_repository.products(supplier1)
for supplier in result:
    print(supplier.__dict__)

# product_repository.update(product4)
# supplier_repository.delete(1)
# product_repository.delete(3)
# result = product_repository.select_all()
# for product in result:
#     print(product.__dict__)
# supplier_repository.update(supplier3)
# supplier_repository.delete(1)
# result = supplier_repository.select(15)
# print(result.name)
# result = supplier_repository.select_all()
# for supplier in result:
#     print(supplier.__dict__)


pdb.set_trace()
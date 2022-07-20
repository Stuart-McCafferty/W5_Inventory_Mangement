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

product5 = Product("Burger", 0, 0.7, 8, supplier1)
product_repository.save(product5)

product6 = Product("Fish", 0, 0.7, 8, supplier3)
product_repository.save(product6)

product7 = Product("Bacon", 0, 0.7, 8, supplier1)
product_repository.save(product7)

product8 = Product("Black Pudding", 0, 0.7, 8, supplier1)
product_repository.save(product8)

product9 = Product("Burger", 0, 0.7, 8, supplier1)
product_repository.save(product9)

product10 = Product("Fish", 0, 0.7, 8, supplier3)
product_repository.save(product10)

product11 = Product("Bacon", 0, 0.7, 8, supplier1)
product_repository.save(product11)

product12 = Product("Black Pudding", 0, 0.7, 8, supplier1)
product_repository.save(product12)





# TESTING

result = product_repository.select_all()
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
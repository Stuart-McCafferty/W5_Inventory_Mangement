import pdb 
from models.supplier import Supplier
from models.product import Product
from models.meal import Meal
from models.meal_product import Meal_Product
import repositories.supplier_repository as supplier_repository
import repositories.product_repository as product_repository
import repositories.meal_repository as meal_repository
import repositories.meal_product_repository as meal_product_repository

supplier_repository.delete_all()
meal_repository.delete_all()
product_repository.delete_all()


supplier1 = Supplier("Brakes", "https://www.brake.co.uk/", "0345606 9090")
supplier_repository.save(supplier1)

supplier2 = Supplier("Mark Murphy", "https://totalproducelocal.co.uk/depot/edinburgh-foodservice/", "0131 335 3040")
supplier_repository.save(supplier2)

supplier3 = Supplier("Campbells", "https://www.campbellsmeat.com/", "0131 526 4444")
supplier_repository.save(supplier3)

# MEALS

meal1 = Meal("Cheese and Bacon Burger", True)
meal_repository.save(meal1)

meal2 = Meal("Fish and Chips", True)
meal_repository.save(meal2)

# CB BURGER 
product1 = Product("Burger", 10, 0.7, 8, 9, supplier3)
product_repository.save(product1)

product2 = Product("Bacon", 10, 0.2, 0.70, 10, supplier3)
product_repository.save(product2)

product3 = Product("Lettuce", 10, 0.2, 0.70, 9, supplier2)
product_repository.save(product3)

product4 = Product("Tomato", 10, 0.2, 0.70, 9, supplier2)
product_repository.save(product4)

product5 = Product("Brioche buns", 10, 0.2, 0.70, 9, supplier1)
product_repository.save(product5)

product6 = Product("Cheese", 10, 0.2, 0.70, 9, supplier2)
product_repository.save(product6)
# ALSO CHIPS HERE


# Fish n Chips

product7 = Product("Fish", 10, 0.7, 8, 9, supplier3)
product_repository.save(product7)

product8 = Product("Peas", 10, 0.2, 0.70, 9, supplier2)
product_repository.save(product8)

product9= Product("Lemon", 10, 0.2, 0.70, 9, supplier2)
product_repository.save(product9)

product10 = Product("Chips", 10, 0.2, 0.70, 9, supplier1)
product_repository.save(product10)


# Cheese and Bacon Burger W/ Chips
meal_product1 = Meal_Product(meal1, product1)
meal_product_repository.save(meal_product1)

meal_product2 = Meal_Product(meal1, product2)
meal_product_repository.save(meal_product2)

meal_product3 = Meal_Product(meal1, product3)
meal_product_repository.save(meal_product3)

meal_product4 = Meal_Product(meal1, product4)
meal_product_repository.save(meal_product4)

meal_product5 = Meal_Product(meal1, product5)
meal_product_repository.save(meal_product5)

meal_product6 = Meal_Product(meal1, product6)
meal_product_repository.save(meal_product6)

meal_product7 = Meal_Product(meal1, product10)
meal_product_repository.save(meal_product7)

# Fish and Chips
meal_product8 = Meal_Product(meal2, product7)
meal_product_repository.save(meal_product8)

meal_product9 = Meal_Product(meal2, product8)
meal_product_repository.save(meal_product5)

meal_product10 = Meal_Product(meal2, product9)
meal_product_repository.save(meal_product6)

meal_product11 = Meal_Product(meal2, product10)
meal_product_repository.save(meal_product11)




# TESTING

result = meal_repository.select_all()
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
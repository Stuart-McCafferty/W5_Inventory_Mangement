import pdb 
from models.supplier import Supplier
import repositories.supplier_repository as supplier_repository
# import repositories.product_repository as product_repository

supplier_repository.delete_all()


supplier1 = Supplier("Brakes", "https://www.brake.co.uk/", "0345606 9090")
supplier_repository.save(supplier1)

supplier2 = Supplier("Mark Murphy", "https://www.brake.co.uk/", "0345606 9090")
supplier_repository.save(supplier2)

supplier3 = Supplier("Campbells", "https://www.brake.co.uk/", "0345606 9090", 1)




# supplier_repository.update(supplier3)
# supplier_repository.delete(1)
# result = supplier_repository.select(15)
# print(result.name)
# result = supplier_repository.select_all()
# for supplier in result:
#     print(supplier.__dict__)


pdb.set_trace()
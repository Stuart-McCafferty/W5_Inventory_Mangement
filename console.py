import pdb 
from models.supplier import Supplier
import repositories.supplier_repository as supplier_repository
# import repositories.product_repository as product_repository

supplier_repository.delete_all()


supplier1 = Supplier("Brakes", "https://www.brake.co.uk/", "0345606 9090")
supplier_repository.save(supplier1)


result = supplier_repository.select_all()
for supplier in result:
    print(supplier.__dict__)


pdb.set_trace()
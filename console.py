import pdb 
from models.supplier import Supplier
import repositories.supplier_repository as supplier_repository

supplier_repository.delete_all()

supplier1 = Supplier("Brakes", "https://www.brake.co.uk/", "0345606 9090")
supplier_repository.save(supplier1)



pdb.set_trace()
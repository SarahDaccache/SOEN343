from models import Delivery
from .package_controller import PackageController

class DeliveryController:
    del_id = 0
    deliveries = list()

    def getInstance():
        return DeliveryController()
    
    def extract_delivery(self, form):
       id = DeliveryController.del_id
       sender = form["sender"] 
       recipient = form["recipient"]
       
       package_controller = PackageController.getInstance()
       package = package_controller.extract_package(form)
       
       DeliveryController.del_id += 1
       delivery = Delivery(id, sender, recipient, package)
       DeliveryController.deliveries.append(delivery)
    

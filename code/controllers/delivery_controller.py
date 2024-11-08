from models import Delivery
from .package_controller import PackageController

class DeliveryController:
    del_id = 0
    instance = None
    deliveries = list()

    def getInstance():
        if DeliveryController.instance is None:
            DeliveryController.instance = DeliveryController()

        return DeliveryController.instance
    
    def extract_delivery(self, form):
       id = DeliveryController.del_id
       sender = form["sender"] 
       recipient = form["recipient"]
       
       package_controller = PackageController.getInstance()
       package = package_controller.extract_package(form)
       
       DeliveryController.del_id += 1
       delivery = Delivery(id, sender, recipient, package)
       DeliveryController.deliveries.append(delivery)

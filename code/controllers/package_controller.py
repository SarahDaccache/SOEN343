from models import Package

class PackageController:
    pack_id = 0
    instance = None

    def getInstance():
        if PackageController.instance is None:
            PackageController.instance = PackageController()

        return PackageController.instance
    
    def extract_package(self, form):
       id = PackageController.pack_id
       pickup = form["pickup"]
       dropoff = form["dropoff"]
       weight = form["weight"]
       
       PackageController.pack_id += 1
       
       return Package(id, pickup, dropoff, weight)

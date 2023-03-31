import MOOSERecoded as moose
import random



def determineMaxSpeed(hp, weight):
    return round((300 * hp ** (1/3)) / (weight ** (1/3)), 0)

def createVehicle(page, id):
    vehicle = page["vehicles"][id]
    class object:
        id = vehicle
        page
        def carryPart(part):
            object.page[part]
            
    return object
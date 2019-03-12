# this function downloads vehicle data from the ST website, extracts relevant info into a Vehicle class Object,
# and stores all of these objects in an array called vehicles.
import urllib.request
import datetime as dt
import json

class Vehicle:
    def __init__(self, idnum, name, enabled, tracker_id):
        self.idnum = idnum
        self.name = name
        self.enabled = enabled
        self.tracker_id = tracker_id
    def print(self):
         print("ID: " + str(self.idnum) + "; Name: " + self.name + "; Enabled: " + str(self.enabled) +
               "; Tracker ID: " + str(self.tracker_id) + "\n")
            

def getVehicles(vehicles):
    # this code extracts vehicle data from downloaded file
     for j in data:
        # each entry in j is a data entry about a vehicle, loop through all of these.
            # extract relevant data from this entry
            idnum = j["id"]
            name = j["name"]
            enabled = j["enabled"]
            tracker_id = j["tracker_id"]
            # create vehicle object and add to vehicles array
            tempVehicle = Vehicle(idnum, name, enabled, tracker_id)
            vehicles.append(tempVehicle)
            tempVehicle.print()
            
           
            
if __name__ == '__main__':
        # Download the vehicle data from website
        url = "http://shuttles.rpi.edu/vehicles"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
       # print(data)
        # array to hold vehicles
        vehicles = []
        getVehicles(vehicles)

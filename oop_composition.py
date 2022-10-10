class Efficiency:
    #mpg storage for each cars make
    data = { 
            "ford": [],
            "honda": [],
            "nissan": [],
            "toyota": [],
            "subaru": []
        }
    
    #constructor builds and appends to data list if there are kwargs
    def __init__(self,brand = None, economy = None): 
        self.brand = brand
        self.economy = economy
        
        #if there are no arguments it doesn't need to append to data 
        if brand is not None and economy is not None:
            self.data[brand].append(economy)
    
    #calculate average mileage stored in data dictionary
    def average(self, brand):
        if brand in self.data:
            data = self.data[brand]
            return sum(data) / len(data)
        return -1 #if vehicle make isnt in the dictionary

class vehicle: 
    def __init__(self, make, model, mileage):
        self.make = make
        self.model = model
        self.mileage = mileage
        #calls efficiency class as a composite to store make and mileage in data dictionary
        self.fuel = Efficiency(make,mileage)
    
    #average for this vehicles make mpg callable for each vehicle object
    def average(self):
        return self.fuel.average(self.make)

#main function runs unless imported as a module
def main():

    #initialize blank efficiency object to access functions 
    efficiency = Efficiency()
    
    #list of vehicle objects to pull from
    vehicles = [
        vehicle(
            make = "ford",
            model = "fusion",
            mileage = 40
        ),
        vehicle(
            make = "ford",
            model = "f150",
            mileage = 10
        ),
        vehicle(
            make = "honda",
            model = "element",
            mileage = 15
        ),
        vehicle(
            make = "honda",
            model = "accord",
            mileage = 40
        ),
        vehicle(
            make = "nissan",
            model = "maxima",
            mileage = 33
        ),
        vehicle(
            make = "nissan",
            model = "altima",
            mileage = 37
        ),
        vehicle(
            make = "subaru",
            model = "outback",
            mileage = 17
        ),
        vehicle(
            make = "subaru",
            model = "crosstrek",
            mileage = 22
        ),
        vehicle(
            make = "toyota",
            model = "camry",
            mileage = 42
        ),
        vehicle(
            make = "toyota",
            model = "tacoma",
            mileage = 17
        ),
        vehicle(
            make = "toyota",
            model = "corolla",
            mileage = 43
        ),   
        vehicle(
            make = "ford",
            model = "festiva",
            mileage = 39
        )
    ]
    
    #calculate average make mpg given a vehicle make
    make = "ford"
    print(efficiency.average(make))

    #calculate average make mpg of vehicle object
    print(vehicles[0].average())

#runs program automatically unless its imported as a module
if __name__=='__main__':
    main() 

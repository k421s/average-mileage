#assuming list of initialized objects - object is outside of the function
class Efficiency:
    
    #mpg storage for each cars make
    data = { 
            "ford": [],
            "honda": [],
            "nissan": [],
            "toyota": [],
            "subaru": []
        }
    
    def __init__(self,brand = None, economy = None): 
        self.brand = brand
        self.economy = economy
        #if init has args it's a component of vehicles
        if brand is not None and economy is not None:
            self.data[brand].append(economy)
    
    #calculate average mpg by pulling from 
    def average(self, brand):
        if brand in self.data:
            data = self.data[brand]
            return sum(data) / len(data)
        return -1 #if vehicle make isnt in the dictionary

class vehicle: 
    #standard constructor
    def __init__(self, make, model, mileage):
        self.make = make
        self.model = model
        self.mileage = mileage
        self.fuel = Efficiency(make,mileage) #this lets us call average mpg for any initialized object with a make type
    
    #average for this vehicles make mpg
    def average(self):
        return self.fuel.average(self.make)
#vehicles as a list of vehicle objects

def main():
    print((40 + 10 + 39) / 3)
    efficiency = Efficiency()
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
    
    #real related function call
    make = "ford"
    print(efficiency.average(make))

    print(Efficiency.data)
    print(vehicles[0].average())

if __name__=='__main__':
    main() 

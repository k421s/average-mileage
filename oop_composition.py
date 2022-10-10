#assuming list of initialized objects - object is outside of the function
#TODO refactor into something like "Economy"
#TODO more vehicles in vehicles list
#TODO empty and wrong make check functions
#TODO make real function call with make in main function
#TODO doc strings

class Efficiency:
    data = { 
            "ford": [],
            "honda": [],
            "nissan": [],
            "toyota": [],
            "subaru": []
        }
    
    def __init__(self,brand,economy): 
        self.brand = brand
        self.economy = economy
        #now I need to load it into the class member
        self.data[brand].append(economy)
    
    #calculate average mpg by pulling from 
    def average(self, brand):
        if brand in self.data:
            data = self.data[brand]
            return sum(data) / len(data)
        else: return -1 #if vehicle make isnt in the dictionary

class vehicle: 
    #standard constructor
    def __init__(self, make, model, mileage):
        self.make = make
        self.model = model
        self.mileage = mileage
        self.obj_mpg = Efficiency(make,mileage) #this lets us call average mpg for any initialized object with a make type

    def make_average_mpg(self):
        return self.obj_mpg.average(self.make)
#vehicles as a list of vehicle objects

def main():
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
        
    ]

    make = "ford"
    print("hello")

    print(Efficiency.data)
    print(vehicles[0].make_average_mpg())

if __name__=='__main__':
    main() 

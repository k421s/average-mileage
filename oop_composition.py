#assuming list of initialized objects - object is outside of the function
#TODO refactor into something like "Economy"
#TODO more vehicles in vehicles list
#TODO empty and wrong make check functions

class Efficiency:
    data = { 
            "ford": [],
            "honda": [],
            "nissan": []
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
            model = "crv",
            mileage = 20
        )
    ]

    make = "ford"
    print("hello")

    print(Efficiency.data)
    print(vehicles[0].make_average_mpg())

if __name__=='__main__':
    main() 

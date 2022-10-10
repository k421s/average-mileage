#assuming list of initialized objects - object is outside of the function
#TODO refactor into something like "Economy"
#TODO more vehicles in vehicles list
#TODO empty and wrong make check functions
#TODO change names


class mpg_aggregate:
    mpg_dict = { 
            "ford": [],
            "honda": [],
            "nissan": []
        }
    
    def __init__(self,make,mileage): 
        self.make = make
        self.mileage = mileage
        #now I need to load it into the class member
        self.mpg_dict[make].append(mileage)
    
    #calculate average mpg by pulling from 
    def calc_average_mpg(self, input_make_str):
        if input_make_str in self.mpg_dict:
            make_mpg_list = self.mpg_dict[input_make_str]
            average_mpg = sum(make_mpg_list) / len(make_mpg_list)
            return average_mpg
        else: return -1 #if vehicle make isnt in the dictionary

class vehicle: 
    #standard constructor
    def __init__(self, make, model, mileage):
        self.make = make
        self.model = model
        self.mileage = mileage
        self.obj_mpg = mpg_aggregate(make,mileage) #this lets us call average mpg for any initialized object with a make type

    def make_average_mpg(self):
        return self.obj_mpg.calc_average_mpg(make)
#vehicles as a list of vehicle objects


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

print(mpg_aggregate.mpg_dict)
print(vehicles[0].make_average_mpg())

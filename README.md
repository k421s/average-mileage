# average-mileage
Calculate average mileage of vehicle make given a list of objects and a make to search for

The way the original list of vehicles was set up reminded me of c structs so the program is written with the assumption that it was a struct type of object translated to python as a list of vehicle objects.

## main components 
List of vehicle objects to calculate average mileage from
```python
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
        ...
        ...
```

The main component of this program is the mpg data list: 

```python
data = { 
            "ford": [],
            "honda": [],
            "nissan": [],
            "toyota": [],
            "subaru": []
        }
```
It stores a list of every vehicle's mpg by make to be pulled from by the average calculating function 

## coupling
There are two classes: Vehicle and Efficiency. 

```python
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
```

Instead of looping through the list every time an average needed to be calculated the mpg data is organized and stored in the `Efficiency` class every time a `Vehicle` is initialized. which is still a linear process but it will save time if multiple averages are calculated and makes more sense (to me).

`Efficiency` is designed to be a component for `Vehicle`, every time a new vehicle object is initialized it initializes an Efficiency object and sends it the make and mileage data to be stored in the `data` list via:

` self.fuel = Efficiency(make,mileage)`

This organizes the data and it also allows average mileage calculation on the current objects make without having to pass a parameter to it. 

for example: 
`print(vehicles[0].average())` 
would print: 
> 29.666666666666668

which is vehicle ones make, `"ford"`, average mpg.


# average-mileage
Calculate average mileage of vehicle make given a list of objects and a make to search for

The way the original list of vehicles was set up reminded me of c structs so the program is written with the assumption that it was a struct type of object translated to python as a list of vehicle objects.

## main components 
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

Instead of looping through the list every time an average needed to be calculated the mpg data is organized and stored in the `Efficiency` class every time a `Vehicle` is initialized. which is still a linear process but it will save time if multiple averages are calculated and makes more sense (to me).

`Efficiency` is designed to be a component for `Vehicle`, every time a new vehicle object is initialized it initializes an Efficiency object and sends it the make and mileage data to be stored in the `data` list via:

` self.fuel = Efficiency(make,mileage)`

This organizes the data and it also allows average mileage calculation on the current objects make without having to pass a parameter to it. 

for example: 
`print(vehicles[0].average())` 
would print: 
> 29.666666666666668
which is vehicle ones make, `"ford"`, average mpg.


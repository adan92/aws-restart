import csv
import copy

myVehicle = {
    "vin": "<empty>",
    "make": "<empty>",
    "model": "<empty>",
    
    "year": 0,
    "range": 0,
    "topSpeed": 0,
    "zeroSixty": 0,
    "mileage": 0
    
}

with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile,delimiter=',')
    lineCount = 0
    
    for row in csvReader:
        if lineCount == 0:
            print(f"Las columnas son: {', '.join(row)} ")
            lineCount +=1
        else:
            lineCount +=1
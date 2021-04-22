from datetime import datetime
import os
possible_field_types = [
    {
        "type": "int",
        "lenght-min": 1,
        "lenght-max" : 25
    },
    {
        "type": "float",
        "lenght-min": 1,
        "lenght-max" : 7
    },
    {
        "type": "char",
        "lenght-min": 1,
        "lenght-max" : 255
    },
    {
        "type": "text",
        "lenght-min": -1,
        "lenght-max" : -1
    }]

for i in possible_field_types:
    print(i)

dateTimeObj = datetime.now()
timestamp = dateTimeObj.strftime("%Y%m%d")
print(timestamp)

print(os.getcwd())



    a.property
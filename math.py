import json

x = {
    "name": "huong",
    "age": 30,
    "married": True,
    "discover": False,
     "cars": [
         {
             "model": "mmmm", "mps": 29.5
         },
         {
             "model": "sss", "mps": 20
         }
     ]
}
print(json.dumps(x, indent=4))
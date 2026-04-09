

# Python JSON



# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.



# JSON in Python
# Python has a built-in package called json, which can be used to work with JSON data.
def pause():
    """Pauses the script and waits for user input to continue."""
    if input('continue? [y/n] ').lower() != 'y':
        exit()

print('---------------------[1 JSON to Python]-----------------------')


import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])

pause()



print('---------------------[2 Python to JSON]-----------------------')

# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

import json

# a Python object (dictionary):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)

# NOTE, in JSON the key part must always be a string

pause()

print('---------------------[3 Python to JSON]-----------------------')


# You can convert Python objects of the following types, into JSON strings:

# dict
# list
# tuple
# string
# int
# float
# True
# False
# None


print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

pause()

print('---------------------[4 Python to JSON]-----------------------')

# When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

# Python	JSON
# dict	Object
# list	Array
# tuple	Array
# str	    String
# int	    Number
# float	Number
# True	true
# False	false
# None	null

# Convert a Python object containing all the legal data types:

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent = 4))

pause()

print('---------------------[5 Reading External JSON]-----------------------')



import json

# Open file using streaming 
with open("00_week_8/data.json", "r") as file:
    data = json.load(file)  # parse JSON directly from file stream

# Access data
for user in data["users"]:
    print(user["name"], user["age"])




pause()


print('---------------------[6 Adding to External JSON]-----------------------')


import json

# Step 1: Read existing JSON
with open("00_week_8/data.json", "r") as file:
    data = json.load(file)

# Step 2: Add new data
new_user = {"name": "sam", "age": 30}
data["users"].append(new_user)

# Step 3: Write back to file
with open("00_week_8/data.json", "w") as file:
    json.dump(data, file, indent=4)

print('Data added!')
pause()
print('---------------------[7 SEATWORK ACTIVITY]-----------------------')

# 1
# create a new file users.json
# create a basic console app that would register user and add it to user.json
# fields: "username, "password"
# add loop or something


# 2
# make a simple login simulator






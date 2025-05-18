#dictionary - a collection of {key: value} pairs
#ordered unchangable no duplicates
capital_cities = {"usa": "Washington, D.C.", "france": "Paris", "germany": "Berlin", "uk": "London", "spain": "Madrid"}
print(capital_cities)
#for know the method and value of dictionary
# print(dir(capital_cities)) # to know the keys of dictionary
#to get the value of a key
print(capital_cities["usa"])
# if python does not find a value for the key, it will give an error 
# print(capital_cities["usa1"]) # it will give an  none
#that how we see the key is exit or not in the dictionary
capital_cities.update({"germany": "Berlin", "uk": "London"}) # we can add 
capital_cities.update({"usa":"barlin"})#we can update the value of the key
# we can add a new key and value
print(capital_cities)
# we can remove a key and value
capital_cities.pop("usa") # we can remove the key and value
print(capital_cities)
# we can remove the last key and value
capital_cities.popitem() # we can remove the last key and value
print(capital_cities)
# we can remove all the key and value   
capital_cities.clear() # we can remove all the key and value
print(capital_cities)
# we can remove the key and value 
capital_cities = {"usa": "Washington, D.C.", "france": "Paris", "germany": "Berlin", "uk": "London", "spain": "Madrid"}
print(capital_cities)
keys = capital_cities.keys() # we can get the keys of the dictionary
print(keys) #keys is an object which resemble a list
# we can convert the keys to a list
keys = list(capital_cities.keys()) # we can convert the keys to a list
print(keys) #keys is an object which resemble a list
for key in capital_cities.keys(): # we can get the keys of the dictionary
    print(key) #keys is an object which resemble a list
# we can get the values of the dictionary
values = capital_cities.values() # we can get the values of the dictionary
print(values) #values is an object which resemble a list
# we can convert the values to a list
values = list(capital_cities.values()) # we can convert the values to a list
print(values) #values is an object which resemble a list
for value in capital_cities.values(): # we can get the values of the dictionary
    print(value) #values is an object which resemble a list
item=capital_cities.items()
print(item) #items is an object which resemble a list
for key, value in capital_cities.items(): # we can get the keys and values of the dictionary
    print(f"{key}: {value}") #items is an object which resemble a list
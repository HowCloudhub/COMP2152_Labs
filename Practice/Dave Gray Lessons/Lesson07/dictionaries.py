# Dictionaries  a little similar to Java Script Objects
# Key Value pairs.
band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vacals="Plant", guitar="Page")

print(band)
print(band2)

# Access items in the dictionary


print(band["vocals"])
print(band.get("guitar"))

print(band.keys())

print(band.values())

# lists all key value pairs as Tuples
print(band.items())

# verify if a key exists
print("guitar" in band)
print("Cowbell" in band)

# Change values in Dictionary

band["guitar"] = "Cheap"
print(band)

band.update({"bass": "JPJ"})

print(band)

# remove items.

print(band.pop("bass"))
print(band)

band["drums"] = "Munir"

print(band)

print(band.popitem())
print(band)

# delete and clear items

band["drums"] = "Munir"
del band["drums"]
print(band)

band2.clear()

print(band2)

del band2

#Copy Dictionary

band2 = band    #creates a reference. Does not create a copy   
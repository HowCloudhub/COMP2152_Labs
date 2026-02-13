# Crtl B to hide the side bar.

users = ["Dave", "John", "Sara"]

data = ["Munir", 42, "Good Man"]

emptylist = []
print("Dave" in users)

print(users[0])
print(users[-1])

print(users.index("John"))
print(users[0:2])
print(users[1:])
print(users[-3:-1])

users += ["Jason"]
print("")
print(users)
users.extend(["Jason Bourn"])
print(users)

users.insert(0, "Bob")
print(users)

# This will not remove any date from the existing list.
users[2:2] = ["Eddie", "Alex"]
print(users)

# This WILL remove previous data occupying index 1 and 2
users[1:3] = ["Jesica", "Connor"]
print(users)


users.remove("Jason")
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

data = ["Munir", 40, "Handsome"]
print(data)

users[1:2] = ["dave"]
users.sort(key=str.lower)
print(users)

num = [4, 43, 23, 45, 89]
print(f"Original num: {num}")
num.reverse()
print(f"after num.reverse() : {num}")

num.sort(reverse=True)
print(f"num.sort(reverse=True) {num}")

# num.sort()  # sort always sorts in assending order.
# print(f"num.sort() {num}")

print(sorted(num, reverse=True))
print(num)

numscopy = num.copy()
mynums = list(num)
mycopy = num[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(num)


# Tuples.  Lists where data and order of data don't change

mytuple = tuple(("Dave", "Munir", "Max"))
antohertuple = (1, 4, 2, 8, 3, 5, 6)

print(type(mytuple))
print(antohertuple)

newlist = list(mytuple)
newlist.append("David")
newtuple = tuple(newlist)
print(newtuple)
print(type(newtuple))

# unpacking. Tuples.  * will unpack into a list.
(one, *two, whateves, hello) = antohertuple

print(one)
print(two)
print(whateves)
print(hello)

# count the number of items in a Tuple.
print(antohertuple.count(0))

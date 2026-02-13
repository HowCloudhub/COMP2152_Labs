# print(42 == 42)

x = True
y = False
z = True

print(not x)
# Checks if both are true. But in practice only checks Y if X is True. In this case x is true- so checks y. y is false- so both are not true.
print(x and y)
# Checks if both are true. Since y is false- does not check x anymore.
print(y and x)
# Checks if either is true. going from left to right, x is true , so it does not check y anymore.
print(x or y)
print(y or x)  # checks if either is ture- going from left to right.

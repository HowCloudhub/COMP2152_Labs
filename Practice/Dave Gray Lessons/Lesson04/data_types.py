# Srting Data Type.


# Literal Assignment . Just literally stating Frist = Name.
import math
first = "Munir"
last = "Howlader"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))


# cosntructor Function.  Wrting the assignment in a constructor style.
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))


# concatanation.   Adding two strings.
fullname = first + " " + last
print(fullname)

fullname += "!"

print(fullname)

# Castig a number to a string.
decade = str(1980)
year = int(19)
print(type(decade))
print(decade)

statement = "I like rock music from the " + decade + 's.'
print(statement)

# Multiple Lines.
multiline = '''
Hey, how are you?  

I was just checking in of. 

                All good? 

'''
print(multiline)


# Escaping spelaial characters.
sentence = 'I\'m back at workd\tHey!\n\nWhere\'s this at \\located?'
print(sentence)


# String Methods

print(first)
print(first.lower())
print(first.upper())
print(first)


print(multiline.title())
print(multiline.replace("good", "okay"))

print(len(multiline))
multiline += "                                 "
multiline = "                   " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

# Build a Menu
print("")

title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$3".rjust(4))
print("Timbits".ljust(16, ".") + "$2".rjust(4))


print("")

# String Index Value
print(first[-1])  # value at the last index
# for a range the does - it does not include the end index. It stops one index prior.
print(first[1:-1])
print(first[1:])  # For range staring from one point till end point value


# some methods return boolean value
print(first.startswith("D"))
print(first.endswith("R"))


# Boolean Data Type
myvalue = True
x = bool(False)
print(isinstance(myvalue, bool))


# Numeric Data Types

# Integer types

price = 100
best_price = int(80)


# float type (has decimals)

gpa = 3.25
y = float(1.14)
print(isinstance(y, float))
print(type(gpa))


# complex Types (mainly used in Engeneering)
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)


# Built in function for numbers
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))


# import math

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# You will have an error if you try to cast incorrect data.
# Integer casting cannot be done for letters. Can have numbers only.
# integer = int(f3fe3f)  >> this will give you an error.

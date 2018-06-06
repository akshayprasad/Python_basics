#printing the output with single quoted and double quoted string.
print('Just logging and looking at print directive example: ')
print('Hello World!!!')
print("Hello World!!!")
print("\n")

#Variables of type integer and float
print('Looking at the difference of Integer and Float: ')
integerVariable = 10
print(integerVariable)

floatVariable = float(integerVariable)
print(floatVariable)
print("\n")

#stirng 
print('Single quote and doublequote assignment: ')
singleQuote = 'Hello'
doubleQuote = "Hello"

print(singleQuote)
print(doubleQuote)
print("\n")

#Operators assignment in a single line
print('multiple variables assignment in a single line: ')
a,b = 2,4
print(a,b)
print("\n")


#List(Array) working example
print('Working of list example: ')
listVariable = []
listVariable.append(1)
listVariable.append(2)
listVariable.append(3)
print(listVariable[0]) # prints 1
print(listVariable[1]) # prints 2
print(listVariable[2]) # prints 3

for x in listVariable:
    print(x)
print("\n")

# Basic operators
print("Basic operators and it's working: ")
print(1+2+3/3)

remainder = 11 % 3
print(remainder)

squared = 7 ** 2
cubed = 2 ** 3

print(squared)
print(cubed)
print("\n")

#using operators with string
print("Operators that's been applied on strings: ")
helloworld = "hello" + " " + "world"
print(helloworld)

surprisehellos = "hello" * 10
print(surprisehellos)
print("\n")

#using operators with Lists
print('Operator applied on list: ')
even = [2,4,6,8]
odd = [1,3,5,7]
allNumbers = odd + even
print(allNumbers) 

print([5,6] * 3) 
print("\n")

# String Formatting
print("String formatting example: ")
name = "python"
print("World of, %s!" % name) 

name = "python"
version = 3.5
print("%s latest version is %.2f" % (name, version))
print("\n")

# Basic String operations
print('Basic String operations: ')
stringVariable = "python learning and knowing it's basic syntax."

print(len(stringVariable)) 

print(stringVariable.index('o'))

print(stringVariable.count('o'))

print(stringVariable.upper()) 

print(stringVariable.lower()) 

print(stringVariable.startswith('python')) 

print(stringVariable.endswith('syntax')) 
print("\n")

#Special list operations
print('Special list operations:')
stringVariable = "Hello world!"
print(stringVariable[3:7]) 
print(stringVariable[3:7:1])

print(stringVariable[3:7:2]) 

print(stringVariable[::-1]) 

print(stringVariable.split(" ")) 
print("\n")

#Conditions
print("Working of conditions: ")
x = 2
print(x == 2) 
print(x == 3)
print(x < 3)
print("\n")

#Boolean operators
print("Boolean operators: ")
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")
print("\n")

#The "in" operator
print("The working of 'in' operator: ")
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")
print("\n")

#The 'is' operator
print("Working of 'is' operator: ")
x = [3,4,5]
y = [3,4,5]
print(x == y) 
print(x is y) 
print("\n")

#The "not" operator
print("The working of not operator: ")
print(not False) 
print((not False) == (False))
print("\n")

# Loops
print("For loop example: ")
odds = [1, 3, 5, 7]
for number in odds:
    print(number)
print("\n")

#for loop with range
print("for loop with range option: ")
for number in range(5):
    print(number)
print("\n")

#usage of while loop
print('While loop example: ')
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1
print("\n")

#usage of break and continue in looping statements
print('break and continue usage in a loop: ')
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
print("\n");

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)
print("\n")

#usage of else clause in a loop
print("usage of else clause in a loop: ")
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))
print("\n")

#Functions in python
print("Functions definition in python: ")
def my_function():
    print("Hello From My Function!")

my_function()
print("\n")


#Classes and Objects
print('class and objects example: ')
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

# Then print out both values
print(myobjectx.variable) 
print(myobjecty.variable)
print("\n")


#Dictionaries
print("Ditionaries in python example: ")
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781

del phonebook["John"]

for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
print("\n")


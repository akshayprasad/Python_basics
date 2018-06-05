<p align="center">
  <a href="http://gulpjs.com">
    <img  src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5Tm_-tuYOXvaJUBLGyl00bo3zvrQmmZon1CHTwgvTc2Bb9c7E">
  </a>
  <p align="center">** Python-Basics **</p>
</p>

## What is Python?
Python is a very simple language, and has a very straightforward syntax. It encourages programmers to program without prepared code. The simplest directive in Python is the "print" directive - it simply prints out a line.

There are two major Python versions, Python 2 and Python 3. Python 2 and 3 are quite different. This tutorial uses Python 3, because it more semantically correct and supports newer features.

To print a string in Python 3, just write:
print("This line will be printed.");

### Indentation
Python uses indentation for blocks, instead of curly braces. Both tabs and spaces are supported, but the standard indentation requires standard Python code to use four spaces
```js
if name == 'Python':
        print(name);
```


## Variables and Types
<ul>
    <li>Python is completely object oriented, and not "statically typed".</li>
    <li>No need to declare variables before using them or declare their type.</li>
    <li>Every variable in Python is an object.</li>
</ul>

### Numbers
Python supports two types and they are:
<ol>
<li> Integer </li>
<li> Floating </li>
</ol>

```js
Integer:

intergerValue = 10;
print(integerValue); //Outputs 10

floatValue = float(integerValue);
print(floatValue); //Outputs 10.0
```

### Strings
Strings can be defined either in a double quote or a single quote.

```js
stringValueSingleQuote = 'python';
stringValueDoubleQuote = "python";

print(stringValueSingleQuote) //outputs python
print(stringValueDoubleQuote) //outputs python
```

```js
one = 1
two = 2
three = one + two
print(three) //outputs 3

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld) //outputs hello world
```

There are additional variations on defining strings that make it easier to include things such as carriage returns, backslashes and Unicode characters.
<a href = 'https://docs.python.org/3/tutorial/introduction.html#strings'>For more on Strings</a>


#### Operator assignment
Assignments can be done on more than one variable "simultaneously" on the same line like this:

```js
a,b = 2,4;
print(a,b) //outputs 2,4.
```


## Lists
Lists are very similar to arrays. They can contain any type of variable, and they can contain as many variables as you wish. Lists can also be iterated over in a very simple manner. Here is an example of how to build a list.

```js
listVariable = []
listVariable.append(1)
listVariable.append(2)
listVariable.append(3)
print(listVariable[0]) # prints 1
print(listVariable[1]) # prints 2
print(listVariable[2]) # prints 3

# prints out 1,2,3
for x in listVariable:
    print(x)

//outputs 1 2 and 3 in a seperate line.
```

## Basic operators
Just as any other programming languages, the addition, subtraction, multiplication, and division operators can be used with numbers.

```js
print(1+2+3/3) //Outputs 2.

remainder = 11 % 3
print(remainder) //Outputs 2

squared = 7 ** 2
cubed = 2 ** 3

print(squared) //outputs 49
print(cubed); //ouputs 8
```

### using operators with string
```js
helloworld = "hello" + " " + "world"
print(helloworld) //outputs hello world

surprisehellos = "hello" * 10
print(surprisehellos) //outputs hellohellohellohellohellohellohellohellohellohello
```

### using operators with Lists
```js
even = [2,4,6,8]
odd = [1,3,5,7]
allNumbers = odd + even
print(allNumbers) //outputs [1, 3, 5, 7, 2, 4, 6, 8]

print([5,6] * 3) //outputs [5, 6, 5, 6, 5, 6]
```

## String Formatting
Python uses C-style string formatting to create new, formatted strings. 
The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s" and "%d".

```js
name = "python"
print("World of, %s!" % name) //Outputs World of python

name = "python"
version = 3.5.1
print("%s latest version is %f" % (name, version)) //Outputs python latest version is 3.5.1
```

List can be also be represented using %s, basically object which is not a string can be formatted using the %s operator as well.
```js
listVariable = [1,2,3]
print("A list: %s" % listVariable) //Outputs [1,2,3]
```

### Important formatters to be remembered
<ul>
  <li>%s - String (or any object with a string representation, like numbers)</li>
  <li>%d - Integers</li>
  <li>%f - Floating point numbers</li>
  <li>%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.</li>
  <li>%x / %X - Integers in hex representation (lowercase/uppercase)</li>
</ul>

## Basic String Operations
Strings are bits of text. They can be defined as anything between quotes

The multiple methods(iun-built) for string are:
<ul>
<li>len()</li>
<li>index()</li>
<li>count()</li>
<li>upper()</li>
<li>lower()</li>
<li>startswith()</li>
<li>endswith()</li>
<li>split()</li>
</ul>

```js
stringVariable = "python learning and knowing it's basic syntax."

print(len(stringVariable)) //Outputs 46

print(stringVariable.index('o')) //Outputs 4

print(stringVariable.count('o')) //outputs 2

print(stringVariable.upper()) //Outputs the string in uppercase

print(stringVariable.lower()) //Outputs the string in lowercase

print(stringVariable.startswith('python')) //Outputs True

print(stringVariable.endswith('syntax')) //Outputs True

```

### Special list operations

```js

stringVariable = "Hello world!"
print(stringVariable[3:7]) or print(stringVariable[3:7:1])//Outputs lo w

print(stringVariable[3:7:2]) //Outputs l

print(stringVariable[::-1]) //Ouputs !dlrow olleH

print(stringVariable.split(" ")) //Outputs ['Hello', 'world!']
```

## Conditions
Python uses boolean variables to evaluate conditions. The boolean values True and False are returned when an expression is compared or evaluated.

```js
x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True
```

### Boolean operators

The "and" and "or" boolean operators allow building complex boolean expressions.
```js
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")
```

### The "in" operator
The "in" operator could be used to check if a specified object exists within an iterable object container, such as a list:
```js
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")
```

<ul>
<li>Python uses indentation to define code blocks, instead of brackets. </li>
<li>The standard Python indentation is 4 spaces, although tabs and any other space size will work, as long as it is consistent. </li>
<li>Notice that code blocks do not need any termination.</li>
</ul>

```js
if <statement is="" true="">:
    <do something="">
    ....
    ....
elif <another statement="" is="" true="">: # else if
    <do something="" else="">
    ....
    ....
else:
    <do another="" thing="">
    ....
    ....
</do></do></another></do></statement>
```

Example:
```js
x = 'NA'
if x == 'NA':
    print("x equals NA!")
else:
    print("x does not equal to NA.")
```

A statement is evaulated as true if one of the following is correct: 
<ol>
<li> The "True" boolean variable is given, or calculated using an expression, such as an arithmetic comparison. </li>
<li> An object which is not considered "empty" is passed. </li>
</ol>


### The 'is' operator
Unlike the double equals operator "==", the "is" operator does not match the values of the variables, but the instances themselves.
```js
x = [3,4,5]
y = [3,4,5]
print(x == y) # Prints out True
print(x is y) # Prints out False
```

### The "not" operator
Using "not" before a boolean expression inverts it:
```js
print(not False) // Prints out True
print((not False) == (False)) // Prints out False
```


## Loops
There are two types of loops in Python, for and while.

### The "for" loop

```js
odds = [1, 3, 5, 7]
for number in odds:
    print(number) //outputs 1 3 5 6 in a seperate line
```


### range() vs xrange()

<ul>
<li>range() and xrange() are two functions that could be used to iterate a certain number of times in for loops in Python. </li>
<li><b>Note: </b>In Python 3, there is no xrange , but the range function behaves like xrange in Python 2.</li>
<li><b>Note: </b>If you want to write code that will run on both Python 2 and Python 3, you should use range().</li>
</ul>

<h3>range()</h3>
<p>This returns a list of numbers created using range() function.</p>

<h3>xrange()</h3>
<p>This function returns the generator object that can be used to display numbers only by looping. Only particular range is displayed on demand and hence called “lazy evaluation“.</p>

<h3>Both are implemented in different ways and have different characteristics associated with them. The points of comparisons are:</h3>
<ul>
<li>Return Type</li>
<li>Memory</li>
<li>Operation Usage</li>
<li>Speed</li>
</ul>


<h3>Return Type</h3>
<ul>
<li>range() returns – the list as return type.</li>
<li>xrange() returns – xrange() object.</li>
</ul>

```js
# Python code to demonstrate range() vs xrange()
# on basis of return type

# initializing a with range()
a = range(1,10)

# initializing a with xrange()
x = xrange(1,10000)

# testing the type of a
print ("The return type of range() is : ")
print (a) //[1,2,3,4,5,6,7,8,9,10]

# testing the type of x
print ("The return type of xrange() is : ")
print (x) //xrange(1, 10)

```

<h3>Example:</h3>

```js
//Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

//Prints out 3,4,5
for x in range(3, 6):
    print(x)

//Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)
```

## "while" loops
<p>While loops repeat as long as a certain boolean condition is met.</p>

```js
//prints out 0,1,2,3,4

count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1
```

### "break" and "continue" statements
<h3>break </h3>
<p>is used to exit a for loop or a while loop</p>

<h3>continue</h3>
<p>is used to skip the current block</p>


```js
//Prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)
```


<h2>Important:</h2>
<h3>can we use "else" clause for loops?</h3>
<p style="color: red;">
unlike languages like C,CPP.. we can use else for loops. When the loop condition of "for" or "while" statement fails then code part in "else" is executed. If break statement is executed inside for loop then the "else" part is skipped. Note that "else" part is executed even if there is a continue statement.
</p>

<h3>Example: </h3>
```js
//Prints out 0,1,2,3,4 and then it prints "count value reached 5"

count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

//Prints out 1,2,3,4
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
```
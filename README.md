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
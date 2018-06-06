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


## Functions

### What are Functions?
<p>Functions are a convenient way to divide your code into useful blocks, allowing us to order our code, make it more readable, reuse it and save some time. Also functions are a key way to define interfaces so programmers can share their code.
</p>

<h3>How do you write functions in Python?</h3>
<p>Python makes use of blocks.</p>

```js
block_head:
    1st block line
    2nd block line
    ...
```

<p>Where a block line is more Python code (even another block), and the block head is of the following format: block_keyword block_name(argument1,argument2, ...) Block keywords you already know are "if", "for", and "while".</p>


<h3>Functions in python are defined using the block keyword "def", followed with the function's name as the block's name.</h3>

```js
def my_function():
    print("Hello From My Function!")

my_function() //prints Hello From My Function!
```


# Import feature
## Classes and Objects
<p>
<ul>
<li>Objects are an encapsulation of variables and functions into a single entity. </li>
<li>Objects get their variables and functions from classes. Classes are essentially a template to create your objects.</li>
</ul>
</p>

<h3>Very basic example is that:</h3>

```js
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")
```

<p>Now the variable "myobjectx" holds an object of the class "MyClass" that contains the variable and the function defined within the class called "MyClass".</p>

### Accessing Object Variables

```js
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()

print(myobjectx.variable) //prints blah
```

<p>You can create multiple different objects that are of the same class(have the same variables and functions defined). However, each object contains independent copies of the variables defined in the class. </p>

```js
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

# Then print out both values
print(myobjectx.variable) //prints blah
print(myobjecty.variable) //prints yackity
```


## Dictionaries
<p>A dictionary is a data type similar to arrays, but works with keys and values instead of indexes. Each value stored in a dictionary can be accessed using a key, which is any type of object (a string, a number, a list, etc.) instead of using its index to address it.</p>

```js
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook) 

//Outputs {'John': 938477566, 'Jack': 938377264, 'Jill': 947662781}
```

<p>Alternatively, a dictionary can be initialized with the same values in the following notation:</p>

```js
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

//Outputs {'John': 938477566, 'Jack': 938377264, 'Jill': 947662781}
```

<h3>Iterating over dictionaries</h3>
<p>Dictionaries can be iterated over, just like a list. However, a dictionary, unlike a list, does not keep the order of the values stored in it. To iterate over key value pairs, use the following syntax:</p>

```js
phonebook = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

//outputs
//Phone number of John is 938477566
//Phone number of Jack is 938377264
//Phone number of Jill is 947662781
```

<h3>Removing a value</h3>
<p>To remove a specified index, use either one of the following notations:</p>

```js
phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
del phonebook["John"]
print(phonebook);

//oputputs {'Jack': 938377264, 'Jill': 947662781}


phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
phonebook.pop("John")
print(phonebook)

//oputputs {'Jack': 938377264, 'Jill': 947662781}
```


## Modules and Packages
<p>In programming, a module is a piece of software that has a specific functionality. For example, when building a ping pong game, one module would be responsible for the game logic, and
another module would be responsible for drawing the game on the screen. Each module is a different file, which can be edited separately.</p>

### Exploring built-in modules
<a href="https://docs.python.org/3/library/">Check out the complete list of built-in modules in the python standard library.</a>

<h3>Two very important functions come in handy when exploring modules in Python:</h3>
<ul>
<li>dir</li>
<li>help</li>
</ul>

<p>We can look for which functions are implemented in each module by using the dir function:</p>

```js
import urllib;
dir(urllib)

//Outputs
/* 
['ContentTooShortError',
 'FancyURLopener',
 'MAXFTPCACHE',
 'URLopener',
 '__all__',
 '__builtins__',
 '__doc__',
 '__file__',
 '__name__',
 '__package__',
 '__version__',
 '_ftperrors',
 '_get_proxies',
 '_get_proxy_settings',
 '_have_ssl',
 '_hexdig',
 '_hextochr',
 '_hostprog',
 '_is_unicode',
 '_localhost',
 '_noheaders',
 '_nportprog',
 '_passwdprog',
 '_portprog',
 '_queryprog',
 '_safe_map',
 '_safe_quoters',
 '_tagprog',
 '_thishost',
 '_typeprog',
 '_urlopener',
 '_userprog',
 '_valueprog',
 'addbase',
 'addclosehook',
 'addinfo',
 'addinfourl',
 'always_safe',
 'basejoin',
 'c',
 'ftpcache',
 'ftperrors',
 'ftpwrapper',
 'getproxies',
 'getproxies_environment',
 'getproxies_macosx_sysconf',
 'i',
 'localhost',
 'main',
 'noheaders',
 'os',
 'pathname2url',
 'proxy_bypass',
 'proxy_bypass_environment',
 'proxy_bypass_macosx_sysconf',
 'quote',
 'quote_plus',
 'reporthook',
 'socket',
 'splitattr',
 'splithost',
 'splitnport',
 'splitpasswd',
 'splitport',
 'splitquery',
 'splittag',
 'splittype',
 'splituser',
 'splitvalue',
 'ssl',
 'string',
 'sys',
 'test',
 'test1',
 'thishost',
 'time',
 'toBytes',
 'unquote',
 'unquote_plus',
 'unwrap',
 'url2pathname',
 'urlcleanup',
 'urlencode',
 'urlopen',
 'urlretrieve']
*/

```


## Numpy Arrays
<p>Numpy arrays are great alternatives to Python Lists. Some of the key advantages of Numpy arrays are that they are fast, easy to work with, and give users the opportunity to perform calculations across entire arrays.</p>

Example:

```js
//Create 2 new lists numbersOdd and numbersEven
numbersOdd = [1, 3, 5, 7]
numbersEven = [2,4,6,8]

//Import the numpy package as np
import numpy as np

# Create 2 numpy arrays from height and weight
np_numbersOdd = np.array(numbersOdd)
np_numbersEven = np.array(numbersEven)

print(type(np_numbersEven))

Outputs:
<class 'numpy.ndarray'>
<class 'numpy.ndarray'>
```

## Pandas Basics

### Pandas DataFrames
<ul>
<li>Pandas is a high-level data manipulation tool developed by Wes McKinney. </li>
<li>It is built on the Numpy package and its key data structure is called the <b>DataFrame</b>. </li>
<li>DataFrames allow you to store and manipulate tabular data in rows of observations and columns of variables.</li>
</ul>

<h3>There are several ways to create a DataFrame. One way way is to use a dictionary. For example:</h3>

```js
dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict)
print(brics)

//Outputs
area    capital       country  population
0   8.516   Brasilia        Brazil      200.40
1  17.100     Moscow        Russia      143.50
2   3.286  New Dehli         India     1252.00
3   9.597    Beijing         China     1357.00
4   1.221   Pretoria  South Africa       52.98


```


<p>As you can see with the new brics DataFrame, Pandas has assigned a key for each country as the numerical values 0 through 4. If you would like to have different index values, say, the two letter country code, you can do that easily as well.</p>

```js

dict = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import pandas as pd
brics = pd.DataFrame(dict)
brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(brics)

//Outputs
      area    capital       country  population
BR   8.516   Brasilia        Brazil      200.40
RU  17.100     Moscow        Russia      143.50
IN   3.286  New Dehli         India     1252.00
CH   9.597    Beijing         China     1357.00
SA   1.221   Pretoria  South Africa       52.98

```

## Generators

<p>Generators are very easy to implement, but a bit difficult to understand.

Generators are used to create iterators, but with a different approach. Generators are simple functions which return an iterable set of items, one at a time, in a special way.

When an iteration over a set of item starts using the for statement, the generator is run. Once the generator's function code reaches a "yield" statement, the generator yields its execution back to the for loop, returning a new value from the set. The generator function can generate as many values (possibly infinite) as it wants, yielding each one in its turn.
</p>

<h3>Example: </h3>

```js
import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1,15)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))


//Outputs
And the next number is... 33!
And the next number is... 17!
And the next number is... 11!
And the next number is... 17!
And the next number is... 10!
And the next number is... 15!
And the next number is... 2!

```

## List Comprehensions

List Comprehensions is a very powerful tool, which creates a new list based on another list, in a single, readable line.

For example, let's say we need to create a list of integers which specify the length of each word in a certain sentence, but only if the word is not the word "the".

<h3>Before list comprehension: </h3>

```js
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
      if word != "the":
          word_lengths.append(len(word))
print(words)

//outputs
['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
```

<h3>After list comprehension: </h3>

```js
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = [len(word) for word in words if word != "the"]
print(words)

//outputs
['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
```

## Multiple Function Arguments
Every function in Python receives a predefined number of arguments.

It is possible to declare functions which receive a variable number of arguments, using the following syntax:

```js
def foo(first, second, third, *therest):
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("And all the rest... %s" % list(therest))
    
foo(1,2,3,4,5,6);

//outputs
First: 1
Second: 2
Third: 3
And all the rest... [4, 5, 6]
```


It is also possible to send functions arguments by keyword, so that the order of the argument does not matter, using the following syntax. 

```js
def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print("Result: %d" %(result))

//outputs
The sum is: 6
Result: 1
```

## Regular Expressions
<p>
Regular Expressions (sometimes shortened to regexp, regex, or re) are a tool for matching patterns in text. In Python, we have the re module. The applications for regular expressions are wide-spread, but they are fairly complex, <b>so when contemplating using a regex for a certain task, think about alternatives, and come to regexes as a last resort.</b>
</p>

<p>An example regex is <b>r"^(From|To|Cc).*?python-list@python.org"</b> Now for an explanation: the caret ^ matches text at the beginning of a line. The following group, the part with (From|To|Cc) means that the line has to start with one of the words that are separated by the pipe |. That is called the OR operator, and the regex will match if the line starts with any of the words in the group. The .*? means to un-greedily match any number of characters, except the newline \n character. The un-greedy part means to match as few repetitions as possible. The . character means any non-newline character, the * means to repeat 0 or more times, and the ? character makes it un-greedy.
</p>

<p>So, the following lines would be matched by that regex: From: <b>python-list@python.org To: !asp]<,. python-list@python.org</b></p>

<a href = "https://docs.python.org/3/library/re.html#regular-expression-syntax%22RE%20syntax">Click for complete reference of the <b>re</b> syntax</a>

<a href = "http://www.ex-parrot.com/pdw/Mail-RFC822-Address.html">As an example of a "proper" email-matching regex, click here</a>

```js
# Exercise: make a regular expression that will match an email
import re
def test_email(your_pattern):
    pattern = re.compile(your_pattern)
    emails = ["john@example.com", "python-list@python.org", "wha.t.`1an?ug{}ly@email.com"]
    for email in emails:
        if not re.match(pattern, email):
            print("You failed to match %s" % (email))
        elif not your_pattern:
            print("Forgot to enter a pattern!")
        else:
            print("Pass")
# Your pattern here!
pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
test_email(pattern)

//Outputs
Pass
Pass
Pass
```


## Exception Handling
<p>When programming, errors happen. It's just a fact of life. Perhaps the user gave bad input. Maybe a network resource was unavailable. Maybe the program ran out of memory. Or the programmer may have even made a mistake!</p>

<p>But sometimes you don't want exceptions to completely stop the program. You might want to do something special when an exception is raised. <b>This is done in a try/except block.</b></p>

Example:

```js
def do_stuff_with_number(n):
        print(n)

the_list = (1, 2, 3, 4, 5)

for i in range(20):
    try:
        do_stuff_with_number(the_list[i])
    except IndexError: # Raised when accessing a non-existing index of a list
        do_stuff_with_number(0)

//outputs
1
2
3
4
5
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
```

## Sets

<p>Sets are lists with no duplicate entries. Let's say you want to collect a list of words used in a paragraph:</p>

```js

print(set("my name is Eric and Eric is my name".split()))
//outputs
{'Eric', 'is', 'name', 'and', 'my'}

a = set(["Jake", "John", "Eric"])
print(a)
//outputs
{'Eric', 'John', 'Jake'}

b = set(["John", "Jill"])
print(b)
//outputs
{'John', 'Jill'}

```

<h3>The different methods are: </h3>
<ul>
<li>intersection()</li>
<li>symmetric_difference()</li>
<li>difference()</li>
<li>union()</li>
</ul>

```js

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.intersection(b))
print(b.intersection(a))

//outputs 
{'John'}
{'John'}

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

//outputs
{'Eric', 'Jake', 'Jill'}
{'Eric', 'Jill', 'Jake'}


a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.difference(b))
print(b.difference(a))

//Outputs
{'Eric', 'Jake'}
{'Jill'}

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.union(b))

//Outputs
{'Jill', 'Eric', 'John', 'Jake'}

```

## Serialization
<p>Data serialization is the concept of converting structured data into a format that allows it to be shared or stored in such a way that its original structure to be recovered. In some cases, the secondary intention of data serialization is to minimize the size of the serialized data which then minimizes disk space or bandwidth requirements.</p>

### Pickle
<p>The native data serialization module for Python is called <a href='https://docs.python.org/2/library/pickle.html'>Pickle<a/>.</p>

Example:

```js
import pickle

//Here's an example dict
grades = { 'Alice': 89, 'Bob': 72, 'Charles': 87 }

//Use dumps to convert the object to a serialized string
serial_grades = pickle.dumps( grades )
print(serial_grades);

//Use loads to de-serialize an object
received_grades = pickle.loads( serial_grades )
print(received_grades)

//Outputs
b'\x80\x03}q\x00(X\x07\x00\x00\x00Charlesq\x01KWX\x03\x00\x00\x00Bobq\x02KHX\x05\x00\x00\x00Aliceq\x03KYu.'
{'Charles': 87, 'Bob': 72, 'Alice': 89}

```

## Partial functions
<p>You can create partial functions in python by using the partial function from the <b>functools</b> library.</p>
<p>Partial functions allow one to derive a function with x parameters to a function with fewer parameters and fixed values set for the more limited function.</p>

Example:

```js
from functools import partial

def multiply(x,y):
        return x * y

# create a new function that multiplies by 2
dbl = partial(multiply,2)
print(dbl(4))

//outputs
8

<b>Note:</b>
<p>An important note: the default values will start replacing variables from the left. The 2 will replace x. y will equal 4 when dbl(4) is called. It does not make a difference in this example, but it does in the example below.</p>

```
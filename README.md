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



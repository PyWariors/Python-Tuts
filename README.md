#What is Python
It is a programming language as well as as the Python interpreter which reads the code and performs the instructions. It was created by [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum)
Origin of python name is from the British comedy Monty Python. 

#Where to Download ?
It can be downloaded from [https://www.python.org/downloads/] (https://www.python.org/downloads/)

#Warning
The support for 2x version is going to stop so make sure you download the latest or atleast a 3x version.

#Datatypes
Data type is a category for values. Each of the assigned value belongs to a certain datatype.
The most common type of data types are integer, floating-point and string. Lists, dictionaries and tuples will be explained later in detail.
##Integer
Integer or Int indicates a value which is whole.

```Python
i1=0
i2=-1
i3=2
print(i1,i2,i3)
```
##Floating-Point
Floating-point are numbers with decimal point. 

```Python
f1=0.0
f2=-1.27
f3=3.3
print(f1,f2,f3)
```

##String
String is text assigned to a variable. Always surround your string with single quotes (''), it's possible to have a string '' which is called a blank string.

```python
s1='Hello'
s2='World !'
```

##String Concatenation & Replication
+ is the concatenation operator, which is used for joining the strings.
* becomes the string replication operatorused when used on one string and one integer value. e.g. 'Hello'*4
```python
s1='Hello'
s2='World !'

#Concatenation
print(s1+' '+s2)

#Replication
print(s1*4)
```

##Lists, Dictionaries & Tuples will be covered later in the tutorial

# Functions in python.
## What are Functions?
Functions are a convenient way to divide your code into useful blocks, allowing us to order our code, make it more readable, debuggable, reuse it and save some time. Also functions are a key way to define interfaces so programmers can share their code.
How do you write functions in Python?
As we have seen on previous tutorials, Python makes use of blocks. The function is defined followed by an indented block. A block is a area of code of written in the format of:
block_head: 
    1st block line 
    2nd block line 
    ...
## sample function definition
def my_function():
     print "Hello From My Function!"
## How do you call functions in Python?
Simply write the function's name followed by (), placing any required arguments within the brackets. For example, lets call the functions written above (in the previous example):
def my_function():
     print "Hello From My Function!"
my_function() Copy

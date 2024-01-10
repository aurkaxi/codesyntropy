# input output
- To print something: `print()`
```py
print("x")
```
Output: `x`

- To take input: `input()`
```py
x = input("Input the value of x: ")
print(x)
```
```
Input the value of x: 5
5
```
Here terminal will prompt to pass a data. which will be assigned to variable `x`. Variables are explained in the following sections.

- To Comment: use `#`. Comments are piece of code that will be ignored (will not execute or run)
```py
#4
x = 5#6
print(x)
```
Output: `5`

# Variables & Data Types
Variables are containers for storing data values. To assing a value to a variable named `x`:
```py
x = value
```
What can be a value? Go to [datatypes](#data-types) for better understanding. 

> Variables are Case-sensitive:
> ```py
> a = 4
> A = "Sally"
> #A will not overwrite a
> ```

# Data Types
To get the type of a variable we can use `type()` function.
```py
x = 1
print(type())
```
Output: `<class 'int'>`
Here `int` is the datatype.

To cast a variable to specific data we have built-in functions with the same name of the datatype. Casting means: *to specify the datatype explicitely*
```py
x = float(1)
print(type(x))
```
Output: `<class 'float'>`
As you can see now we explicitely specified x to be a float.

## Numeric Types
### int
Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
```py
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
```
```
<class 'int'>
<class 'int'>
<class 'int'>
```
### float
Float, or "floating point number" is a number, positive or negative, containing one or more decimals.
```py
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
```
```
<class 'float'>
<class 'float'>
<class 'float'>
```
Float can also be scientific numbers with an "e" to indicate the power of 10.
```py
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
```
```
<class 'float'>
<class 'float'>
<class 'float'>
```
### Complex
Complex numbers are written with a "j" as the imaginary part
```py
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
```
```
<class 'complex'>
<class 'complex'>
<class 'complex'>
```

## Text Type or String (str)
Either in double or single quotes. double quote can include single quote. and vice-versa.
```py
x = "Hello"
y = 'Hello'
print(x) # prints: Hello
print(y) # prints: Hello
print(x==y) # True
```
### Multiline Strings
Use 3 quotes to assign multiline string.
```py
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
```
You can also use escape codes (`\n`). But more on that later.

> Strings are arrays of characters. You can perform same actions on both (loop, in, indexing via list[index]). Check list-methods.md note.


## Sequence Types
To get an item of a sequence via it's index:
```py
sequence[0] # first item
sequence.get(1) # second item
```
Index starts from `0`. For reverse order it's from `-1`
To get the length: 
```py
len(sequence) # returns a integer
```
To change a value:
`sequence[index] = "new value"`

To slice a sequence:
`sequence[start : end : step]`
```py
x = [1,2,3,4,5,6]
print(x[0:5:2]) # [1, 3, 5]
```
### list
Lists are used to store multiple items in a single variable.
```py
thislist = ["apple", "banana", "cherry"]
print(thislist)
```
To construct/cast a list: `list()`

- Ordered
- Changable
- Allow Duplicates

### tuple
A tuple is a collection which is ordered and unchangeable.
```py
thistuple = ("apple", "banana", "cherry")
```
To construct/cast a tupele: `tuple()`

- Ordered
- Unchangable
- Allow Duplicates

### range
A sequence you can construct via passing start and end value. end value is excluded.
```py
x = range(1, 10) # 1,2,3,4,5,6,7,8,9
```

## Mapping Type (dict)
Dictionaries are used to store data values in key:value pairs.
```py
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
```
All the keys must be same type, Value can be multiple types.

To access, pass the key: `thisdict["brand"]`. It can be modified in the same way as sequences.
`hisdict["brand"] = "Toyota"`

- Ordered
- Changable
- No Duplicates

Construct/cast: `dict()`

`dict` shares some built-in functions and methods as sequences.


## Boolean Type (bool)
Booleans represent one of two values: True or False.
```py
print(10 > 9)
print(10 == 9)
print(10 < 9)
```
```
True
False
False
```
Everything is True unless it's empty or explicitely False.

# Basic Operators:
- Arithmetic
    - `+` : Addition
    - `-` : Substraction
    - `*` : Multiplication
    - `/` : Division
    - `%` : Modulus
    - `**`: Exponentiation
    - `//`: Floor division
- We can combine operators with `=` to assing. e.g. instead of `x = x + 1` we can write `x += 1`. works for all arithmetic operators.
- Comparison
    - `==` : Equal
    - `!=` : Not Equal
    - `>`  : Greater than
    - `<`  : Less than
    - `>=` : Greater than or equal to
    - `<=` : Less than or equal to
- `and`: True if both side true
- `or`: True if either side is true. if both false then false
- `not`: reverse True-False
- `is`: if both side is same
- `is not`: if both side is not same
- `in`: if element is in a iterator
- `not in`: if elemetn is not in a iterator


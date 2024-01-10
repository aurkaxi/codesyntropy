# List Manipulation
#### To add:
- `append(x)`: adds `x` to the end of the list
- `extend(I)`: adds the elements of `I` to the end of the list
- `insert(pos, item)`: adds `item` to the `pos`-th position of the list
#### Change Items:
`list[pos] = new`
#### To Remove
- `del list[pos]`: to remove via list slicing. pos can be `range` type. `del list[1:10:2]`
- `remove(x)`: to remove a specific item
- `pop(pos)`: to remove `pos`-th item
- `clear()`: to clear the whoel list
#### Sort:
`sort(reverse: bool, key: function)`: to sort a value. `key` is a function that will take each element and return an integer to help the sorting system. 
imagine having a list of names. and for each name our functions takes the string and output a random number.
`sort` will remember which item got what value, and sort them according to the values passed by key.

for all methods: see **list-methods.md**

# Tuple Operations
#### Create
`x = (1,2,'a', "b")`

to create with one item, a `,` must be passed. `x = (1,)`

#### access:
- `x[i]`; where i < |len(x)|
- slices are also available: `x[i:j:k]`
- to check existence: `i in x`

#### modify
tuples are immutable. but you can convert it to list, modify the list and then convert back to tuple
```py
x : tuple = (1,2,3)
x : list = list(x)
x : tuple = tuple(x)
```
#### UNPACK
```py
x = (1,2,3,4)
(a,b,*c) = x

print(a) # 1
print(b) # 2
print(c) # [3,4]
```
using asteric will make the rest of the items a list of that variable. other wise each variable will get an item respectedly

#### iteration:
`for _ in tuple(_)`

#### Misc
```py
x = (1,2,3)
y = (4,5,6)

_sum = x+y # (1,2,3,4,5,6)
mul = x * 2 # (1,2,3,1,2,3)
```

#### methods:
- `index()`: get index of a specific item
- `count()`: total number of items

# String manipulation:
Method | Description 
---|---
capitalize() | Converts the first character to upper case 
casefold() | Converts string into lower case 
center() | Returns a centered string 
count() | Returns the number of times a specified value occurs in a string 
encode() | Returns an encoded version of the string 
endswith() | Returns true if the string ends with the specified value 
expandtabs() | Sets the tab size of the string 
find() | Searches the string for a specified value and returns the position of where it was found 
format() | Formats specified values in a string 
format_map() | Formats specified values in a string 
index() | Searches the string for a specified value and returns the position of where it was found 
isalnum() | Returns True if all characters in the string are alphanumeric 
isalpha() | Returns True if all characters in the string are in the alphabet 
isascii() | Returns True if all characters in the string are ascii characters 
isdecimal() | Returns True if all characters in the string are decimals 
isdigit() | Returns True if all characters in the string are digits 
isidentifier() | Returns True if the string is an identifier 
islower() | Returns True if all characters in the string are lower case 
isnumeric() | Returns True if all characters in the string are numeric 
isprintable() | Returns True if all characters in the string are printable 
isspace() | Returns True if all characters in the string are whitespaces 
istitle() | Returns True if the string follows the rules of a title 
isupper() | Returns True if all characters in the string are upper case 
join() | Converts the elements of an iterable into a string 
ljust() | Returns a left justified version of the string 
lower() | Converts a string into lower case 
lstrip() | Returns a left trim version of the string 
maketrans() | Returns a translation table to be used in translations 
partition() | Returns a tuple where the string is parted into three parts 
replace() | Returns a string where a specified value is replaced with a specified value 
rfind() | Searches the string for a specified value and returns the last position of where it was found 
rindex() | Searches the string for a specified value and returns the last position of where it was found 
rjust() | Returns a right justified version of the string 
rpartition() | Returns a tuple where the string is parted into three parts 
rsplit() | Splits the string at the specified separator, and returns a list 
rstrip() | Returns a right trim version of the string 
split() | Splits the string at the specified separator, and returns a list 
splitlines() | Splits the string at line breaks and returns a list 
startswith() | Returns true if the string starts with the specified value 
strip() | Returns a trimmed version of the string 
swapcase() | Swaps cases, lower case becomes upper case and vice versa 
title() | Converts the first character of each word to upper case 
translate() | Returns a translated string 
upper() | Converts a string into upper case 
zfill() | Fills the string with a specified number of 0 values at the beginning 

# Looping Constructs
### For loop:
make an for-each loop. it iterates over each element and perform a task
```py
x = [1,2,3]
for i in x:
    print(x)
```
```
1
2
3
```
### while loop
loops a code block until condition is false
```py
count = 0
while count < 3:
    print(count)
    count += 1
```
```
0
1
2
```
### loop controllers:
- break: breaks current loop.
- continue: skips the rest of the code block of the loop
```py
for i in [1,2,3]:
    if i == 2:
        continue
    print(i)
```
```
1
3
```
- pass: does nothing :)

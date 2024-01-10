# List Methods

## append()
Adds an element at the end of the list
### Syntax:
```
list.append(elmnt)
```
Parameter | Description
-|-
elmnt | **Required**. An element of any type (string, number, object etc.)
### Example
```py
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)
```
Output: `['apple', 'banana', 'cherry', 'orange']`

## clear()
Removes all the elments from the list
### Syntax:
```
list.clear()
```
Parameter | Description
-|-
No parameter
### Example
```py
fruits = ['apple', 'banana', 'cherry', 'orange']

fruits.clear()
print(fruits)
```
Output: `[]`

## copy()
Returns a copy of the list
### Syntax:
```
list.copy()
```
Parameter | Description
-|-
No parameter
### Example
```py
fruits = ["apple", "banana", "cherry"]

x = fruits.copy()

print(x)
```
Output: `['apple', 'banana', 'cherry']`

## count()
Returns the number of elements with the specified value
### Syntax:
```
list.count(value)
```
Parameter | Description
-|-
value | **Required**. Any type (string, number, list, tuple, etc.). The value to search for.
### Example
```py
fruits = ["apple", "banana", "cherry"]

x = fruits.count("cherry")

print(x)
```
Output: `1`

## extend()
Add the elements of a list (or any iterable), to the end of the current list
### Syntax:
```
list.extend(iterable)
```
Parameter | Description
-|-
iterable | **Required**. Any iterable (list, set, tuple, etc.)
### Example
```py
fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)

print(fruits)
```
Output: `['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']`

## index()
Returns the index of the first element with the specified value
### Syntax:
```
list.index(elmnt)
```
Parameter | Description
-|-
elmnt | **Required**. Any type (string, number, list, etc.). The element to search for
### Example
```py
fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")

print(x)
```
Output: `2`

## insert()
Adds an element at the specified position
### Syntax:
```
list.insert(pos, elmnt)
```
Parameter | Description
-|-
pos | **Required**. A number specifying in which position to insert the value
elmnt | **Required**. An element of any type (string, number, object etc.)
### Example
```py
fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")

print(fruits)
```
Output: `['apple', 'orange', 'banana', 'cherry']`

## pop()
Removes the element at the specified position
### Syntax:
```
list.pop(pos)
```
Parameter | Description
-|-
pos | **Optional**. A number specifying the position of the element you want to remove, default value is -1, which returns the last item
### Example
```py
fruits = ['apple', 'banana', 'cherry']

fruits.pop(1)

print(fruits)
```
Output: `['apple', 'cherry']`

## remove()
Removes the first item with the specified value
### Syntax:
```
list.remove(elmnt)
```
Parameter | Description
-|-
elmnt | **Required**. Any type (string, number, list etc.) The element you want to remove
### Example
```py
fruits = ['apple', 'banana', 'cherry']

fruits.remove("banana")

print(fruits)
```
Output: `['apple', 'cherry']`

## reverse()
Reverses the order of the list
### Syntax:
```
list.reverse()
```
Parameter | Description
-|-
No parameter
### Example
```py
fruits = ['apple', 'banana', 'cherry']

fruits.reverse()

print(fruits)
```
Output: `['cherry', 'banana', 'apple']`

## sort()
Sorts the list
### Syntax:
```
list.sort(reverse=True|False, key=myFunc)
```
Parameter | Description
-|-
reverse | **Optional**. reverse=True will sort the list descending. Default is reverse=False
key | **Optional**. A function to specify the sorting criteria(s)
### Example
```py
cars = [2, 1, 3]

cars.sort()

print(cars)
```
Output: `[1, 2, 3]`

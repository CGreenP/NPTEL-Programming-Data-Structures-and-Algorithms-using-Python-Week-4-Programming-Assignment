# NPTEL-Programming-Data-Structures-and-Algorithms-using-Python-Week-4-Programming-Assignment
NPTEL Programming, Data Structures and Algorithms using Python Week 4 Programming Assignment

# Week 4 Programming Assignment
1. We have a list of annual rainfall recordings of cities. Each element in the list is of the form (c,r) where c is the city and r is the annual rainfall for a particular year. The list may have multiple entries for the same city, corresponding to rainfall recordings in different years.

Write a Python function rainaverage(l) that takes as input a list of rainfall recordings and computes the avarage rainfall for each city. The output should be a list of pairs (c,ar) where c is the city and ar is the average rainfall for this city among the recordings in the input list. Note that ar should be of type float. The output should be sorted in dictionary order with respect to the city name.

Here are some examples to show how rainaverage(l) should work.
```python
>>> rainaverage([(1,2),(1,3),(2,3),(1,1),(3,8)])
[(1, 2.0), (2, 3.0), (3, 8.0)]

>>> rainaverage([('Bombay',848),('Madras',103),('Bombay',923),('Bangalore',201),('Madras',128)])
[('Bangalore', 201.0), ('Bombay', 885.5), ('Madras', 115.5)]
```

2. A list in Python can contain nested lists. The degree of nesting need not be uniform. For instance [1,2,[3,4,[5,6]]] is a valid Python list. Write a Python function flatten(l) that takes a nonempty list of lists and returns a simple list of all the elements in the nested lists, flattened out. You can make use of the following function that returns True if its input is of type list.
```python
def listtype(l):
  return(type(l) == type([]))
```
Here are some examples to show how flatten(l) should work.
```python
>>> flatten([1,2,[3],[4,[5,6]]])
[1, 2, 3, 4, 5, 6]

>>> flatten([1,2,3,(4,5,6)])
[1, 2, 3, (4, 5, 6)]
```

# Sample Test Cases
|              | Input                                                                                                                                          | Output                                                                                  |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| Test Case 1  | rainaverage([(1,2),(1,3),(2,3),(1,1),(3,8)])                                                                                                   | [(1, 2.0), (2, 3.0), (3, 8.0)]                                                          |
| Test Case 2  | rainaverage([('Bombay',848),('Madras',103),('Bombay',923),('Bangalore',201),('Madras',128)])                                                   | [('Bangalore', 201.0), ('Bombay', 885.5), ('Madras', 115.5)]                            |
| Test Case 3  | flatten([1,2,[3],[4,[5,6]]])                                                                                                                   | [1, 2, 3, 4, 5, 6]                                                                      |
| Test Case 4  | flatten([1,2,3,(4,5,6)])                                                                                                                       | [1, 2, 3, (4, 5, 6)]                                                                    |
| Test Case 5  | flatten(["hello",True,3])                                                                                                                      | ['hello', True, 3]                                                                      |
| Test Case 6  | flatten([1,2,[3,["hello",True]],[4,[5,6]]])                                                                                                    | [1, 2, 3, 'hello', True, 4, 5, 6]                                                       |
| Test Case 7  | rainaverage([(1,2),(1,3),(2,3),(1,1),(3,8)])                                                                                                   | [(1, 2.0), (2, 3.0), (3, 8.0)]                                                          |
| Test Case 8  | rainaverage([(1,0),(1,3),(2,3),(1,1),(3,8),(3,-8)])                                                                                            | [(1, 1.3333333333333333), (2, 3.0), (3, 0.0)]                                           |
| Test Case 9  | rainaverage([('Bombay',848),('Madras',103),('Bombay',923),('Bangalore',201),('Madras',128)])                                                   | [('Bangalore', 201.0), ('Bombay', 885.5), ('Madras', 115.5)]                            |
| Test Case 10 | rainaverage([('Bombay',1848),('Madras',103),('Bombay',923),('Bangalore',201),('Madras',128),('Madras',103),('Bombay',948),('Bangalore',323)])  | [('Bangalore', 262.0), ('Bombay', 1239.6666666666667), ('Madras', 111.33333333333333)]  |
| Test Case 11 | rainaverage([('Bombay',1848),('Bombay',923),('Bombay',201),('Bombay',128),('Bombay',103),('Bombay',948),('Bangalore',323)])                    | [('Bangalore', 323.0), ('Bombay', 691.8333333333334)]                                   |
| Test Case 12 | flatten([1,2,3,(4,5,6)])                                                                                                                       | [1, 2, 3, (4, 5, 6)]                                                                    |
| Test Case 13 | flatten(["hello",True,3])                                                                                                                      | ['hello', True, 3]                                                                      |
| Test Case 14 | flatten([1,2,[3,["hello",True]],[4,[5,6]]])                                                                                                    | [1, 2, 3, 'hello', True, 4, 5, 6]                                                       |
| Test Case 15 | flatten([[1,2,[3],[4,[5,6]]]])                                                                                                                 | [1, 2, 3, 4, 5, 6]                                                                      |
| Test Case 16 | flatten([[[]]])                                                                                                                                | []                                                                                      |

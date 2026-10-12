# Lab 5: C++ Standard Template Library

**Attention: no code samples in this lab, you need to create everything by yourself****.**

**Exercise 1:** This exercise is designed to get you familiar with [the numeric\_limits class](https://en.cppreference.com/w/cpp/types/numeric_limits) in STL. (**30 minutes coding)**

1. Create a C++ program to print out the max and min value of the following primitive types: int, unsigned int, long, double and float. What do you find from this program?
2. Try other methods on different primitive types per your interest.

```
Take Away for Exercise 1:   
    All data types have limits, there are max/min values.   
    If you continuously increase (or decrease) an integer/float/double   
    you will get an overflow/underflow eventually. AND, for float/double,   
    there are numbers that the computer simply cannot represent!
```

**Exercise 2:** This exercise is designed to get you familiar with [the vector class in STL](https://en.cppreference.com/w/cpp/container/vector). (**60 minutes** **coding**)

1. Create an integer vector of size 5
2. Initialize each element in the vector with a random even number
3. Print the value of each element in the vector, using iterator if you can
4. Add five random odd numbers to the end of the vector one by one
5. Sort the vector in an ascending order, using a proper sorting algorithm in STL
6. Print the value of each element in the vector
7. **Optional**
   1. Create an integer vector with the same size as the vector obtained in step 5, but the value of each element is doubled.
   2. Create another "vector of integer vector"
   3. Add the vectors created in steps 5 and 7.1 into the newly created empty "vector of vector" in step 7.2
   4. Print the value of each element in this newly created "vector of vector"

```
Take Away for Exercise 2:   
    Well, this (and the rest of the utilities) is a rather convenient   
    utility to know, and familiarizing with how to use this is important.   
    [This is true for the the rest of this exercise]
```

**Exercise 3:** This exercise is designed to get you familiar with [the list class in STL](https://en.cppreference.com/w/cpp/container/list). (**45 minutes** **coding**)

1. Create an empty integer list
2. Add 1, 3, 5, 7, 9 to the end of the list in sequence
3. Add 2, 4, 6, 8, 10 to the beginning of the list in sequence; at the end of this step, you should have the following elements in the list in sequence: 10, 8, 6, 4, 2, 1, 3, 5, 7, 9
4. Print out the first and last element in the list
5. Remove element “3” from the list
6. Sort the list using the sorting method in List Class, but not the one in <algorithm>
7. Print out the value of each element in the list
8. Remove all “odd” numbers in the list
9. Print out the value of each element in the list

**Exercise 4:** This exercise is designed to get you familiar with [the map class in STL](https://en.cppreference.com/w/cpp/container/map). (**45 minutes** **coding**)

1. Create an empty map, whose “key” is string type and “value” is integer type
2. Add five different key-value pairs into the map
3. Print out each key-value pairs in the map
4. Insert a pair whose key exists in the map, print out the return value of the insert operation
5. Insert a pair whose key does not exist in the map, print out the return value of the insert operation
6. Please try to use both operator[] and insert method in the following two steps
   1. Try to update a pair’s value given a key that does not exist in the map. Any runtime errors?
   2. Try to update a pair’s value given an existing key in the map.

**What to submit**

1. Please create separate files for each of the exercises and submit the four cpp files (no need for separate folders).
2. Zip everything together and submit that *single* zip file.

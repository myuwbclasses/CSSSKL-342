# Lab 2: C++ memory management: pointers, arrays, new and delete operators

**Attention:**All files used in this lab can be accessed by following [**this link**](https://github.com/myuwbclasses/CSSSKL-342/) (source code files are in **All-Labs/Lab2**).

This lab is all about pointers, references, memory allocation and deallocation, etc. You will also think a bit about good, secure programming practice relevant to dynamic allocation and related issues (among many other things).

**Exercise 1:** Use [Pointer1.cpp](https://github.com/myuwbclasses/CSSSKL-342/blob/main/All-Labs/Lab2/1.BasicPointers/Pointer1.cpp "Pointer1.cpp") to explore basic pointer concepts (**30 minutes in coding**).

1. **Question**: Consider the call to display2() in main(), what's wrong with the call?
2. **Coding (finish in 5min)**: Fix the problem you saw in the first question ***without***changing display2().
   1. **Take away:**notice the difference of "&" and "\*" and how to pass parameters
3. **Coding (finish in 15min)**:
   1. Create a new function named "display3," which looks like "void display3(int m, int\* p)"
   2. In "display3," assign new values to "m" and "\*p"
   3. Print out the values of "b" and "a" in in main()
   4. Call "display3" by passing in "b" and "aPtr"
   5. Print out the values of "b" and "a" in in main() again, after calling display3() in the previous step
   6. **Take away:** parameter values can be changed "following" (de-referencing) pointers. This is one way to return results from a function (by defining parameter as references or pointers).
4. **Coding (finish in 5min)**
   1. Please update function "display3"
      1. In "display3," after the code to update the value of "\*p," print out "\*p," "p" and "&p."
      2. **Take away:**pay attention to the values printed out:
         - dereferencing the pointer,
         - the pointer, and
         - address of the pointer.
5. **Coding (finish in 5min)**: Back in main(), at the bottom, assign a new value to the storage that "aPtr" points to (hint: use the dereference operator) and output both "\*aPtr" and "a" - what has happened?

```
Take away for Exercise 1  
      Intro to pointer syntax  
      Differences between "&" and "*"  
      How and when to use "&" vs "*"
```

**Exercise 2**: Function pointer: The code in [Pointer2.cpp](https://github.com/myuwbclasses/CSSSKL-342/blob/main/All-Labs/Lab2/2.FunctionPointers/Pointer2.cpp "Pointer2.cpp") is sort of like a "stupid pointer tricks" example. It also introduces the typedef construct. Go over this code to make sure you understand what's going on in it. **No Coding!**

```
Take away for Exercise 2  
      typedef: allows "aliasing" of identifiers to new data type  
      Define pointers to functions and passing functions as parameters 
```

**Exercise 3:** Dynamic memory allocation: New and Delete in C++. We'll do some demos by updating [Pointer3.cpp](https://github.com/myuwbclasses/CSSSKL-342/blob/main/All-Labs/Lab2/3.NewAndDelete/Pointer3.cpp "Pointer3.cpp") to enhance the understanding of memory management in C++.

```
Now, on the Linux machines, try running  
     valgrind --leak-check=full <Your Executable>  
What do you see? Why?   
Now, comment out one of the "delete" and try again.
```

```
Take away for Exercise 3  
      new to allocate, delete to remove  
      Array allocation new [], must be paired with delete [].
```

**We'll do interactive coding in this exercise.**

**Exercise 4:** We will use the code in [ArrayDemo.cpp](https://github.com/myuwbclasses/CSSSKL-342/blob/main/All-Labs/Lab2/4.Arrays/ArrayDemo.cpp "ArrayDemo.cpp") to explore arrays and the relationships between arrays and pointers. First of all, make sure you understand the purpose and syntax of the forward declarations at the beginning of the file. Then do the following (**90 minutes in coding**):

1. **Question**: How are the declarations of the arrays set and set2 different than how they would be declared in Java?
2. **Coding (finish in 30min)**:

1. Add a function called linearSearch()
2. This function takes as input an array, its size, and a target integer to find
3. It should return -1 if the item is not found, or its (non-negative) index if found
4. Test it on one of the provided arrays

3. **Coding (finish in 10min)**: Rewrite swap() so that it takes two pointers *only* and swaps the values at those two memory locations. To avoid collision with the std::swap() function, please name and call your swap function MySwap();
4. **Coding (finish in 30min)**: Rewrite bubble() so that it uses a pointer and pointer arithmetic, rather than an array with array indexing. Which version of the code do you think is better? Why?
5. **Coding (finish in 20min)**:

1. Change all int array parameter declarations in the function definitions using int[] to declarations using int\* pointers.
2. Remember to change the function prototypes, too.
3. In main(), declare arrays set and set2 dynamically using "new".
4. Also in main(), you now need to delete this memory manually (it's an array, so use delete []).
5. Set all pointer variables in main() to null after deleting storage (why?).

```
Take away for Exercise 4  
      Understand array indexing and pointer arithmetic relationship.     
```

### What to submit

Please submit one zip file of the following:

- Updated versions of Pointer1.cpp and ArrayDemo.cpp.
- .h files that you have created, if any.
- A .txt file describing your understanding of the best practices to use dynamic memory allocation in C++.
- Zip everything together and submit that *single* zip file.

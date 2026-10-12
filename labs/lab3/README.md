# Lab 3: Class, constructors, inheritance and lifespan

**Attention:**All files used in this lab can be accessed by following [**this link**](https://github.com/myuwbclasses/CSSSKL-342) (source code files are in **All-Labs/Lab3**).

**Exercise1:** The first part of today's lab is to learn Class in C++ and investigate how inheritance affects which methods get called and in what order constructors and destructors are called. Please look at the **1.Inheritance** folder in your download, compile and run (source code files A.cpp, A.h, B.cpp, B.h, C.cpp, C.h, and InheritanceTest.cpp.)

**Question**

1. What do you observe?
2. How are the constructors and destructors called? in which order?
   - **Take away:**construction is done from the super class (A first) to derived classes (then B, and C later). Destruction occurred in the reversed order, from derived class (C first) and then the super classes (then B, then A).

**Coding (finish in 20min)**

1. Add an "int" type private data member named "testData1" in A, and update A's "parameterized constructor" to initialize this newly added data member **using "initialization list."** You don't need to update other constructors. You may complete other constructors in Step 4.
   - **Take away:** how to initialize an instance variable in the initialization list (the prefer way).
2. Add another "int" type private data member named "testData2" in A, and update A's "default constructor" to initialize this newly added data member **without** using the initialization list. You don't need to update other constructors. You may complete other constructors in Step 4.
   - **Take away:**alternate ways to initialize, all of the ways are valid, but use initializer when possible.
3. Now you should have two data members added to A, can you tell the difference between using the "initialization list" or not?
   - **Take away:**alternate ways to initialize, all of the ways are valid, but use initializer when possible.
4. Please complete both "default constructor" and "parameterized constructor" to properly initialize all data members in A.
   - **Take away:**All ways are valid, but you need to make sure to initialize \_ALL\_ instance variables. Notice the ones created on the stack (local) has garbage in them!
5. Add an "int" type private data member named "testDataB" in class B and a "double" type private data member named "testDataC" in class C. Update constructors of B and C to make sure that the constructors in B and C (which should initialize their new members to some reasonable values) use the correct superclass constructors to **initialize every data member properly**.

```
Take away for Exercise 1  
    Class constructor and destructors  
    Calling sequence of the constructors and destructors  
    Default vs constructors with parameters (initializers)
```

**Exercise2:** Example code to evaluate variable scope, lifespan, and lvalues; please look at the **2.LifeSpan**folder in your download, compile and run (source code files: ScopeEtc.cpp, SuperInt.cpp, and SuperInt.h.)

**Question**

1. Try putting a SuperInt on the right hand side of an assignment statement using theValue(). Does it work? Why?
   - **Take away:**nothing too interesting, we can return the value of an instance variable. But, in this case we are returning the ***reference***to the variable!
2. Try putting a SuperInt on the left hand side of an assignment statement using theValue(). Does it work? Why?
   - **Take away:**First, returning a **const**type means the function cannot be a l-value. Second, if the the return type is not of **const***,* then, if the receiver of this function is an integer reference, then, the receiver can change this instance variable! **Ask me if you don't understand what I mean.**

**Coding (finish in 20min)**

1. Update the member function theValue() of SuperInt class so that SuperInt can be put on the left hand side of an assignment statement using theValue(). That is, theValue() can be use for assignment, e.g., *theValue() = 4;* Note that in this case, theValue() is referred to as the *lvalue* since it appears on the left-hand-side of the assignment statement.
2. Create a new class "SuperSuperInt," which inherits the "SuperInt" class. Please declare and define this class in separate .h and .cpp files, and **DO NOT** update SuperInt.h and SuperInt.cpp directly. Please name your new files as "SuperSuperInt.cpp" and "SuperSuperInt.h."
3. Add one member function theValue() to SuperSuperInt.
4. Code the member function theValue() of SuperSuperInt to return the value of data member "myValue" in SuperInt. Please make sure the returned value of theValue() **CANNOT** be put on the left hand side of an assignment statement.

```
Take away for Exercise 2  
    Scope of variables and when do they get destructred  
    Function returning a reference as lvalue in statements  
    Practice with sub-classing and working with instances from the super class.
```

**Exercise3:** Now, let's play with a pair of classes: Square and SquareContainer (you may struggle with this one). The latter is a dynamically allocated array of the former that can resize itself if needed. Please look at the **3.Classes** folder in your download. The files in question are Square.cpp, Square.h, SquareContainer.cpp, SquareContainer.h and ClassTest.cpp. Please download, compile and run these files, and convince yourself that you understand what they do.

```
Take away for Exercise 3  
    Practice with sub-classing (in a non-trivial example).
```

**Question**

1. Is there a problem with the fact that SquareContainer.h defines two classes?

**Coding (finish in 60min) - just try to finish as many as you can**

1. Add an overloaded **assignment operator** to the Square class (*this is already done,* *included in the given code for your reference. So, there is nothing you need to do here*).
2. Add a **"<" operator** for Square objects, which returns "true" when a Square object's size is smaller than the compared one; false otherwise;
3. Does the Square class need an overloaded assignment operator? Why or why not? Answer this as a comment in the code.
4. Add an overloaded **assignment operator** to the **SquareContainer**class, using the copy() and clear() methods.
5. (**Optional**) Add a **stream output operator** to the **Square** class to print out the size of the square.
6. (**Optional**) Add a **stream output operator** to the **SquareContainer** class to print out the size of each square in  the container.
7. Update "ClassTest.cpp" to test your updated classes.

```
Further Take away for Exercise 3  
    Operator overload  
    Friend classes and operator overload  
    Start thinking about the future, need for copy constructor and assignment operator overload
```

### What to submit

1. For each exercises, please create separate folders for the files to be submitted.
2. Updated files including the drivers testing your code in appropriate folders.
3. Zip **all required files** together and submit that *single* zip file.

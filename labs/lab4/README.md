# Lab 4: Copy constructors, assignment operators, deep vs. shallow copy; templates and iterators

**Attention:** All files used in this lab can be accessed by following [this link](https://github.com/myuwbclasses/CSSSKL-342) (source code files are in **All-Labs/Lab4**).

**Exercise 1:** This exercise is designed to present a class that has both a copy constructor and an assignment operator and to illustrate the difference between deep and shallow copies. Please download and compile the code in **Lab4/Exercise1** (MyClass.h, MyClass.cpp, and CopyAssignTest.cpp). Then do the following (**3****0 minutes coding**):

1. **Question**: Look at the code; do you think that MyClass::operator=() is doing a deep or shallow copy?
   - ```
     Take Away: Know the difference between deep and shallow copy.
     ```
2. **Question & Coding**: Do you notice any warning posted by the compiler? Is there a memory leak issue? How can you fix it?
   - ```
     Take Away: How to eye-ball memory leak (constructor and destructor)
     ```
3. **Coding**: Is MyClass::setIp() implemented correctly? What exactly does it do?
   - ```
     Take Away: What to watch out for when assigning value to a pointer type.
     ```
4. **Coding**: Derive a new subclass of MyClass, name it "MySubClass" and define a private "int" type data member named "subClassData" in this new class. What do you need to do is to ensure that the correct copy constructor and assignment operators are called. Verify that your new class works correctly.
   - ```
     Take Away: When to and how to call super class constructor/methods
     ```

**Exercise 2:** Template functions and classes. Be sure to create all necessary driver file, .h file and .cpp files. (**60 minutes** **coding**)

1. **Coding**: Convert the given MySwap, MyBubbleSort, and printArray functions into template functions. Verify your work by sorting an array of int, float, and char.
   - ```
     Take Away: Practice working with template functions
     ```
2. **Coding**: Dynamically allocate an array of Square objects, using the Square Class provided in **Lab4/Exercise2** (Square.h, Square.cpp) (with overloaded "<<" and "<" operators implemented).
   - ```
     Take Away: Preparation for using your own template
     ```
3. **Coding**: Use the bubble sort function you created in step 1 to sort the array of Square objects and print out the sorted result.
   - ```
     Take Away: [for next 3 steps]: Your template is useful! You can sort more   
     than just numbers, you can sort anything under the Sun as long as they   
     know how to compare themselves.
     ```
4. **Interactive Coding**: Update your Square class to be a template class
5. **Coding**: Use the template bubble sort function you created in step 1 to sort the array of Square objects of a specific type of your choice.

**Exercise 3:** The next set of files have to do with iterators. Download and compile the code in **Lab4/Exercise3** (SquareContainer2.h, SquareContainer2.cpp, and IteratorTest.cpp) and consider the following activities (**30 minutes** **coding**):

1. **Question**: Look at the code in IteratorTest.cpp. What do you think it does? Compile the code (do you need to do anything "unusual" to get it to compile?) and run it. Does it do what you think it would?
   - ```
     Take Away: Reminder of how to template class compilation, understanding of code.
     ```
2. **Question**: Why do the iterator increment operators return an iterator? How do the two increment operators differ? Is the iterator they return allocated dynamically, auto, or something else?
   - ```
     Take Away: What does it mean to return a reference to self (in this case,   
     and, in general, remember, overloaded operators typically return self).
     ```
   - ```
     Take note that: pre-increment (++i) returns a reference to self, while post-increment (i++) makes   
     a copy of self, perform increment, and then returns the copy made before the increment.   
     Do you know why this is the case?
     ```
3. **Interactive Coding and Question**: Change SquareContainer::iterator::operator\*() so that it is a const method. What is this supposed to mean? When you try to compile and run the program, what happens? Does this appear to be consistent with the declaration of that operator as const? Why or why not? In your opinion, should that operator be declared const?
   - ```
     Take Away: Understanding of "const", when to use, and why to (or not to) use.
     ```

### What to submit

1. For each exercise, please create separate folders for the files to be submitted.
2. Updated or new .cpp and .h files for all coding exercises: Exercises 1.2, 1.3, 1.4, 2, and 3.3
3. Answers to the questions (anywhere there is a "?" even as part of coding question) in a text file.
4. Zip everything together and submit that *single* zip file.

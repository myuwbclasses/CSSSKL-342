# Lab 1: Toolchains, type conversion, references, file I/O issues

**Attention:** All files used in this lab can be accessed by following **[this link](https://github.com/myuwbclasses/CSSSKL-342)** (source code files are in **All-Labs/Lab1**).  
For this lab, we will be using the following code to experiment with the basics of the C++ toolchain, primitives, type conversion, pass by value, and pass by reference:

**Exercise 1 (60 minutes coding)**: Two programs to explore numeric primitives. The first one ([Primitive1.cpp](https://github.com/myuwbclasses/CSSSKL-342/blob/main/All-Labs/Lab1/1.PrimitiveDataTypes/Primitive1.cpp)) is simple as an example program for you. The second one ([Primitive2.cpp](https://github.com/myuwbclasses/CSSSKL-342/blob/main/All-Labs/Lab1/1.PrimitiveDataTypes/Primitive2.cpp)) examines some aspects of implicit and explicit type conversion of primitives, in particular between integer and floating point types. **TODO - write programs and functions:**  
1. Write a program named “**Primitive3.cpp**.”  
2. This program should have a main function.  
3. This program should have another function named “myRoudingFunction” and this function should round up or round down a float/double value to an integer value.  
4. Rules

- For positive values
  - Round up a value if its fraction part is greater or equal to “.5”
  - Round down a value if its fraction part is less than “.5”
- For negative values
  - Round down a value if its fraction part is greater or equal to “.5”
  - Round up a value if its fraction part is less than “.5”
- You are not allowed to use the “round” function provided by C++. But, you may compare the results obtained by your rounding function and the system provided “round” function.

5. Examples

- 0.4 should be rounded down to 0
- 0.6 should be rounded up to 1
- -0.4 should be rounded up to 0
- -0.6 should be rounded down to -1

6. In your program, you also need to write some test code to test your rounding function.

```
Take away for Exercise 1:  
    Create a simple C++ program from scratch  
    Work with primitive data types and their conversions  
    Remember to test any and all code you write  
    An important outcome is you have just written a C++ program from scratch
```

**Exercise 2 (no coding)**: We'll look at references and function calling using [ReferenceDemo.cpp](https://github.com/myuwbclasses/CSSSKL-342/blob/main/All-Labs/Lab1/2.References/ReferenceDemo.cpp). **TODO - answer all questions:**  
1. Please name your answer file as “**AnswersToReferenceDemo.txt**.”  
2. Download and try to compile the file. Why doesn't it compile? I'm not just looking for which line(s) have the problem, but rather what is wrong with those line(s).  
3. What is happening when onePlus() is called? In other words, what exactly does the function receive as an argument? Why isn't the value of the variable in main() altered?  
4. Conversely, consider the call to refIncrement(). What is the argument here and why is the value of the variable in main() changed?  
5. Finally, consider the code related to value(). First of all, make sure you understand what Pair is and what the declaration of pairs means.  
6. Next, consider a call to value(). What does the function receive as an argument? What is the meaning of const in this context?  
7. What does value() return? How can it be legal and what does it mean to apply the ++operator to its return value?

```
Take away for Exercise 2:  
  The significance of the "&" symbol (reference)   
  Passing parameters by value/reference  
  Function returning value/reference
```

**Exercise 3 (60 minutes coding)**: A brief file I/O demonstration program, and an input file for it. **TODO - answer all questions and write programs:**  
1.Please check the file operation example files: [FileDemo.cpp](https://github.com/myuwbclasses/CSSSKL-342/blob/main/All-Labs/Lab1/3.File-IO/FileDemo.cpp "FileDemo.cpp") and [rats.dat](https://github.com/myuwbclasses/CSSSKL-342/blob/main/All-Labs/Lab1/3.File-IO/rats.dat "rats.dat").  
2. Please name your answer file as “**AnswersToFileDemo.txt**.”  
3. Write a program named “**FileOperationPractice.cpp**.”  
4. This program should have a main function.  
5. In your program

- Read a text file that contains integers, print out each integer to "cout" and stop when you hit the end of file.
- Use this program to read and display the contents of three different text files ([textfile1.txt,](datafiles/textfile1.txt) [textfile2.txt](datafiles/textfile2.txt), [textfile3.txt](datafiles/textfile3.txt)) that contain the same numbers but use Unix/Linux, Windows/DOS, and Mac OS end of line characters.
- Do you encounter any problems? Does it matter what OS you're developing your code on? See if transferring these files from, say, a Windows machine to a Linux machine alters them by checking their ASCII contents using the Linux od -a command ([Examples](https://en.wikipedia.org/wiki/Od_(Unix)#)) to use the od command).

```
Take away for Exercise 3:  
  Simple file I/O  
  Appreciation for subtle text file storage differences
```

**What to submit in this lab**  
1. Primitive3.cpp  
2. FileOperationPractice.cpp  
3. AnswersToReferenceDemo.txt  
4. AnswersToFileDemo.txt  
5. Create a folder for all of the above files, zip the folder, and submit one single zip file.

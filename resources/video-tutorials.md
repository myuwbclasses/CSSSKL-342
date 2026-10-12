> Note: these screencasts are by Professor Stiber and are hosted on Canvas (not in this repo).

### Related To Lab 1: Toolchains

- C++ development process with Windows and Visual Studio

In this screencast, I out line the process of using Visual Studio to build a C++ application, including the project settings to get a basic console app, and then transfer the code to Linux for testing.

- C++ development process with Mac OS X and Xcode

In this screencast, I out line the process of using Xcode to build a C++ application, including the project settings to get a basic console app, and then transfer the code to Linux for testing.

### Related To Lab 2: Pointers & Memory

- Pointers

I spend some time here playing with code that uses and manipulates pointers. In particular, I look at the "address of" (&) operator, pointer declaration and dereferencing (\*) operator, and the relationship between arrays and pointers, including pointer arithmetic. I close with a brief example of passing a pointer to a function as an argument to another function.

- C++ memory management

Examining details of pointers, memory, allocation and de-allocation.

- Examining dynamic memory

Going through the details of a dynamically allocated link list.

### Related To Lab 3: Classes

- Classes

This is a screencast about classes, building applications from multiple classes, exceptions, testing your code, and dealing with compilation errors. Because I didn't want this to be an hour long, I don't do anything in excruciating detail, but I hope this conveys the idea. In particular, you'll note that I run into an issue with a forward declaration of a class. I didn't want to spend the time to look up the details and refresh my memory, so I just did away with the forward declaration. It turns out that that was the right thing to do anyway. If all you need to do is refer or point to a class, then you can declare a forward reference and put the details of the class declaration later. However, in this case, I want to use the class in a throw(), so I needed to have the entire class before that statement. Of course, this is all a result of me wanting to keep the number of files small for this screencast. In a real program, I would have had separate .cpp and .h files for the exception class, and including the .h file would have taken care of the declaration with no muss or fuss.

- Inheritance

This is an explanation of the mechanics of C++ inheritance, including the order that constructors are invoked, how to cause a superclass non-default constructor to be invoked, how to provide safe access and modification of superclass private data members, how to provide direct access to superclass data members (i.e., "protected"), using superclass pointers to point to subclass objects, and how to enable late binding by declaring methods "virtual", thus creating an entry for that method in the object's virtual method table (VMT). This last matter is shown using destructors.

More than all that, this screencast also illustrates how to play with code to learn how C++ works.

### Related To Lab 4: Shallow vs Deep Copy

- Copy Constructors and Assignment Operators (Shallow Version)

If all of the members of your class are either primitives or objects that have copy constructors, destructors, and assignment operators (operator=()) defined for them, then your life may be very easy: you may not need to define any of those for your class, instead relying on those defined for its members. In this screencast, we examine the action of those default actions for a simple class, then add dynamically allocated storage to show how this approach breaks down. I cannot emphasize this point enough: *if you allocate any dynamic storage in your class, then you must implement the full complement of functions that control construction, destruction, and copying (which includes assignment).*

- Copy Constructors and Assignment Operators (Deep Version)

This is a continuation of the preceding shallow copy/assign screencast, in which we implement the full complement of construction, destruction, and copying methods. Once we've done that, we see that we get copies of objects that also duplicate the deep, dynamically allocated structure of the original. This is the behavior that we want.

### Related To Lab 5: Libraries

- Iterators and Templates

This screencast covers some more advanced topics in C++ object oriented programming. The first topic is that of *iterators*. An iterator is like a pointer into an ADT that you can use outside the ADT to keep track of where you are while in the middle of some algorithm. Unlike a real pointer, which would expose the underlying ADT implementation, an iterator is an object that hides the implementation details necessary to identify a location in the ADT. In place of those details, it provides a standard looking pointer interface, with operations to increment the pointer (move to the next element in the ADT), in some cases decrement it (move to the previous element; not shown here), dereference it (to access or change an item stored in the ADT, and compare it to other iterators (typically, for equality or inequality). In other words, whatever the ADT really does internally, an iterator provides a substitute interface that makes it look like an array accessed via pointers.

Templates are used to define classes that can hold a variety of items. So, for example, instead of defining a "list of int" class, you can define a generic list class, and at variable declaration time (or object creation time, for dynamically allocated objects), you can specify what type of thing your list object holds (int, double, list of int, whatever). The trickiest thing here is remembering that you can't compile class template .cpp files separately. In our class, we will instead include the .cpp file from the .h file, and exclude the .cpp file from the build (omit it from the g++ command line).
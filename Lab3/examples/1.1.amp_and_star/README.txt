1.1.amp_and_star -- every row of the two & and * tables in the Lab 3 page

Build and run (in the container):
    g++ -std=c++17 -Wall -Wextra amp_star.cpp -o amp_star
    ./amp_star

Output (g++ 11, cssimages/linuxlab):
    aVar = 7, bVar = 6
    show: 10
    peek: 10
    gValue = 21

Follow aVar: 5, then r = 6 (through the reference), bVar copies 6, then
*bPtr = 7. addOne makes it 8, addTwo makes it 10. getRef() = 20 sets gValue,
and *getPtr() = *getPtr() + 1 makes it 21.

Try it: remove the // in front of  &aVar = bPtr;  and build again:
    amp_star.cpp:25:5: error: lvalue required as left operand of assignment
       25 |     &aVar = bPtr;     // does not compile: an address cannot be assigned to (see README.txt)
          |     ^~~~~
An address is a value, like 5: you can copy it, pass it, compare it, but you
can't assign to it, so the address of a variable never changes.

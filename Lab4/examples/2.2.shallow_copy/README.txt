2.2.shallow_copy -- what the compiler-written copy does to a class that owns memory

Build and run (in the container):
    g++ -std=c++17 -Wall -Wextra -g shallow.cpp -o shallow
    ./shallow

Output (g++ 11, cssimages/linuxlab):
    a.get(0) = 99
    free(): double free detected in tcache 2
    Aborted (core dumped)
(exit code 134)

Numbers has a destructor but no copy constructor, so for  Numbers b = a;
the compiler writes one that copies each member. data_ is a pointer, so b
gets a copy of the ADDRESS:

    a.data_ --+
              +--> [ 10 | 0 | 0 ]      one array, two owners
    b.data_ --+

- b.set(0, 99) changes the shared array, so a.get(0) prints 99, not 10.
- At the end of main, ~b deletes the array, then ~a deletes the same array
  again: a double free. glibc notices and aborts the program.

valgrind --leak-check=full ./shallow points at both deletes:
    Invalid free() / delete / delete[] / realloc()
       by 0x40139E: Numbers::~Numbers() (shallow.cpp:14)
       by 0x401282: main (shallow.cpp:30)
     ... (where it was freed the first time)
       by 0x40139E: Numbers::~Numbers() (shallow.cpp:14)
       by 0x401276: main (shallow.cpp:30)

The fix is the rule of three: see example 2.3.

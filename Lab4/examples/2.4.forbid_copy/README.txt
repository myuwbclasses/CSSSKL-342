2.4.forbid_copy -- a class that owns memory and can't be copied at all

Build and run (in the container):
    g++ -std=c++17 -Wall -Wextra -g nocopy.cpp -o nocopy
    ./nocopy

Output (g++ 11, cssimages/linuxlab):
    10

valgrind --leak-check=full ./nocopy: no errors, no leaks.

Numbers is example 2.2's class. Instead of writing a deep copy (example 2.3),
it says copying isn't allowed:
    Numbers(const Numbers &) = delete;
    Numbers &operator=(const Numbers &) = delete;
Now the compiler won't write the shallow versions, and any copy is a compile
error instead of a double free at run time. Passing by reference
(show(const Numbers &)) makes no copy, so it still works.

Try it: uncomment  Numbers b = a;  (line 32):
    nocopy.cpp:32:17: error: use of deleted function 'Numbers::Numbers(const Numbers&)'
    nocopy.cpp:14:5: note: declared here

Try it: uncomment  Numbers c(5); c = a;  (line 33):
    nocopy.cpp:33:23: error: use of deleted function 'Numbers& Numbers::operator=(const Numbers&)'
    nocopy.cpp:15:14: note: declared here

Passing a Numbers BY VALUE (void show(Numbers nums)) is a copy too, so it
gets the same copy-constructor error.

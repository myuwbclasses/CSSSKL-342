2.1.shallow_vs_deep -- shallow vs. deep copy of a 4-element int array

Build and run (in the container):
    g++ -std=c++17 -Wall -Wextra -g copies.cpp -o copies
    ./copies

Output (g++ 11, cssimages/linuxlab; your addresses will differ):
    original points to 0x238efeb0: 99 20 30 40
    shallow  points to 0x238efeb0: 99 20 30 40
    deep     points to 0x238efed0: 10 20 30 40

valgrind --leak-check=full ./copies: no errors, no leaks.

    original --+
               +--> [ 99 | 20 | 30 | 40 ]    0x238efeb0   one array, two pointers
    shallow  --+

    deep     -----> [ 10 | 20 | 30 | 40 ]    0x238efed0   its own array

- shallow = original copies the ADDRESS: original and shallow print the same
  address, so changing original[0] shows up through shallow as well.
- deep gets its own array from new, and the loop copies the VALUES into it:
  a different address, so it keeps 10.
- One array means one delete[]: delete[] original also frees what shallow
  points at. Deleting through both would be a double free.

When a class has a pointer member, the compiler-written copy constructor does
what  shallow = original  does here: example 2.2 shows what goes wrong.

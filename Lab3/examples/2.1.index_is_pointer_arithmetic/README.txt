2.1.index_is_pointer_arithmetic -- a[i] is *(a + i), an index can be negative,
and nothing checks array bounds

Build and run (in the container):
    g++ -std=c++17 -Wall -Wextra index.cpp -o index
    ./index

Output (g++ 11, cssimages/linuxlab):
    a[3] = 40,  *(a + 3) = 40
    p[0] = 30
    p[1] = 40
    p[-1] = 20
    p[-2] = 10,  *(p - 2) = 10
    wrote b[4] and b[-1]: no error, no crash
    b's own 4 elements are unchanged: 1 2 3 4 (10 and 5 went into memory that isn't b's)

    a:    [ 10 ][ 20 ][ 30 ][ 40 ][ 50 ]
            a[0]  a[1]  a[2]  a[3]  a[4]
           p[-2] p[-1]  p[0]  p[1]  p[2]
                         ^
                         p = &(a[2])

C++ defines x[i] as *(x + i) for any pointer x and any int i: start at x and
move i elements. So a[3] and *(a + 3) are the same element, and from p,
which points at a[2], p[-2] steps two elements back to a[0].

A negative index only makes sense from a pointer into the middle.

********************************************************************
  WARNING: C++ DOES NOT CHECK ARRAY BOUNDS.
********************************************************************
b has 4 elements, b[0] to b[3]. b[4] = 10 and b[-1] = 5 write outside it:
  - g++ -Wall -Wextra compiles them without a single warning,
  - the program runs to the end without crashing (exit code 0),
  - and valgrind reports ERROR SUMMARY: 0 errors (b is a local variable,
    and valgrind only checks heap memory).
The 10 and the 5 overwrote whatever happened to be next to b: another
variable, or the information the program needs to return from a function.
Undefined behavior: it may look fine, give wrong answers later, or crash
somewhere far away. Java would throw ArrayIndexOutOfBoundsException; C++
says nothing. Keeping every index between 0 and size - 1 is YOUR job.

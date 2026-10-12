2.3.array_2d -- int a[2][3], and reaching it through an int ** (pointer to pointer)

Build and run (in the container):
    g++ -std=c++17 -Wall -Wextra array2d.cpp -o array2d
    ./array2d

Output (g++ 11, cssimages/linuxlab; addresses vary):
    1 2 3
    4 5 60
    &a[0][2] = 0x7ffffd91c848  &a[1][0] = 0x7ffffd91c84c
    p[1][2] = 60
    *(*(p + 1) + 2) = 60

a[2][3] is 2 rows of 3 ints, stored as ONE contiguous block of 6 ints, row
after row: a[1][0] is 4 bytes after a[0][2]. a[r][c] is row r, column c.

The code writes the parentheses out to show how C++ groups each expression:
[] is applied left to right, and binds tighter than * and &.
    a[r][c]     is  (a[r])[c]         pick row r, then column c in that row
    &a[0][2]    is  &((a[0])[2])      the address of that element
    int *x[2]   is  int *(x[2])       x is an array of 2 pointers
    p[1][2]     is  (p[1])[2]         is  *(*(p + 1) + 2)

Try it: remove the // in front of  int **bad(a);  and build again:
    array2d.cpp:27:15: error: cannot convert 'int (*)[3]' to 'int**' in initialization
An int ** must point to a POINTER, and a holds only ints. (a becomes a
pointer to its first ROW, int (*)[3]: a different type.)

To use an int **, build the middle level yourself, an array of row pointers:

      p                rows                  the ints (a: one block)
   +-----+          +-----+            +----+----+----+
   |  o--+--------> |  o--+----------> |  1 |  2 |  3 |   a[0]
   +-----+          +-----+            +----+----+----+
                    |  o--+----------> |  4 |  5 | 60 |   a[1]
                    +-----+            +----+----+----+
    int **          int *[2]                int

p[1][2] follows two pointers: p -> rows[1] -> the third int of row 1 (60).
This is the layout you'll use for a 2D array whose size is known only at
run time: rows made with new int *[nRows], each row with new int[nCols].

// array2d.cpp -- int a[2][3]: 2 rows of 3 ints, stored as ONE block of 6 ints,
// row after row. And how an int ** (pointer to pointer) can reach the same ints.
//
// Parentheses below show how C++ actually groups each expression. [] is applied
// left to right, and [] binds tighter than * and &:
//     a[r][c]    means  (a[r])[c]     -- first pick row r, then column c in it
//     &a[0][2]   means  &((a[0])[2])  -- the address of that element
//     int *x[2]  means  int *(x[2])   -- x is an ARRAY of 2 pointers, not a pointer to an array
#include <iostream>
using namespace std;

int main() {
    int a[2][3] = {{1, 2, 3},
                   {4, 5, 6}};      // set them all, row by row
    (a[1])[2] = 60;                 // set one: row 1, then column 2   (usually written a[1][2])

    for (int r = 0; r < 2; r++) {   // nested loops: each row, then each column
        for (int c = 0; c < 3; c++) {
            cout << (a[r])[c] << " ";
        }
        cout << endl;
    }

    // One block: (a[1])[0] sits right after (a[0])[2], 4 bytes later.
    cout << "&a[0][2] = " << &((a[0])[2]) << "  &a[1][0] = " << &((a[1])[0]) << endl;

    // int **bad(a);                // does NOT compile: a holds ints, not pointers (README.txt)
    int *rows[2] = {a[0], a[1]};    // means int *(rows[2]): an array of 2 pointers, one to the
                                    // start of each row (g++ warns if you write those parentheses)
    int **p(rows);                  // NOW int ** is legal: p points to rows[0]
    cout << "p[1][2] = " << (p[1])[2] << endl;             // (p[1]) is rows[1]; then [2] is the 60
    // The same thing as pure pointer arithmetic:  *(*(p + 1) + 2)
    cout << "*(*(p + 1) + 2) = " << *(*(p + 1) + 2) << endl;
    return 0;
}


// Memory sketch of a, rows, and p (each box of a is one 4-byte int):
//
//     p               rows
//  +-----+         +-----+
//  |  o--+-------> |  o--+----------------+    rows[0] = a[0]
//  +-----+         +-----+                |
//   int **         |  o--+----------------|--------------+   rows[1] = a[1]
//                  +-----+                |              |
//                  int *[2]               v              v
//                                      +----+----+----+----+----+----+
//                                   a: |  1 |  2 |  3 |  4 |  5 | 60 |
//                                      +----+----+----+----+----+----+
//                                      |<-- a[0] ---->|<-- a[1] ---->|
//                                        a[0][0]       a[1][0]   a[1][2]
//
// a is ONE block of 6 ints, row after row; it holds no pointers, which is
// why int **bad(a) doesn't compile. rows is a separate array of 2 pointers
// into a, and p points to rows[0]. So p[1][2], that is (p[1])[2], follows
// p -> rows[1] -> a[1][0], then moves 2 ints to a[1][2], the 60.

// index.cpp -- a[i] is just *(a + i), so an index can be negative,
// and NOTHING checks that an index is inside the array.
#include <iostream>
using namespace std;

int main() {
    int a[5] = {10, 20, 30, 40, 50};

    // The same element, written two ways: indexing IS pointer arithmetic.
    cout << "a[3] = " << a[3] << ",  *(a + 3) = " << *(a + 3) << endl;

    // Point p at the middle element. Now indexes count from p, both ways.
    int *p = &(a[2]);
    cout << "p[0] = " << p[0] << endl;               // a[2]
    cout << "p[1] = " << p[1] << endl;               // a[3]
    cout << "p[-1] = " << p[-1] << endl;             // a[1]
    cout << "p[-2] = " << p[-2] << ",  *(p - 2) = " << *(p - 2) << endl;             // a[0]

    // ************************************************************************
    // WARNING: C++ DOES NOT CHECK ARRAY BOUNDS.
    // b has 4 elements, b[0] to b[3]. Both lines below write OUTSIDE b, into
    // whatever memory is next to it. They compile without a warning and run
    // without a crash or an error message: the bug is silent.
    // ************************************************************************
    int b[4] = {1, 2, 3, 4};
    b[4] = 10;     // one past the end
    b[-1] = 5;     // one before the start
    cout << "wrote b[4] and b[-1]: no error, no crash" << endl;
    cout << "b's own 4 elements are unchanged:";
    for (int i = 0; i < 4; i++) {
        cout << " " << b[i];
    }
    cout << " (10 and 5 went into memory that isn't b's)" << endl;

    return 0;
}

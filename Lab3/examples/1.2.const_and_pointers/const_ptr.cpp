// const_ptr.cpp -- where the const goes decides WHAT is constant.
// Read a declaration right to left: "p is a pointer to a const int".
#include <iostream>
using namespace std;

int main() {
    int a = 1;
    int b = 2;

    const int *p = &a;   // pointer to const int: can't change a THROUGH p, can move p
    // *p = 10;          // error: assignment of read-only location '* p'
    p = &b;              // OK: p now points to b

    int *const q = &a;   // const pointer to int: can change a through q, can't move q
    *q = 10;             // OK: a is now 10
    // q = &b;           // error: assignment of read-only variable 'q'

    cout << "*p = " << *p << ", *q = " << *q << ", a = " << a << "\n";
    return 0;
}

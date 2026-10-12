// copy_test.cpp -- what happens when an IntArray is copied, and assigned?
// Part A runs as is. Uncomment Part B once IntArray has operator=.
// Otherwise, do not change.

#include <iostream>
#include "intarray.h"
using namespace std;

void printByValue(IntArray arr) {
    cout << "in printByValue: " << arr.toString() << endl;
}

int main() {
    IntArray a;
    a.add(1);
    a.add(2);
    a.add(3);

    // ---------------------------------------------------- Part A: copying
    IntArray b = a;          // copy constructor
    b.set(0, 99);
    cout << "a: " << a.toString() << endl;             // should still be [1, 2, 3]
    cout << "b: " << b.toString() << endl;             // [99, 2, 3]

    b.add(4);
    b.add(5);                // b grows; a must not notice
    cout << "a: " << a.toString() << endl;             // [1, 2, 3]
    cout << "b: " << b.toString() << endl;             // [99, 2, 3, 4, 5]

    printByValue(a);         // copy constructor again
    cout << "a after printByValue: " << a.toString() << endl;             // [1, 2, 3]

    // ---------------------------------------------------- Part B: assigning
    // IntArray c;
    // c.add(42);
    // c = a;                   // operator=: c already exists (and owns an array)
    // c.set(0, 99);
    // cout << "a: " << a.toString() << endl;                  // [1, 2, 3]
    // cout << "c: " << c.toString() << endl;                  // [99, 2, 3]

    // a = a;                   // self-assignment must be harmless
    // cout << "a = a: " << a.toString() << endl;              // [1, 2, 3]

    // IntArray d;
    // IntArray e;
    // d = e = a;               // chaining: operator= returns *this
    // e.set(1, 0);
    // cout << "d: " << d.toString() << endl;                  // [1, 2, 3]
    // cout << "e: " << e.toString() << endl;                  // [1, 0, 3]
    return 0;
}

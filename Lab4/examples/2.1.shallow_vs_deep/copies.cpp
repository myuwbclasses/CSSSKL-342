// copies.cpp -- shallow vs. deep copy of a 4-element int array.
// Shallow: copy the POINTER (both point at one array). Deep: new array, copy the VALUES.
#include <iostream>
using namespace std;

void print(const char *name, const int *p) {
    cout << name << " points to " << p << ":";          // the address the pointer holds
    for (int i = 0; i < 4; i++) {
        cout << " " << p[i];
    }
    cout << endl;
}

int main() {
    int *original = new int[4]{10, 20, 30, 40};
    int *shallow = original;                 // shallow copy: same address, ONE array
    int *deep = new int[4];                  // deep copy: its own array ...
    for (int i = 0; i < 4; i++) {
        deep[i] = original[i];               // ... holding copies of the values
    }

    original[0] = 99;                        // change the original array
    print("original", original);
    print("shallow ", shallow);              // same address, so it sees 99
    print("deep    ", deep);                 // different address, still 10

    delete[] original;                       // frees shallow's array too: never delete[] both
    delete[] deep;
    return 0;
}

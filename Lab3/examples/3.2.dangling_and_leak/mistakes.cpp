// mistakes.cpp -- three classic heap mistakes: one dangling pointer, two leaks.
// Run it under valgrind:   valgrind --leak-check=full ./mistakes
#include <iostream>
using namespace std;

void forget() {
    int *temp = new int[10];    // 3. temp is a local: it dies at the }, the 10 ints don't
    temp[0] = 1;
}                               //    no delete[]: nobody has their address any more

int main() {
    // 1. A dangling pointer: two pointers to one block, delete through one.
    int *first = new int(7);
    int *second = first;        // copies the ADDRESS, not the int
    delete first;
    first = nullptr;            // fixes first ... but second still holds the old address
    cout << "second still points to " << second << ", which is no longer ours" << endl;
    // cout << *second << endl;              // use after delete: valgrind "Invalid read"

    // 2. A guaranteed leak: lose the only pointer to a block before deleting it.
    int *block = new int[100];
    block = new int[100];       // the first 100 ints can never be freed now
    delete[] block;             // frees only the second block

    forget();                   // 3. leaks 10 ints every time it's called
    cout << "end of main" << endl;
    return 0;
}

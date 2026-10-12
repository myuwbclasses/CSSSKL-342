// amp_star.cpp -- every row of the two & and * tables, in one small program.
#include <iostream>
using namespace std;

int gValue = 10;                   // a global: it lives for the whole program

int &getRef() { return gValue; }   // & in a declaration: returns a reference
int* getPtr() { return &gValue; }  // * in a declaration: returns a pointer
                                   // & in a statement:   the address of gValue

void addOne(int &n) { n = n + 1; }                                 // reference parameter
void show(const int &n) { cout << "show: " << n << "\n"; }         // const reference
void addTwo(int *p) { *p = *p + 2; }                               // pointer parameter
void peek(const int *p) { cout << "peek: " << *p << "\n"; }        // pointer to const

int main() {
    int aVar = 5;
    int *aPtr = &aVar;   // declaration: aPtr is a pointer;  statement part: &aVar is an address
    int &r = aVar;       // declaration: r is a reference, another name for aVar
    int *bPtr = aPtr;    // declaration: bPtr is a pointer, holding the same address as aPtr

    r = 6;               // through the reference: aVar is now 6
    int bVar = *aPtr;    // dereference on the right: bVar gets 6
    *bPtr = 7;           // dereference on the left: aVar receives 7
    // &aVar = bPtr;     // does not compile: an address cannot be assigned to (see README.txt)
    cout << "aVar = " << aVar << ", bVar = " << bVar << "\n";

    addOne(aVar);        // pass by reference: aVar is 8
    addTwo(&aVar);       // pass an address:   aVar is 10
    show(aVar);
    peek(&aVar);

    getRef() = 20;       // a returned reference can be on the left of =
    *getPtr() = *getPtr() + 1;   // so can a dereferenced returned pointer
    cout << "gValue = " << gValue << "\n";
    return 0;
}

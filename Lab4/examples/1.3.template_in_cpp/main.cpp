// main.cpp -- the same Box code as example 1.2, but it includes box.h,
// so it sees only the declarations, not the member definitions.
#include <iostream>
#include <string>
#include "box.h"
using namespace std;

int main() {
    Box<int> a(5);                          // T is int
    Box<string> b("hello");                 // T is string
    a.set(a.get() + 1);
    cout << a.get() << " " << b.get() << endl;              // 6 hello
    cout << a << " " << b << endl;                          // [6] [hello]
    return 0;
}

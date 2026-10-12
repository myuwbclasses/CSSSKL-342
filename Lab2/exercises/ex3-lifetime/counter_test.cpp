// counter_test.cpp -- tests for Counter. Do not change this file.

#include <iostream>
#include "counter.h"
using namespace std;

void report(const Counter &c) {
    cout << "count = " << c.value() << endl;             // needs a const value()
}

int main() {
    Counter c;
    c.value() = 4;         // needs value() to return a reference
    c.value()++;
    report(c);             // count = 5

    const Counter fixed;
    report(fixed);         // count = 0
    // fixed.value() = 9;  // Q6: uncomment this line. What happens, and why?
    return 0;
}

// main.cpp -- driver for the Rational class. Do not change this file.

#include <iostream>
#include "rational.h"
using namespace std;

// Prints a Rational. Takes it by const reference: no copy, no changes.
void show(const string &label, const Rational &r) {
    cout << label << r.toString() << "  (" << r.toDouble() << ")" << endl;
}

int main() {
    Rational zero;
    Rational five(5);
    Rational a(6, -8);
    Rational b(10, 4);
    Rational c(0, 7);

    show("default: ", zero);    // 0
    show("five:    ", five);    // 5
    show("6/-8:    ", a);       // -3/4
    show("10/4:    ", b);       // 5/2
    show("0/7:     ", c);       // 0

    cout << "a = " << a.numerator() << " over " << a.denominator() << endl;
    return 0;
}

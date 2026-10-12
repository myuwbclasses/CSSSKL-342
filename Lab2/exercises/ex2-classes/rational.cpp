// rational.cpp -- member function definitions for Rational. Complete the TODOs.

#include "rational.h"

#include <numeric>   // gcd
using namespace std;

// TODO 1: leave this body empty at first, run main, and note what
//         "default:" prints (Q2). Then initialize num_ and den_ with an
//         initializer list.
Rational::Rational() {
}

// TODO 2: initialize with an initializer list.
Rational::Rational(int whole) {
}

// TODO 3: initialize with an initializer list, then call normalize().
Rational::Rational(int num, int den) {
}

int Rational::numerator() {
    return num_;
}

int Rational::denominator() {
    return den_;
}

// TODO 4: return the value as a double (watch out for integer division).
double Rational::toDouble() {
    return 0.0;
}

// TODO 5: "num/den", or just "num" when den_ is 1. (Hint: to_string)
string Rational::toString() {
    return "";
}

// TODO 6: if den_ is negative, flip the sign of both. Then divide both by
//         gcd(num_, den_). (gcd(0, d) is d, so 0/5 becomes 0/1.)
void Rational::normalize() {
}

// rational.h -- a fraction num/den, always stored in lowest terms with den > 0.
//
// STARTER CODE: rational.cpp is incomplete, and main.cpp does not compile
// until you fix one problem in this file (see the handout).
#ifndef RATIONAL_H
#define RATIONAL_H

#include <string>

class Rational {
public:
    Rational();                    // 0/1
    Rational(int whole);           // whole/1
    Rational(int num, int den);    // precondition: den != 0

    int numerator();
    int denominator();
    double toDouble();
    std::string toString();        // "3/4", or just "2" when the denominator is 1

private:
    int num_;
    int den_;

    void normalize();              // reduce to lowest terms; make den_ positive
};

#endif

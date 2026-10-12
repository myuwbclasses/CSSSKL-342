// rational.h -- Rational from Lab 2. The constructor will now throw
// std::invalid_argument when the denominator is 0 (TODO 1 in rational.cpp).
#ifndef RATIONAL_H
#define RATIONAL_H

#include <string>

class Rational {
public:
    Rational();
    Rational(int whole);
    Rational(int num, int den);    // throws std::invalid_argument if den == 0

    int numerator() const;
    int denominator() const;
    double toDouble() const;
    std::string toString() const;

private:
    int num_;
    int den_;

    void normalize();
};

#endif

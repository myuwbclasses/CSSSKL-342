// rational.h -- Rational from Exercise 2 (complete), plus operators to add.
#ifndef RATIONAL_H
#define RATIONAL_H

#include <iosfwd>   // declares std::ostream without all of <iostream>
#include <string>

class Rational {
public:
    Rational();
    Rational(int whole);
    Rational(int num, int den);    // precondition: den != 0

    int numerator() const;
    int denominator() const;
    double toDouble() const;
    std::string toString() const;

    // Compound assignment: changes *this, returns *this by reference.
    Rational &operator+=(const Rational &rhs);
    // TODO: declare operator*=

private:
    int num_;
    int den_;

    void normalize();
};

// Non-member operators, so that  2 + r  works as well as  r + 2.
Rational operator+(const Rational &a, const Rational &b);
// TODO: declare operator- and operator*

bool operator==(const Rational &a, const Rational &b);
// TODO: declare operator!=
bool operator<(const Rational &a, const Rational &b);

std::ostream &operator<<(std::ostream &out, const Rational &r);

#endif

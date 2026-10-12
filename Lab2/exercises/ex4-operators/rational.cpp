// rational.cpp -- Rational members (complete) and operators (TODO).

#include "rational.h"

#include <numeric>
#include <ostream>
using namespace std;

Rational::Rational() : num_(0), den_(1) {
}

Rational::Rational(int whole) : num_(whole), den_(1) {
}

Rational::Rational(int num, int den) : num_(num), den_(den) {
    normalize();
}

int Rational::numerator() const {
    return num_;
}

int Rational::denominator() const {
    return den_;
}

double Rational::toDouble() const {
    return static_cast<double>(num_) / den_;
}

string Rational::toString() const {
    if (den_ == 1) {
        return to_string(num_);
    }
    return to_string(num_) + "/" + to_string(den_);
}

void Rational::normalize() {
    if (den_ < 0) {
        num_ = -num_;
        den_ = -den_;
    }
    int g = gcd(num_, den_);
    num_ /= g;
    den_ /= g;
}

// ------------------------------------------------------------------ TODO
// a/b + c/d = (a*d + c*b) / (b*d). Update num_ and den_, normalize, and
// return *this.
Rational &Rational::operator+=(const Rational &rhs) {
    return *this;
}

// TODO: operator*=

// Hint: implement + using +=:  Rational result = a; result += b; return result;
Rational operator+(const Rational &a, const Rational &b) {
    return Rational();
}

// TODO: operator- and operator*

// Both sides are always in lowest terms, so compare the parts.
bool operator==(const Rational &a, const Rational &b) {
    return false;
}

// TODO: operator!=  (write it using ==)

// a/b < c/d  exactly when  a*d < c*b  (the denominators are positive).
bool operator<(const Rational &a, const Rational &b) {
    return false;
}

// Print r.toString() and return the stream.
ostream &operator<<(ostream &out, const Rational &r) {
    return out;
}

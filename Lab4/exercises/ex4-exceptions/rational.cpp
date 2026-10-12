// rational.cpp -- Rational members.

#include "rational.h"

#include <numeric>
#include <stdexcept>
using namespace std;

Rational::Rational() : num_(0), den_(1) {
}

Rational::Rational(int whole) : num_(whole), den_(1) {
}

// TODO 1: if den is 0, throw invalid_argument("denominator is zero").
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

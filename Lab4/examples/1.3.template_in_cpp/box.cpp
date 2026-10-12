// box.cpp -- the same member definitions as example 1.2. This file compiles
// fine but produces no code at all: nothing in it asks for Box<int> or
// Box<string> (or operator<< for them), so none is instantiated.
#include <string>
#include "box.h"
using namespace std;

// Take note that the class's name is Box<T>, not Box: each member defined
// outside the class repeats the template line and says Box<T>::. (The
// constructor's own name stays Box: Box<T>::Box.)
template <typename T>
Box<T>::Box(const T &value) : value_(value) {}

template <typename T>
T Box<T>::get() const {
    return value_;
}

template <typename T>
void Box<T>::set(const T &value) {
    value_ = value;
}

// operator<< is not a member (no Box<T>::), but a friend, so it can read value_.
// It is written with T here, while the friend line in the class says U.
// That's fine: this is its own template, and its template line starts a new
// scope, so T here is just this function's parameter name (no class T is in
// scope out here). Template parameter names don't have to match; only the
// shape must: "for any type, operator<<(ostream &, const Box<that type> &)".
// Both lines declare that same template, so this is the friend.
template <typename T>
ostream &operator<<(ostream &out, const Box<T> &box) {
    out << "[" << box.value_ << "]";        // needs T to support << too
    return out;
}

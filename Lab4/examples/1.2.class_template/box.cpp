// box.cpp -- a class template: Box<T> holds one value of any type T.
#include <iostream>
#include <string>
#include <vector>
using namespace std;

template <typename T>
class Box {
public:
    explicit Box(const T &value);
    T get() const;
    void set(const T &value);

    // Why template <typename U>, and not T?
    // - Inside the class, T is already taken: it is THIS Box's type (int,
    //   in Box<int>). Writing template <typename T> again is an error:
    //   "declaration of template parameter 'T' shadows template parameter".
    // - Leaving the template line out, as for a normal class:
    //       friend ostream &operator<<(ostream &out, const Box<T> &box);
    //   declares a plain (non-template) function for each Box: for Box<int>,
    //   operator<<(ostream &, const Box<int> &). Nobody writes that
    //   function. The operator<< template we define is a different function,
    //   so g++ warns (-Wnon-template-friend) and the link fails.
    // - So the friend gets a template line of its own, with a new name, U:
    //   "every operator<< <U>, for any U, is a friend of Box<T>". When main
    //   does cout << a (a is a Box<int>), U is deduced as int.
    template <typename U>
    friend ostream &operator<<(ostream &out, const Box<U> &box);

private:
    T value_;
};

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

int main() {
    Box<int> a(5);                          // T is int
    Box<string> b("hello");                 // T is string
    a.set(a.get() + 1);
    cout << a.get() << " " << b.get() << endl;              // 6 hello
    cout << a << " " << b << endl;                          // [6] [hello]: U is int, then string

    vector<int> v;                          // the library's class templates work the same way:
    v.push_back(10);                        // vector<int> is a growable array of ints
    v.push_back(20);
    cout << v.size() << " " << v[1] << endl;                // 2 20
    return 0;
}

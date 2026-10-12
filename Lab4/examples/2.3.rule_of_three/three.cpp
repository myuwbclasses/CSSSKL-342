// three.cpp -- example 2.2's Numbers, done right: the rule of three.
// The same class, plus a copy constructor and operator= that make DEEP copies.
#include <iostream>
using namespace std;

class Numbers {
public:
    // explicit: this constructor runs only when you ask for it, as in  Numbers a(3);
    // Without explicit, C++ may also use it to quietly turn an int into a Numbers:
    // Numbers a = 3;  would compile, and passing 3 to a function that takes a
    // const Numbers & would build a temporary Numbers of 3 zeros. explicit makes
    // both a compile error. Use it on any constructor that takes one argument.
    explicit Numbers(int n) : data_(new int[n]()), size_(n) {}
    ~Numbers() { delete[] data_; }                      // 1. destructor: release what you own

    Numbers(const Numbers &other)                       // 2. copy constructor: a NEW object
        : data_(new int[other.size_]), size_(other.size_) {    // gets its OWN array,
        cout << "  copy constructor" << endl;
        for (int i = 0; i < size_; i++) {
            data_[i] = other.data_[i];                  //    holding copies of the values
        }
    }

    Numbers &operator=(const Numbers &other) {          // 3. copy assignment: this object already
        cout << "  operator=" << endl;                  //    exists and already owns an array
        if (this != &other) {                           //    a = a must change nothing
            int *copy = new int[other.size_];           //    copy first,
            for (int i = 0; i < other.size_; i++) {
                copy[i] = other.data_[i];
            }
            delete[] data_;                             //    then release the old array,
            data_ = copy;                               //    then re-point
            size_ = other.size_;
        }
        return *this;                                   //    so c = b = a works
    }

    void set(int i, int value) { data_[i] = value; }
    int get(int i) const { return data_[i]; }

private:
    int *data_;
    int size_;      // how many ints data_ holds
};

int main() {
    Numbers a(3);
    a.set(0, 10);
    cout << "Numbers b = a;" << endl;
    Numbers b = a;              // b is NEW: copy constructor, b gets its own array
    b.set(0, 99);               // so changing b leaves a alone
    Numbers c(5);
    cout << "c = b;" << endl;
    c = b;                      // c ALREADY exists: operator= releases its 5 ints
    cout << "a = a;" << endl;
    a = a;                      // self-assignment: safe
    cout << "a.get(0) = " << a.get(0) << ", b.get(0) = " << b.get(0)
         << ", c.get(0) = " << c.get(0) << endl;                // 10, 99, 99
    return 0;                   // ~c, ~b, ~a: each deletes its OWN array
}

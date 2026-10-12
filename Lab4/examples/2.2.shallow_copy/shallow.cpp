// shallow.cpp -- a class that owns an array, with a destructor but NO copy
// constructor. The compiler-written copy copies the POINTER, not the array.
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
    ~Numbers() { delete[] data_; }
    void set(int i, int value) { data_[i] = value; }
    int get(int i) const { return data_[i]; }

private:
    int *data_;
    int size_;      // how many ints data_ holds
};

int main() {
    Numbers a(3);
    a.set(0, 10);
    Numbers b = a;              // compiler-written copy: b.data_ is a.data_, ONE shared array
    b.set(0, 99);               // so changing b changes a
    cout << "a.get(0) = " << a.get(0) << endl;                // 99, not 10
    return 0;                   // ~b deletes the array, then ~a deletes it AGAIN
}

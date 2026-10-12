// nocopy.cpp -- example 2.2's Numbers, made safe the other way: no copies at all.
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
    Numbers(const Numbers &) = delete;                  // no copy constructor
    Numbers &operator=(const Numbers &) = delete;       // no operator=
    void set(int i, int value) { data_[i] = value; }
    int get(int i) const { return data_[i]; }

private:
    int *data_;
    int size_;      // how many ints data_ holds
};

void show(const Numbers &nums) {        // by reference: no copy, so this is fine
    cout << nums.get(0) << endl;
}

int main() {
    Numbers a(3);
    a.set(0, 10);
    show(a);                            // 10
    // Numbers b = a;                   // Try it: compile error, copy constructor is deleted
    // Numbers c(5); c = a;             // Try it: compile error, operator= is deleted
    return 0;
}

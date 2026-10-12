// increment.cpp -- pre-increment (++x) and post-increment (x++) on your own
// class: what each returns. Iterators overload them the same way.
#include <iostream>
using namespace std;

class Counter {
public:
    explicit Counter(int start) : n_(start) {}
    int value() const { return n_; }

    Counter &operator++() {        // ++c: move first, then return THIS object
        n_++;
        return *this;
    }

    Counter operator++(int) {      // c++: the unused int marks it as postfix;
        Counter old = *this;       //      save the old state,
        n_++;                      //      move,
        return old;                //      return the OLD state, by value
    }

private:
    int n_;
};

int main() {
    Counter c(5);
    Counter a = ++c;               // c becomes 6, a is 6
    cout << "after a = ++c: a = " << a.value() << ", c = " << c.value() << endl;
    Counter b = c++;               // b is 6 (the old value), c becomes 7
    cout << "after b = c++: b = " << b.value() << ", c = " << c.value() << endl;
    return 0;
}

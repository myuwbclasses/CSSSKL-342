// return_this.cpp -- why += returns *this (the current object) by reference.
//
// Build and run (in VS Code's terminal, attached to your container):
//   g++ -std=c++17 -Wall -Wextra return_this.cpp -o return_this
//   ./return_this
// README.txt in this folder shows the real output.

#include <iostream>
using namespace std;

class Money {
public:
    Money(int cents) : cents_(cents) {}
    int cents() const { return cents_; }

    // += changes the object it is called on, then returns THAT object.
    // *this means "the current object": in  total += a  it is total itself.
    // Returning it by reference (Money &) hands back total, not a copy.
    Money &operator+=(const Money &rhs) {
        cents_ += rhs.cents_;
        return *this;
    }

private:
    int cents_;
};

int main() {
    Money total(100), a(20), b(3);

    // total += a  returns total itself, so the second += also changes total:
    // it means  total.operator+=(a).operator+=(b)
    (total += a) += b;

    cout << "total = " << total.cents() << endl;    // 100 + 20 + 3 = 123
    return 0;
}

// What if operator+= returned  Money  (by value) instead of  Money&?
// Then  total += a  would hand back a COPY of total, the second += would change
// that copy, and the copy would be thrown away: total would end up 120, not 123.

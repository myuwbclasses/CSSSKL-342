// operators.cpp -- an operator is a function: as a member, or as a non-member
// (a global function, outside any class).
//
// Build and run (in VS Code's terminal, attached to your container):
//   g++ -std=c++17 -Wall -Wextra operators.cpp -o operators
//   ./operators
// README.txt in this folder shows the real output.
// (-, *, and / work exactly the same way as + below.)

#include <iostream>
using namespace std;

class Money {
public:
    Money(int cents) : cents_(cents) {}
    int cents() const { return cents_; }

    // MEMBER operator: declared INSIDE the class. The left operand is the object
    // the function is called on, so it takes only ONE parameter (the right one).
    Money operator+(const Money &rhs) const {
        cout << "  [member] Money::operator+" << endl;
        return Money(cents_ + rhs.cents_);
    }

private:
    int cents_;
};

// The SAME operator+ written as a NON-MEMBER: declared OUTSIDE the class -- a
// global function, like any other -- so both operands are parameters (TWO).
// It does exactly the same thing. Use ONE form or the other, never both: to try
// this one, uncomment it AND comment out the member operator+ above.
//
// Money operator+(const Money &lhs, const Money &rhs) {
//     cout << "  [non-member] global operator+" << endl;
//     return Money(lhs.cents() + rhs.cents());    // only public members: it isn't a member
// }

int main() {
    Money a(500), b(120);

    // These two lines do EXACTLY the same thing:
    //   Money s1 = a + b;            <- what you normally write
    //   Money s2 = a.operator+(b);   <- what the compiler turns it into: call the
    //                                   member operator+ ON a, passing b
    // (With the non-member version, the compiler instead calls operator+(a, b):
    //  a + b stays the same, but a.operator+(b) would no longer compile.)
    cout << "a + b" << endl;
    Money s1 = a + b;
    cout << "a.operator+(b)" << endl;
    Money s2 = a.operator+(b);

    cout << s1.cents() << " " << s2.cents() << endl;    // same function, same result
    return 0;
}

// why_nonmember.cpp -- why + is usually written as a NON-member.
//
// Two classes that are identical except for one thing:
//   MemberMoney    writes operator+ as a MEMBER function
//   Money          writes operator+ as a NON-MEMBER (global) function
// Both have a constructor that takes one int, so the compiler may turn an int
// like 2 into a Money object automatically when it needs one.
//
// Build and run (in VS Code's terminal, attached to your container):
//   g++ -std=c++17 -Wall -Wextra why_nonmember.cpp -o why_nonmember
//   ./why_nonmember
// Then uncomment the line marked TRY THIS and build again: read the error.
// README.txt in this folder shows the real output and the error.

#include <iostream>
using namespace std;

// ---------------------------------------------------------------- + as a MEMBER
class MemberMoney {
public:
    MemberMoney(int cents) : cents_(cents) {}      // lets the compiler turn 2 into MemberMoney(2)
    int cents() const { return cents_; }

    MemberMoney operator+(const MemberMoney &rhs) const {
        return MemberMoney(cents_ + rhs.cents_);
    }

private:
    int cents_;
};

// ---------------------------------------------------------------- + as a NON-MEMBER
class Money {
public:
    Money(int cents) : cents_(cents) {}            // lets the compiler turn 2 into Money(2)
    int cents() const { return cents_; }

private:
    int cents_;
};

Money operator+(const Money &a, const Money &b) {   // a global function: both operands are parameters
    return Money(a.cents() + b.cents());
}

int main() {
    MemberMoney m(500);
    Money n(500);

    // ---- MEMBER version: only one order works ----
    MemberMoney m1 = m + 2;     // m.operator+(2): 2 is an ARGUMENT, so the compiler
                                //   converts it to MemberMoney(2). Works.
    // MemberMoney m2 = 2 + m;  // TRY THIS: means 2.operator+(m) -- but 2 is an int,
                                //   which has no member functions, and the compiler
                                //   never converts the object a member is called ON.
                                //   error: no match for 'operator+'
                                //          (operand types are 'int' and 'MemberMoney')
    cout << "member:     m + 2 = " << m1.cents() << endl;

    // ---- NON-MEMBER version: both orders work ----
    Money n1 = n + 2;           // operator+(n, 2): 2 converts to Money(2)
    Money n2 = 2 + n;           // operator+(2, n): 2 converts to Money(2) here too,
                                //   because BOTH operands are ordinary arguments
    cout << "non-member: n + 2 = " << n1.cents() << endl;
    cout << "non-member: 2 + n = " << n2.cents() << endl;
    return 0;
}

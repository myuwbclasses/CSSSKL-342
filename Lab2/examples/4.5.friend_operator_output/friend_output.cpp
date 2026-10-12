// friend_output.cpp -- operator<< with accessors (no friend needed) vs. without (friend).
//
// Build and run (in VS Code's terminal, attached to your container):
//   g++ -std=c++17 -Wall -Wextra friend_output.cpp -o friend_output
//   ./friend_output
// Then delete the friend line in Secret and build again: read the error.
// README.txt in this folder shows the real output and the error.

#include <iostream>
using namespace std;

// ---------------------------------------------------------------- 1. WITH accessors
class Point {
public:
    Point(int x, int y) : x_(x), y_(y) {}
    int x() const { return x_; }                  // public accessors
    int y() const { return y_; }
private:
    int x_, y_;
};

// A non-member (global) function. It only uses the PUBLIC accessors,
// so it needs no special permission: no friend.
ostream &operator<<(ostream &out, const Point &p) {
    out << "(" << p.x() << ", " << p.y() << ")";
    return out;
}

// ---------------------------------------------------------------- 2. WITHOUT accessors
class Secret {
public:
    Secret(int code) : code_(code) {}
    // No accessor for code_. To let operator<< read it, the class names that
    // function as a FRIEND. This line is only a declaration, and it does NOT
    // make operator<< a member: it's still a global function.
    friend ostream &operator<<(ostream &out, const Secret &s);
private:
    int code_;
};

// The definition: an ordinary global function. No "friend" here, no "Secret::"
// in front -- it belongs to no class. Because of the friend line above, it may
// read the private s.code_.
ostream &operator<<(ostream &out, const Secret &s) {
    out << "Secret #" << s.code_;
    return out;
}

// ---------------------------------------------------------------- the same driver for both
int main() {
    Point p(3, 4);
    Secret s(42);
    cout << p << endl;              // calls operator<<(cout, p)
    cout << s << endl;              // calls operator<<(cout, s)
    cout << p << " " << s << endl;  // chaining: each << returns the stream
    return 0;
}

// build_from.cpp -- write the real logic once; build the other operators from it.
//
// Build and run (in VS Code's terminal, attached to your container):
//   g++ -std=c++17 -Wall -Wextra build_from.cpp -o build_from
//   ./build_from

#include <iostream>
using namespace std;

class Money {
public:
    Money(int cents) : cents_(cents) {}
    int cents() const { return cents_; }

    Money &operator+=(const Money &rhs) {      // the real work of adding is HERE
        cents_ += rhs.cents_;
        return *this;
    }

private:
    int cents_;
};

// + reuses +=: copy the left side, add the right side to the copy.
Money operator+(const Money &a, const Money &b) {
    Money result = a;
    result += b;
    return result;
}

// The real work of comparing is HERE...
bool operator==(const Money &a, const Money &b) {
    return a.cents() == b.cents();
}

// ...and != just reuses it.
bool operator!=(const Money &a, const Money &b) {
    return !(a == b);
}

int main() {
    Money a(500), b(120);
    cout << (a + b).cents() << endl;            // 620
    cout << boolalpha << (a != b) << endl;      // true
    return 0;
}

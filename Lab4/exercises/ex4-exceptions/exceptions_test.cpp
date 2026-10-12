// exceptions_test.cpp -- throwing and catching. Complete the TODOs in order.

#include <iostream>
#include <stdexcept>
#include "ArrayStack.h"
#include "PrecondViolatedExcept.h"
#include "rational.h"
using namespace std;

// Throws a different kind of exception for each choice.
void risky(int choice) {
    if (choice == 1) {
        throw PrecondViolatedExcept("peek() called on an empty stack");
    }
    if (choice == 2) {
        throw out_of_range("index 7 is out of range");
    }
    if (choice == 3) {
        throw runtime_error("disk full");
    }
    cout << "  no exception" << endl;
}

int main() {
    // ---- Part A. After TODO 1 (in rational.cpp), run this once AS IS and
    // note what an uncaught exception does. Then put both lines in a try
    // block, catch const invalid_argument &, and print "caught: " and
    // e.what().
    Rational bad(1, 0);
    cout << "bad = " << bad.toString() << endl;

    cout << "after Part A" << endl;

    // ---- Part B. After TODO 2 (in ArrayStack.h): peek at an empty stack
    // inside a try block, and catch const PrecondViolatedExcept&.
    ArrayStack<int> stack;
    stack.push(1);
    stack.pop();
    // cout << stack.peek() << endl;

    // ---- Part C (TODO 3). Call risky(choice) for choice = 0, 1, 2, 3 in a
    // loop. Use ONE try block with three catch clauses, for
    // PrecondViolatedExcept, logic_error, and exception. Each
    // handler prints which clause caught it and e.what(). Choose the order
    // of the clauses carefully.

    cout << "done" << endl;
    return 0;
}

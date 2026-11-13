// test_rounding.cpp -- tests for myRound. Add your own cases at the TODO.

#include <cmath>
#include <iostream>
#include "rounding.h"
using namespace std;

int failures = 0;

// Compares myRound(input) against the expected answer and reports the result.
void check(double input, int expected) {
    int actual = myRound(input);
    if (actual == expected) {
        cout << "PASS  myRound(" << input << ") = " << actual << endl;
    } else {
        cout << "FAIL  myRound(" << input << ") = " << actual
             << ", expected " << expected << endl;
        failures++;
    }
}

int main() {
    check(0.4, 0);
    check(0.6, 1);
    check(-0.4, 0);
    check(-0.6, -1);

    // TODO: add at least 3 more cases: an exact half (2.5), a negative exact
    // half (-2.5), and 0.0. You may compare against round (from <cmath>) here,
    // in the tests.

    cout << failures << " failure(s)" << endl;
    return failures == 0 ? 0 : 1;
}

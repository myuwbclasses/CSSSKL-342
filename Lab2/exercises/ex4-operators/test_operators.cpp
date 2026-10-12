// test_operators.cpp -- tests for the Rational operators. Do not change the
// existing tests; you may add more at the end of main.
//
// The tests marked "(needs your declaration)" will not compile until you
// declare and define those operators. Uncomment them as you go.

#include <iostream>
#include <sstream>
#include <string>
#include "rational.h"
using namespace std;

int failures = 0;

void check(const string &what, const string &actual, const string &expected) {
    if (actual == expected) {
        cout << "PASS  " << what << " = " << actual << endl;
    } else {
        cout << "FAIL  " << what << " = " << actual << ", expected " << expected << endl;
        failures++;
    }
}

void check(const string &what, bool actual, bool expected) {
    check(what, string(actual ? "true" : "false"), string(expected ? "true" : "false"));
}

int main() {
    Rational half(1, 2), third(1, 3), quarter(1, 4);

    Rational r = half;
    r += third;
    check("r += 1/3", r.toString(), "5/6");
    check("1/2 + 1/3", (half + third).toString(), "5/6");
    check("1/2 + 2", (half + 2).toString(), "5/2");
    check("2 + 1/2", (2 + half).toString(), "5/2");
    check("(1/4 + 1/4) == 1/2", quarter + quarter == half, true);
    check("1/3 < 1/2", third < half, true);
    check("1/2 < 1/3", half < third, false);
    check("-1/2 < 1/3", Rational(-1, 2) < third, true);

    ostringstream out;
    out << half << " and " << Rational(4, 2);
    check("cout << ...", out.str(), "1/2 and 2");

    // (needs your declaration)
    // check("1/2 - 1/3", (half - third).toString(), "1/6");
    // check("1/2 * 2/3", (half * Rational(2, 3)).toString(), "1/3");
    // check("1/2 != 1/3", half != third, true);
    // Rational s = third;
    // s *= Rational(3, 5);
    // check("s *= 3/5", s.toString(), "1/5");
    // Rational t(1, 6);
    // (t += third) += third;
    // check("(t += 1/3) += 1/3", t.toString(), "5/6");

    cout << failures << " failure(s)" << endl;
    return failures == 0 ? 0 : 1;
}

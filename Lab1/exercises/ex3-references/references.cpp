// references.cpp -- reference variables, pass by value vs. by reference,
// const reference, and returning a reference.
// Part A is given: run it and read it. Then implement each TODO function and
// uncomment the matching lines in main().

#include <iostream>
#include <string>
using namespace std;

// ---------- Part B: passing arguments ----------

// Given (do not change): tries to add one to its argument.
void addOneByValue(int n) {
    n = n + 1;
}

// TODO: same as addOneByValue, but the caller's variable must change.
void addOneByReference(int &n);

// TODO: exchange the values of the caller's two variables.
void swapValues(int &a, int &b);

// TODO: "return" two results through reference parameters: the quotient and
// the remainder of dividend / divisor. Assume divisor is not 0.
void divide(int dividend, int divisor, int &quotient, int &remainder);

// TODO: count the vowels (a, e, i, o, u; either case) in word.
// word.size() is the number of characters, and word[k] is the character at
// position k (like Java's charAt). Make k a size_t: comparing an int with
// word.size() gives a -Wsign-compare warning (Part 2).
// Why is the parameter const string & rather than string? (Q5)
int countVowels(const string &word);

// ---------- Part C: returning a reference ----------

// TODO: return a REFERENCE to whichever of a and b is larger (a if they are
// equal), so the caller can assign to it:
//   larger(p, q) = 0;   // sets the larger of p and q to 0
int &larger(int &a, int &b);

// Given: a classic mistake. Compile with -Wall and read the warning (Q7).
int &badReference() {
    int local = 42;
    return local;
}

int main() {
    // ---------- Part A: reference variables (given) ----------
    int i = 1;
    int &r = i;     // r is another NAME for i: no new int is created
    int x = r;      // x is a new, separate int, initialized with a COPY of i's value
    cout << "start:      i = " << i << ", r = " << r << ", x = " << x << endl;

    r = 2;          // changes... which variables? (Q1)
    cout << "after r = 2: i = " << i << ", r = " << r << ", x = " << x << endl;

    // In an expression, &i means "the address of i": where i lives in memory.
    // (This & is different from the & in a declaration; pointers come later.)
    cout << "addresses:  &i = " << &i << ", &r = " << &r << ", &x = " << &x << endl;

    // Q2: uncomment the next line, compile, read the error, then comment it out again.
    // int &xr;

    // ---------- Part B: passing arguments ----------
    addOneByValue(x);
    cout << "after addOneByValue(x):     x = " << x << endl;
    // TODO: uncomment once implemented
    // addOneByReference(x);
    // cout << "after addOneByReference(x): x = " << x << endl;
    // addOneByReference(r);
    // cout << "after addOneByReference(r): i = " << i << endl;

    int a = 1, b = 2;
    // swapValues(a, b);
    cout << "a = " << a << ", b = " << b << endl;

    int quot = 0, rem = 0;
    // divide(17, 5, quot, rem);
    cout << "17 / 5 = " << quot << " remainder " << rem << endl;

    // cout << "vowels in \"Data Structures\": "
    //           << countVowels("Data Structures") << endl;

    // ---------- Part C: returning a reference ----------
    int p = 4, q = 9;
    // larger(p, q) = 0;
    cout << "p = " << p << ", q = " << q << endl;
    // larger(p, q)++;
    // cout << "p = " << p << ", q = " << q << endl;

    return 0;
}

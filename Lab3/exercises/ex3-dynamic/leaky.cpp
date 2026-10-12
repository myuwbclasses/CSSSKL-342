// leaky.cpp -- this program "works", but has three memory bugs.
// Run it under valgrind, find all three, and fix them.
//
//   valgrind --leak-check=full ./leaky

#include <iostream>
#include <string>
using namespace std;

string* makeGreeting(const string &name) {
    return new string("Hello, " + name);
}

int sumOfSquares(int n) {
    int *squares = new int[n];
    for (int i = 0; i < n; i++) {
        squares[i] = i * i;
    }
    int sum = 0;
    for (int i = 0; i <= n; i++) {
        sum += squares[i];
    }
    delete[] squares;
    return sum;
}

int main() {
    string *greeting = makeGreeting("CSS SKL 342");
    cout << *greeting << endl;

    cout << "sum of squares below 5: " << sumOfSquares(5) << endl;

    int *scores = new int[3];
    scores[0] = 90;
    scores[1] = 85;
    scores[2] = 77;
    cout << "first score: " << scores[0] << endl;
    delete scores;

    return 0;
}

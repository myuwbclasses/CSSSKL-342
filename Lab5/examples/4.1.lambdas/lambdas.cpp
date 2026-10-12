// lambdas.cpp -- passing behavior to algorithms: a named function, a lambda,
// and lambdas that capture local variables by copy [x] or by reference [&x].
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

bool shorterFirst(const string &a, const string &b) {
    return a.size() < b.size();                  // true when a must come before b
}

int main() {
    vector<string> words = {"queue", "map", "vector", "list", "set"};

    sort(words.begin(), words.end(), shorterFirst);           // a named function
    for (const auto &w : words) { cout << w << " "; }
    cout << endl;

    sort(words.begin(), words.end(),                          // the same idea as a lambda,
         [](const string &a, const string &b) { return a > b; });                 // Z to A
    for (const auto &w : words) { cout << w << " "; }
    cout << endl;

    size_t minLength = 4;                                     // a local variable ...
    auto longOnes = count_if(words.begin(), words.end(),
                             [minLength](const string &w) { return w.size() >= minLength; });
    cout << longOnes << " words have at least " << minLength << " letters" << endl;

    int x = 1;
    auto byCopy = [x]() { return x; };                        // copies x now
    auto byRef = [&x]() { return x; };                        // refers to x itself
    x = 5;
    cout << byCopy() << " " << byRef() << endl;               // 1 5
    return 0;
}

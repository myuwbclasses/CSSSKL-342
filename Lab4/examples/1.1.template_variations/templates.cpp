// templates.cpp -- function templates: one type parameter, two,
// T deduced from the arguments, and T given explicitly in < >.
#include <iostream>
#include <string>
using namespace std;

template <typename T>                    // one type parameter
T maxOf(T a, T b) {                      // the compiler writes one real maxOf for each T used
    return (a < b) ? b : a;              // so T must support <
}

template <typename A, typename B>        // two type parameters, can differ
void showBoth(A a, B b) {
    cout << a << " | " << b << endl;
}

template <typename R, typename T>        // R appears only in the return type,
R convertTo(T value) {                   // so it can't be deduced: the caller must name it
    return static_cast<R>(value);
}

int main() {
    cout << maxOf(3, 7) << endl;                           // deduced: T is int          -> 7
    cout << maxOf<int>(3, 7) << endl;                      // explicit: same function    -> 7
    cout << maxOf<double>(3, 4.5) << endl;                 // explicit: 3 becomes 3.0    -> 4.5
    cout << maxOf<string>("pear", "apple") << endl;                 // compares strings -> pear
    // cout << maxOf(3, 4.5) << endl;                      // error: is T int or double? (README.txt)

    showBoth(42, "apples");                                // deduced: A int, B const char*
    showBoth<double, string>(42, "apples");                // explicit: 42 becomes 42.0, prints 42
    showBoth<char>(65, 2.5);                               // A explicit (char: 'A'), B deduced: double

    cout << convertTo<int>(3.99) << endl;                  // R explicit, T deduced: 3 (cut, not rounded)
    cout << convertTo<char, int>(66) << endl;              // both explicit: B
    return 0;
}

// same_loop.cpp -- the same iterator loop works on a vector, a list, and a
// string; a range-based for is shorthand for it.
#include <iostream>
#include <list>
#include <string>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {3, 1, 4};
    list<int> l = {1, 5, 9};
    string s = "abc";

    for (auto it = v.begin(); it != v.end(); ++it) {   // *it is the element, ++it moves on
        cout << *it << " ";
    }
    cout << endl;

    for (auto it = l.begin(); it != l.end(); ++it) {   // same loop, a linked list underneath
        *it = *it * 10;                                // write through the iterator
    }
    for (int n : l) {                                  // range-for: begin(), !=, ++, * for you
        cout << n << " ";
    }
    cout << endl;

    for (auto it = s.rbegin(); it != s.rend(); ++it) { // reverse iterators: last to first
        cout << *it;
    }
    cout << endl;
    return 0;
}

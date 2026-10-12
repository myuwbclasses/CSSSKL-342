// list_test.cpp -- tests for SimpleList's iterator. Do not change.

#include <algorithm>
#include <iostream>
#include <string>
#include "SimpleList.h"
using namespace std;

int main() {
    SimpleList<int> numbers;
    for (int i = 1; i <= 5; i++) {
        numbers.pushBack(i * i);
    }

    cout << "range-for:";
    for (int n : numbers) {                          // uses begin, end, !=, ++, *
        cout << " " << n;
    }
    cout << endl;                                    // range-for: 1 4 9 16 25

    for (int &n : numbers) {                         // write through the iterator
        n = -n;
    }

    cout << "explicit loop:";
    for (SimpleList<int>::Iterator it = numbers.begin(); it != numbers.end(); ++it) {
        cout << " " << *it;
    }
    cout << endl;                                    // explicit loop: -1 -4 -9 -16 -25

    SimpleList<int>::Iterator it = numbers.begin();
    SimpleList<int>::Iterator old = it++;            // post-increment
    cout << "old: " << *old << ", it: " << *it << endl;             // old: -1, it: -4
    SimpleList<int>::Iterator same = ++it;           // pre-increment
    cout << "same: " << *same << ", it: " << *it << endl;           // same: -9, it: -9

    SimpleList<string> words;
    words.pushBack("stack");
    words.pushBack("queue");
    words.pushBack("list");
    auto found = find(words.begin(), words.end(), "queue");          // a standard algorithm
    cout << "found queue: " << boolalpha << (found != words.end()) << endl;                 // true
    cout << "count of list: " << count(words.begin(), words.end(), "list") << endl;                 // 1
    return 0;
}

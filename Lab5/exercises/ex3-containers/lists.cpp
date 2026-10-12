// lists.cpp -- list. Complete each TODO; print the list after each step
// with printList.

#include <iostream>
#include <list>
using namespace std;

void printList(const list<int> &values) {
    for (int v : values) {
        cout << v << " ";
    }
    cout << endl;
}

int main() {
    list<int> numbers;

    // TODO 1: add 1, 3, 5, 7, 9 to the BACK, in that order.
    // TODO 2: add 2, 4, 6, 8, 10 to the FRONT, in that order.
    //         Expected: 10 8 6 4 2 1 3 5 7 9
    // TODO 3: print the first and last elements (front(), back()).
    // TODO 4: remove the element 3 (list's own remove member function).
    // TODO 5: sort with the list's own sort() member function. Then try
    //         sort(numbers.begin(), numbers.end()) instead, read the
    //         error, and remove that line (Q2).
    // TODO 6: remove every odd number (remove_if with a lambda:
    //         [](int n) { return n % 2 != 0; }).
    // TODO 7: insert 5 just before the 6, using an iterator found with a loop.
    //         Expected: 2 4 5 6 8 10

    printList(numbers);
    return 0;
}

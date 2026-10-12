// chain_test.cpp -- tests for the node functions. Do not change.
// Run it under valgrind too: it must report no leaks and no errors.

#include <iostream>
#include "nodes.h"
using namespace std;

int main() {
    Node *head = nullptr;
    printChain(head);                                        // []
    cout << "length: " << length(head) << endl;              // 0

    pushFront(head, 4);
    pushFront(head, 1);
    pushFront(head, 3);
    printChain(head);                                        // [3 -> 1 -> 4]

    pushBack(head, 5);
    pushBack(head, 1);
    printChain(head);                                        // [3 -> 1 -> 4 -> 5 -> 1]
    cout << "length: " << length(head) << endl;              // 5

    cout << boolalpha;
    cout << "contains 5: " << contains(head, 5) << endl;             // true
    cout << "contains 9: " << contains(head, 9) << endl;             // false

    cout << "remove 1: " << removeFirst(head, 1) << endl;            // true (the first 1)
    printChain(head);                                        // [3 -> 4 -> 5 -> 1]
    cout << "remove 3: " << removeFirst(head, 3) << endl;            // true (the head)
    printChain(head);                                        // [4 -> 5 -> 1]
    cout << "remove 9: " << removeFirst(head, 9) << endl;            // false
    cout << "remove 1: " << removeFirst(head, 1) << endl;            // true (the tail)
    printChain(head);                                        // [4 -> 5]

    Node *empty = nullptr;
    pushBack(empty, 7);
    printChain(empty);                                       // [7]
    deleteChain(empty);

    deleteChain(head);
    printChain(head);                                        // []
    cout << "head is null: " << (head == nullptr) << endl;            // true
    return 0;
}

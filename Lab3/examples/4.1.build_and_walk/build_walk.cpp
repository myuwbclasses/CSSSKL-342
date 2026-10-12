// build_walk.cpp -- a hard-coded chain of 3 nodes, 10 -> 20 -> 30: build it,
// walk it, and free it. Everything in main, no functions.
#include <iostream>
using namespace std;

struct Node {
    int item;
    Node *next;                              // the next node, or nullptr after the last one
};

int main() {
    Node *head = nullptr;                    // an empty chain: no nodes yet

    Node *n30 = new Node{30, nullptr};       // build from the last node: its next is nullptr
    Node *n20 = new Node{20, n30};           // 20's next is 30
    head = new Node{10, n20};                // head -> 10 -> 20 -> 30 -> nullptr

    Node *cur = head;                        // walk: start at the first node,
    while (cur != nullptr) {                 // stop when we fall off the end,
        cout << cur->item << " ";
        cur = cur->next;                     // and move to the next node each time
    }
    cout << endl;                            // 10 20 30

    cout << head->next->next->item << endl;             // 30: two links from head

    delete head;                             // three news, so three deletes
    delete n20;
    delete n30;
    return 0;
}

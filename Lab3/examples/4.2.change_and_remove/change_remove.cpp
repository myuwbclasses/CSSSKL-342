// change_remove.cpp -- the same hard-coded chain, 10 -> 20 -> 30: remove the
// second node, remove the first node, add a node at the front. All in main.
#include <iostream>
using namespace std;

struct Node {
    int item;
    Node *next;
};

int main() {
    Node *n30 = new Node{30, nullptr};
    Node *n20 = new Node{20, n30};
    Node *head = new Node{10, n20};          // head -> 10 -> 20 -> 30

    // Remove the second node (20): link around it, then delete it.
    Node *doomed = head->next;
    head->next = doomed->next;               // 10 now points to 30
    delete doomed;                           // head -> 10 -> 30

    // Remove the first node (10): there is no node before it, so head must move.
    Node *old = head;
    head = head->next;                       // move head to 30 BEFORE deleting 10
    delete old;                              // head -> 30

    // Add 5 at the front: the new node points to the old first node.
    head = new Node{5, head};                // head -> 5 -> 30

    Node *cur = head;
    while (cur != nullptr) {
        cout << cur->item << " ";
        cur = cur->next;
    }
    cout << endl;                            // 5 30

    delete head->next;                       // free the two nodes that are left
    delete head;
    return 0;
}

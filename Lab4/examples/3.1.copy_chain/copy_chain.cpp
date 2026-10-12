// copy_chain.cpp -- copying a chain of nodes: pushing each item reverses it,
// appending at the end (remembering the last node) keeps the order.
#include <iostream>
using namespace std;

struct Node {
    int item;
    Node *next;
};

void print(const char *label, const Node *head) {
    cout << label;
    for (const Node *cur = head; cur != nullptr; cur = cur->next) {
        cout << " " << cur->item;
    }
    cout << endl;
}

int main() {
    Node *original = new Node{1, new Node{2, new Node{3, nullptr}}};   // 1 -> 2 -> 3
    print("original:", original);

    Node *pushed = nullptr;                      // copy by pushing at the front:
    for (const Node *cur = original; cur != nullptr; cur = cur->next) {
        pushed = new Node{cur->item, pushed};
    }
    print("pushed:  ", pushed);                  // 3 2 1: reversed

    Node *appended = nullptr;                    // copy by appending at the end:
    Node *last = nullptr;
    for (const Node *cur = original; cur != nullptr; cur = cur->next) {
        Node *copy = new Node{cur->item, nullptr};
        if (last == nullptr) {
            appended = copy;                     // the first copy becomes the head
        } else {
            last->next = copy;                   // each later copy hangs off the last one
        }
        last = copy;
    }
    print("appended:", appended);                // 1 2 3: same order

    for (Node *head : {original, pushed, appended}) {   // three chains, nine nodes: free them all
        while (head != nullptr) {
            Node *next = head->next;
            delete head;
            head = next;
        }
    }
    return 0;
}

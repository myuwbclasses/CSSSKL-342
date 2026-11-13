// nodes.cpp -- operations on a chain of linked nodes. Complete the TODOs.
//
// Draw boxes and arrows on paper before you write each function, and check
// three cases every time: an empty chain, a chain of one node, and a longer
// chain.

#include "nodes.h"
#include <iostream>
using namespace std;

void pushFront(Node *&head, int value) {
    Node *newNode = new Node;
    newNode->item = value;
    newNode->next = head;
    head = newNode;
}

void printChain(const Node *head) {
    cout << "[";
    for (const Node *cur = head; cur != nullptr; cur = cur->next) {
        cout << cur->item;
        if (cur->next != nullptr) {
            cout << " -> ";
        }
    }
    cout << "]" << endl;
}

// Given: counts the nodes. Read it first: walking a chain always looks like this.
int length(const Node *head) {
    int count = 0;
    for (const Node *cur = head; cur != nullptr; cur = cur->next) {
        count++;
    }
    return count;
}

// TODO 2
bool contains(const Node *head, int value) {
    return false;
}

// TODO 3: an empty chain is a special case. Otherwise walk to the last node.
void pushBack(Node *&head, int value) {
}

// TODO 4: removing the head node is a special case. Otherwise find the node
//         BEFORE the one to remove. Don't forget to delete the removed node.
bool removeFirst(Node *&head, int value) {
    return false;
}

// TODO 5: save cur->next BEFORE deleting cur.
void deleteChain(Node *&head) {
}

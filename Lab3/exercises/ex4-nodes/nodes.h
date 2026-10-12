// nodes.h -- a chain of linked nodes, the building block of Carrano's
// LinkedBag, linked stacks, and linked lists (the CSS 342 textbook).
//
// These are free functions on a raw chain (no class yet; that's Lab 4).
// head points to the first node, or is nullptr for an empty chain.
#ifndef NODES_H
#define NODES_H

struct Node {
    int item;
    Node *next;
};

// Insert value at the front. head changes, so it is passed by reference.
void pushFront(Node *&head, int value);

// Print the items in order, like:  [3 -> 1 -> 4]   (empty chain: [])
void printChain(const Node *head);

// Number of nodes in the chain.
int length(const Node *head);

// true if value is somewhere in the chain.
bool contains(const Node *head, int value);

// Insert value at the end of the chain.
void pushBack(Node *&head, int value);

// Remove the FIRST node holding value. Returns false if there is none.
bool removeFirst(Node *&head, int value);

// Delete every node, and leave head == nullptr.
void deleteChain(Node *&head);

#endif

// LinkedStack.h -- a stack stored as a chain of nodes, after Carrano's
// LinkedStack (the CSS 342 textbook). A class template, so it all lives in this header.
//
// push, pop, peek, and isEmpty are done. Complete the rule of three:
// the destructor, the copy constructor, and the copy assignment operator.
#ifndef LINKED_STACK_H
#define LINKED_STACK_H

template <typename ItemType>
class LinkedStack {
public:
    LinkedStack() : top_(nullptr), count_(0) {}

    // TODO 1: destructor -- delete every node.
    // TODO 2: copy constructor -- a deep copy, with the items in the SAME order.
    // TODO 3: copy assignment operator.

    bool isEmpty() const { return top_ == nullptr; }
    int size() const { return count_; }

    void push(const ItemType &newItem) {
        top_ = new Node{newItem, top_};
        count_++;
    }

    // Removes the top item. Returns false if the stack is empty.
    bool pop() {
        if (isEmpty()) {
            return false;
        }
        Node *doomed = top_;
        top_ = top_->next;
        delete doomed;
        count_--;
        return true;
    }

    // Precondition: the stack is not empty.
    ItemType peek() const {
        return top_->item;
    }

private:
    struct Node {
        ItemType item;
        Node *next;
    };

    Node *top_;
    int count_;
};

#endif

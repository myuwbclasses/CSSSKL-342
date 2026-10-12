// ArrayStack.h -- a fixed-capacity stack. peek and pop must throw when the
// stack is empty (TODO 2), the way Carrano's stacks do.
#ifndef ARRAY_STACK_H
#define ARRAY_STACK_H

#include "PrecondViolatedExcept.h"

template <typename ItemType>
class ArrayStack {
public:
    ArrayStack() : top_(-1) {}

    bool isEmpty() const { return top_ < 0; }

    // Returns false if the stack is full.
    bool push(const ItemType &newEntry) {
        if (top_ == CAPACITY - 1) {
            return false;
        }
        top_++;
        items_[top_] = newEntry;
        return true;
    }

    // TODO 2: throw PrecondViolatedExcept("pop() called on an empty stack")
    //         if the stack is empty.
    void pop() {
        top_--;
    }

    // TODO 2: throw PrecondViolatedExcept("peek() called on an empty stack")
    //         if the stack is empty.
    ItemType peek() const {
        return items_[top_];
    }

private:
    static const int CAPACITY = 5;
    ItemType items_[CAPACITY];
    int top_;
};

#endif

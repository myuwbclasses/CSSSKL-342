// intarray.h -- a growable array of ints that owns its memory.
//
// STARTER CODE: IntArray has a destructor but no copy constructor and no
// operator=, so the compiler writes both for you. copy_test shows why that's
// a problem.
#ifndef INTARRAY_H
#define INTARRAY_H

#include <string>

class IntArray {
public:
    explicit IntArray(int capacity = 4);
    ~IntArray();

    // TODO 1: declare the copy constructor here.
    // TODO 2: declare the copy assignment operator (operator=) here.

    void add(int value);                // grows the array when it's full
    int get(int index) const;           // precondition: 0 <= index < size()
    void set(int index, int value);     // precondition: 0 <= index < size()
    int size() const;
    std::string toString() const;       // like "[1, 2, 3]"

private:
    int *data_;       // owned: allocated with new[], released in the destructor
    int size_;
    int capacity_;
};

#endif

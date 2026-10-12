// counter.h -- returning references from member functions.
//
// The whole class is in this header so you can focus on the two value()
// functions. Complete the TODOs, then build counter_test.
#ifndef COUNTER_H
#define COUNTER_H

class Counter {
public:
    Counter() : count_(0) {}

    // Returns a COPY of the count. The caller cannot change count_ through it.
    int value() {
        return count_;
    }

    // TODO 1: change the function above so it returns a REFERENCE to count_,
    //         so that   c.value() = 4;   and   c.value()++;   change the counter.

    // TODO 2: add a second, const version of value() that returns int, so that
    //         a const Counter can still be read (see counter_test.cpp).

private:
    int count_;
};

#endif

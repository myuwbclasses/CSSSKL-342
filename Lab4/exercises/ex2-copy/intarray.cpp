// intarray.cpp -- IntArray members.

#include "intarray.h"
using namespace std;

IntArray::IntArray(int capacity)
    : data_(new int[capacity]), size_(0), capacity_(capacity) {
}

IntArray::~IntArray() {
    delete[] data_;
}

// TODO 1: define the copy constructor. It must make a DEEP copy: its own new
//         array, with the same capacity, holding copies of other's values.

// TODO 2: define operator=. Four steps: do nothing for self-assignment;
//         copy other's values into a new array; release the old array;
//         return *this.

void IntArray::add(int value) {
    if (size_ == capacity_) {
        int *bigger = new int[capacity_ * 2];
        for (int i = 0; i < size_; i++) {
            bigger[i] = data_[i];
        }
        delete[] data_;
        data_ = bigger;
        capacity_ *= 2;
    }
    data_[size_] = value;
    size_++;
}

int IntArray::get(int index) const {
    return data_[index];
}

void IntArray::set(int index, int value) {
    data_[index] = value;
}

int IntArray::size() const {
    return size_;
}

string IntArray::toString() const {
    string result = "[";
    for (int i = 0; i < size_; i++) {
        if (i > 0) {
            result += ", ";
        }
        result += to_string(data_[i]);
    }
    return result + "]";
}

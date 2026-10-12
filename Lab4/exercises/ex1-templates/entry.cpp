// entry.cpp -- Entry's member definitions. Part B, TODO 1 moves them into
// entry.h and deletes this file.

#include "entry.h"
using namespace std;

Entry::Entry(const string &label, int value) : label_(label), value_(value) {
}

int Entry::getValue() const {
    return value_;
}

void Entry::setValue(int value) {
    value_ = value;
}

bool Entry::operator<(const Entry &other) const {
    return value_ < other.value_;
}

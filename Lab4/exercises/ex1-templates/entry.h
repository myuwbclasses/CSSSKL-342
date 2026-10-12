// entry.h -- an Entry is a label with an int value, like "apples" 12.
// A working, ordinary (not templated) class: entry.cpp has its definitions.
//
// Part B:
// TODO 1: make Entry a class template, Entry<T>, where T is the type of the
//         value (the label stays a std::string). Move the definitions from
//         entry.cpp into this file, below the class, and delete entry.cpp.
// TODO 2: a global operator<< that prints an Entry as label=value, for
//         example apples=12. Entry has no getLabel(), so make operator<< a
//         friend of Entry.
#ifndef ENTRY_H
#define ENTRY_H

#include <string>

class Entry {
public:
    Entry(const std::string &label, int value);
    int getValue() const;
    void setValue(int value);
    bool operator<(const Entry &other) const;   // compares the values

private:
    std::string label_;
    int value_;
};

#endif

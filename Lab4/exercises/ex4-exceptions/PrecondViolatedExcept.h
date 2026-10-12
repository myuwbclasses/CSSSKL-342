// PrecondViolatedExcept.h -- the exception class Carrano's ADTs throw when
// a precondition is broken (for example, peek() on an empty stack).
// Complete; do not change.
#ifndef PRECOND_VIOLATED_EXCEPT_H
#define PRECOND_VIOLATED_EXCEPT_H

#include <stdexcept>
#include <string>

class PrecondViolatedExcept : public std::logic_error {
public:
    explicit PrecondViolatedExcept(const std::string &message = "")
        : std::logic_error("Precondition Violated Exception: " + message) {}
};

#endif

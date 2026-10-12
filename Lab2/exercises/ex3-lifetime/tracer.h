// tracer.h -- a class that announces when its objects are created and destroyed.
#ifndef TRACER_H
#define TRACER_H

#include <string>

class Tracer {
public:
    Tracer(const std::string &name);       // prints "+ name"
    Tracer(const Tracer &other);           // copy constructor: prints "+ copy of name"
    ~Tracer();                             // destructor: prints "- name"
    const std::string &name() const;

private:
    std::string name_;
};

#endif

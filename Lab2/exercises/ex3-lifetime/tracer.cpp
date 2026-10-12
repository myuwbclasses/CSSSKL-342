// tracer.cpp -- Tracer member definitions (complete; do not change).

#include "tracer.h"
#include <iostream>
using namespace std;

Tracer::Tracer(const string &name) : name_(name) {
    cout << "  + " << name_ << endl;
}

Tracer::Tracer(const Tracer &other) : name_("copy of " + other.name_) {
    cout << "  + " << name_ << endl;
}

Tracer::~Tracer() {
    cout << "  - " << name_ << endl;
}

const string &Tracer::name() const {
    return name_;
}

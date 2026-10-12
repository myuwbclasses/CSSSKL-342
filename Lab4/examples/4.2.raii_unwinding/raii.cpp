// raii.cpp -- stack unwinding: when an exception leaves a function, the
// destructors of its local objects run. A raw new has no destructor, so it
// leaks; a unique_ptr is an object whose destructor frees the memory.
#include <iostream>
#include <memory>
#include <stdexcept>
using namespace std;

struct Tracer {
    const char *name;
    explicit Tracer(const char *n) : name(n) { cout << "  make " << name << endl; }
    ~Tracer() { cout << "  destroy " << name << endl; }
};

void work() {
    Tracer local("local");                                  // a local object
    int *raw = new int[100];                                // raw new: only a delete[] frees it
    unique_ptr<int[]> safe = make_unique<int[]>(100);             // freed by safe's destructor
    raw[0] = 1;
    safe[0] = 1;
    throw runtime_error("something failed");                // leaves work() here
    delete[] raw;                                           // never reached
}

int main() {
    try {
        work();
    } catch (const runtime_error &e) {
        cout << "caught: " << e.what() << endl;             // local was destroyed before this
    }
    return 0;
}

// copy.cpp -- Tracer t1(t2) and Tracer t1 = t2 are BOTH copy construction.
//
// Build and run (in VS Code's terminal, attached to your container):
//   g++ -std=c++17 -Wall -Wextra copy.cpp -o copy
//   ./copy
// README.txt in this folder shows the real output.

#include <iostream>
using namespace std;

int nextId = 1;    // each new Tracer gets the next number: #1, #2, ...

class Tracer {
public:
    // Constructor: makes a brand-new object.
    Tracer() : id_(nextId++) {
        cout << "  constructor:      new object #" << id_ << endl;
    }
    // Copy constructor: makes a brand-new object as a copy of an existing one.
    Tracer(const Tracer &other) : id_(nextId++) {
        cout << "  copy constructor: new object #" << id_ << ", copied from #" << other.id_ << endl;
    }
    // Assignment operator: copies into an object that ALREADY exists; no new
    // object is made. (You'll write these yourself later; here it just prints,
    // so you can see when it runs.)
    Tracer &operator=(const Tracer &other) {
        cout << "  assignment:       existing object #" << id_ << " gets the value of #" << other.id_ << endl;
        return *this;
    }
private:
    int id_;
};

int main() {
    cout << "Tracer t2;" << endl;
    Tracer t2;

    cout << "Tracer t1(t2);      // copy construction" << endl;
    Tracer t1(t2);

    cout << "Tracer t3 = t2;     // ALSO copy construction: t3 is being created" << endl;
    Tracer t3 = t2;

    cout << "t3 = t1;            // assignment: t3 already exists" << endl;
    t3 = t1;
    return 0;
}

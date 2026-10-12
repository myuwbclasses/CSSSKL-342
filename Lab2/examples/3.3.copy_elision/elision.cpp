// elision.cpp -- returning a local object by value usually makes NO copy.
//
// Build and run it two ways (in VS Code's terminal, attached to your container):
//   g++ -std=c++17 -Wall -Wextra elision.cpp -o elision
//   ./elision
//   g++ -std=c++17 -Wall -Wextra -fno-elide-constructors elision.cpp -o noelision
//   ./noelision
// The second build turns copy elision off, so you can see the copy it saves.
// README.txt in this folder shows the real output of both.

#include <iostream>
using namespace std;

int nextId = 1;    // each new Tracer gets the next number: #1, #2, ...

class Tracer {
public:
    Tracer() : id_(nextId++) {
        cout << "  constructor:      new object #" << id_ << endl;
    }
    Tracer(const Tracer &other) : id_(nextId++) {
        cout << "  copy constructor: new object #" << id_ << ", copied from #" << other.id_ << endl;
    }
    ~Tracer() {
        cout << "  destructor:       object #" << id_ << endl;
    }
private:
    int id_;
};

// Builds a Tracer in a local variable and returns it by value.
Tracer make() {
    Tracer local;
    return local;
}

int main() {
    cout << "Tracer t = make();" << endl;
    Tracer t = make();
    cout << "main ends" << endl;
    return 0;
}

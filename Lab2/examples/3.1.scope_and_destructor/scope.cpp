// scope.cpp -- objects are destroyed at the end of the { } block they were created in.
//
// Build and run (in VS Code's terminal, attached to your container):
//   g++ -std=c++17 -Wall -Wextra scope.cpp -o scope
//   ./scope
// Before you run it, predict the order of the lines. README.txt in this folder
// shows the real output.

#include <iostream>
#include <string>
using namespace std;

// A class whose constructor and destructor print, so you can see when they run.
class Noisy {
public:
    Noisy(const string &name) : name_(name) {
        cout << "  constructed " << name_ << endl;
    }
    ~Noisy() {
        cout << "  destroyed " << name_ << endl;
    }
private:
    string name_;
};

int main() {
    cout << "main starts" << endl;
    Noisy a("a");

    {                                   // a sub-block: its own scope
        cout << "inner block starts" << endl;
        Noisy b("b");
        Noisy c("c");
        cout << "inner block ends" << endl;
    }                                   // b and c die HERE, in reverse order: c, then b

    cout << "back in main" << endl;
    Noisy d("d");
    cout << "main ends" << endl;
    return 0;
}                                       // d and a die HERE, in reverse order: d, then a

// args.cpp -- command-line arguments: argc counts them, argv holds them.
#include <iostream>
using namespace std;

int main(int argc, char *argv[]) {
    cout << "argc = " << argc << endl;
    for (int i = 0; i < argc; i++) {
        cout << "argv[" << i << "] = " << argv[i] << endl;             // argv[0] is the program
    }

    if (argc != 2) {                                     // check BEFORE using argv[1]
        cerr << "usage: " << argv[0] << " <name>" << endl;             // errors go to cerr
        return 1;                                        // nonzero: "it failed"
    }
    cout << "hello, " << argv[1] << endl;
    return 0;
}

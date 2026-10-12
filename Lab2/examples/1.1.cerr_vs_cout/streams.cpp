// streams.cpp -- cout is the program's real output; cerr is for debug and error messages.
//
// Build and run (in VS Code's terminal, attached to your container):
//   g++ -std=c++17 -Wall -Wextra streams.cpp -o streams
//   ./streams                  both kinds of lines appear on the screen
//   ./streams > out.txt        only the debug line appears; out.txt gets the results
//   ./streams 2> err.txt       only the results appear; err.txt gets the debug line
// README.txt in this folder shows the exact output of each.

#include <iostream>
using namespace std;

int main() {
    cout << "result: 42" << endl;           // real output: goes where > sends it
    cerr << "debug: computing..." << endl;  // debug message: stays on the screen with >
    cout << "result: 99" << endl;
    return 0;
}

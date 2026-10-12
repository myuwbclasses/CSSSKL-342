// crash.cpp -- output sent to cout can be lost when the program crashes.
//
// Build and run (in VS Code's terminal, attached to your container):
//   g++ -std=c++17 -Wall -Wextra crash.cpp -o crash
//   ./crash
// "step 1: about to divide" never appears, even though that line ran before
// the crash. Then try the two fixes below, one at a time, and run again.
// README.txt in this folder shows the exact output of each version.

#include <iostream>
using namespace std;

int divide(int total, int count) {
    return total / count;        // count is 0: the program crashes here
}

int main() {
    cout << "step 1: about to divide";              // no newline, no endl
    // Fix A: end the line with endl, which writes cout's waiting text out now:
    //     cout << "step 1: about to divide" << endl;
    // Fix B: send debug messages to cerr, which is written immediately:
    //     cerr << "step 1: about to divide";
    int result = divide(10, 0);
    cout << "result: " << result << endl;
    return 0;
}

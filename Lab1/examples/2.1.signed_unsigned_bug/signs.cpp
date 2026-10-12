// signs.cpp -- two bugs that come from mixing signed (int) and unsigned types.
//
// Build and run (in VS Code's terminal, attached to your container):
//   g++ -std=c++17 -Wall -Wextra signs.cpp -o signs
//   ./signs
// Read the two warnings g++ prints: they point at exactly these bugs.
// README.txt in this folder shows the real output and the fixes.

#include <iostream>
#include <string>
using namespace std;

int main() {
    string word = "abc";

    // Bug 1: print the indexes of word from last to first, with an unsigned counter.
    // An unsigned int is never negative, so i >= 0 is ALWAYS true: after 0, i-- wraps
    // around to 4294967295 and the loop keeps going. (The step counter stops it for
    // this demo; without it, the loop never ends and word[i] would read far past the
    // end of the string.)
    int steps = 0;
    for (unsigned int i = word.size() - 1; i >= 0; i--) {
        cout << "i = " << i << endl;
        steps++;
        if (steps == 6) {
            cout << "...stopped after 6 steps: this loop never ends on its own" << endl;
            break;
        }
    }

    // Bug 2: compare a negative int with an unsigned size.
    // -1 means "not found". Before comparing, the int is converted to unsigned,
    // so -1 becomes 4294967295 (or larger), which is NOT less than 3.
    int position = -1;
    if (position < word.size()) {
        cout << "position " << position << " is a valid index" << endl;
    } else {
        cout << "position " << position << " is NOT less than " << word.size() << "?!" << endl;
    }
    return 0;
}

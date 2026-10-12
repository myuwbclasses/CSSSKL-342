// words.cpp -- string and vector<string> together, reading the
// file named on the command line:
//     ./words data/lines.txt

#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

// TODO 2: split a line into words, using istringstream and >>.
vector<string> split(const string &line) {
    vector<string> words;
    words.push_back(line);       // placeholder: the whole line as one word
    return words;
}

// TODO 3: join the words with one space between them (no trailing space).
string join(const vector<string> &words) {
    return words.empty() ? "" : words[0];    // placeholder: replace
}

// TODO 4: return a copy of word with its letters reversed.
//         (Hint: build it from word.rbegin() to word.rend(), or loop backward.)
string reversed(const string &word) {
    return word;
}

int main(int argc, char *argv[]) {
    // TODO 1: the file name must be given: if argc isn't 2, print a usage
    //         message to cerr and return 1. Replace this line with that check.
    cout << "argc is " << argc << endl;

    ifstream in(argv[1]);
    // TODO 1 (continued): if the file didn't open (!in), print an error that
    //         names the file to cerr and return 1.

    string line;
    int lineNumber = 0;
    while (getline(in, line)) {
        lineNumber++;
        vector<string> words = split(line);

        // TODO 5: replace each word with its reverse, then print
        //         "<lineNumber> (<line.size()> chars): <word count> words: <joined words>"
        //         for example   1 (22 chars): 4 words: atad serutcurts ni ++C
    }
    return 0;
}

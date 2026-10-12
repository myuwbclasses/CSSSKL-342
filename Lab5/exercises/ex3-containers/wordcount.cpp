// wordcount.cpp -- count how often each word appears, with map.
//
// Usage:   ./wordcount data/sample.txt

#include <cctype>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
using namespace std;

// Lowercases word and strips punctuation from both ends: "Stack," -> "stack".
// Given; do not change.
string normalize(const string &word) {
    size_t start = 0;
    size_t end = word.size();
    while (start < end && !isalnum(static_cast<unsigned char>(word[start]))) {
        start++;
    }
    while (end > start && !isalnum(static_cast<unsigned char>(word[end - 1]))) {
        end--;
    }
    string result;
    for (size_t i = start; i < end; i++) {
        result += static_cast<char>(tolower(static_cast<unsigned char>(word[i])));
    }
    return result;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        cerr << "usage: " << argv[0] << " <filename>" << endl;
        return 1;
    }
    ifstream in(argv[1]);
    if (!in) {
        cerr << "error: cannot open " << argv[1] << endl;
        return 1;
    }

    map<string, int> counts;
    string word;
    while (in >> word) {
        string w = normalize(word);
        if (!w.empty()) {
            // TODO 1: count w. (One line: what does counts[w] do when w is new?)
        }
    }

    // TODO 2: print every word and its count, one per line, as "word: count".
    //         Use a range-based for over the map; each element is a
    //         pair with .first (key) and .second (value). In what order
    //         do they come out?

    // TODO 3: print how many DIFFERENT words there are (counts.size()).

    // TODO 4: look up "queue" and "tree" WITHOUT adding them if missing:
    //         use counts.find(...) and compare with counts.end().
    //         Then print counts.size() again: it must not have changed.

    // TODO 5: find and print the most frequent word and its count.

    return 0;
}

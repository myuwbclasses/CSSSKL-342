// parse_line.cpp -- read whole lines with getline, then take each line
// apart with a istringstream and >>, field by field, in their own types.
// Run:  ./parse_line < people.txt
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main() {
    string line;
    while (getline(cin, line)) {                 // one whole line per pass
        istringstream fields(line);               // a stream that reads from the string
        string name;
        int age;
        double height;
        if (fields >> name >> age >> height) {    // all three fields read: a good line
            cout << name << " is " << age << ", " << height << " m" << endl;
        } else {                                  // missing or wrong fields
            cerr << "bad line: \"" << line << "\"" << endl;
        }
    }
    return 0;
}

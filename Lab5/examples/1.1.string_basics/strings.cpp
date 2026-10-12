// strings.cpp -- string: a class that owns its characters and knows its size.
#include <iostream>
#include <stdexcept>
#include <string>
using namespace std;

int main() {
    string fruit = "pear";
    string other = "pe";
    other += "ar";                                    // += and + join strings
    cout << fruit.size() << " " << fruit[0] << fruit.at(3) << endl;             // 4 pr

    // == and < compare the CHARACTERS (Java's == on strings compares references)
    cout << boolalpha << (fruit == other) << " "
         << (string("apple") < fruit) << endl;                                  // true true

    cout << fruit.substr(1, 2) << endl;               // 2 characters from index 1: ea
    cout << fruit.find("ar") << endl;                 // index where "ar" starts: 2
    if (fruit.find("z") == string::npos) {            // npos: not found
        cout << "no z in " << fruit << endl;
    }

    string label = "item " + to_string(42);           // number -> string
    int n = stoi("17") + 1;                           // string -> int: 18
    cout << label << ", " << n << endl;               // item 42, 18
    try {
        stoi("abc");                                  // not a number
    } catch (const invalid_argument &e) {
        cout << "invalid_argument: " << e.what() << endl;
    }
    return 0;
}

// map_lookup.cpp -- a map from names to phone extensions: insert, look up
// with [] (which ADDS missing keys) and with find (which doesn't), sorted order.
#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
    map<string, int> ext;
    ext["Zoe"] = 4410;                          // [] with = adds or overwrites
    ext["Amir"] = 4102;
    ext.insert({"Mei", 4307});                  // insert adds only if the key is new
    ext.insert({"Mei", 9999});                  // key exists: nothing changes
    cout << "size " << ext.size() << ", Mei " << ext["Mei"] << endl;

    auto found = ext.find("Ravi");              // find just looks
    if (found == ext.end()) {
        cout << "Ravi not found; size still " << ext.size() << endl;
    }
    cout << "ext[\"Ravi\"] is " << ext["Ravi"] << endl;             // [] ADDS Ravi, with 0
    cout << "size now " << ext.size() << endl;

    for (const auto &entry : ext) {             // sorted by key; each entry is a pair
        cout << entry.first << ": " << entry.second << endl;
    }
    return 0;
}

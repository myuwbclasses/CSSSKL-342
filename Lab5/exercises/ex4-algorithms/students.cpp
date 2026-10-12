// students.cpp -- standard algorithms with function pointers and lambdas.
// Complete the TODOs in order.

#include <algorithm>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
using namespace std;

struct Student {
    string name;
    int id;
    double gpa;
};

void printAll(const string &title, const vector<Student> &students) {
    cout << title << ":" << endl;
    for (const Student &s : students) {
        cout << "  " << s.id << " " << s.name << " " << s.gpa << endl;
    }
}

// A comparison function: true when a should come before b.
bool byName(const Student &a, const Student &b) {
    return a.name < b.name;
}

// TODO 1: write byId, ordering by id (smallest first).

// A function-pointer type for comparison functions like byName.
using Compare = bool (*)(const Student &, const Student &);

// TODO 2: sort students with the given comparison function, using sort.
void sortBy(vector<Student> &students, Compare before) {
    (void)students;    // placeholder: remove these two lines
    (void)before;
}

int main() {
    vector<Student> students = {
        {"Mina", 1042, 3.6}, {"Ari", 1007, 2.9}, {"Jordan", 1100, 1.8},
        {"Kai", 1015, 3.9},  {"Lee", 1003, 3.1}, {"Sam", 1050, 1.5},
    };

    // TODO 3: sortBy(students, byName) and print; then sortBy(students, byId)
    //         and print.

    // TODO 4: sort by gpa, highest first, by passing sort a LAMBDA:
    //             [](const Student &a, const Student &b) { return ... ; }
    //         and print.

    // TODO 5: find_if: find the first student (in the current order) with
    //         gpa below 2.0, and print the name (or "none").

    // TODO 6: count_if: how many students have gpa >= 3.0?

    // TODO 7: accumulate: the average gpa. (Start the sum at 0.0, not 0:
    //         see Q4.)

    // TODO 8: a lambda that CAPTURES a local variable: let int minId = 1040;
    //         count the students whose id >= minId with
    //             [minId](const Student &s) { ... }

    // TODO 9: remove every student with gpa below 2.0 with the erase-remove
    //         idiom:
    //             students.erase(remove_if(...), students.end());
    //         and print.

    return 0;
}

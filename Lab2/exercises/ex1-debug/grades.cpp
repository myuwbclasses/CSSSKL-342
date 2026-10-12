// grades.cpp -- prints each student's average and letter grade.
//
// It compiles with no warnings, but it has THREE bugs. Find them with the
// debugger (gdb, then VS Code), not by staring at the code: that is the point
// of Exercise 1. Do not change main().

#include <iostream>
#include <string>
using namespace std;

// Returns the average of `count` scores that add up to `total`.
double average(int total, int count) {
    return total / count;
}

// Returns the letter grade for an average:
//   A: 90 and up,  B: 80 and up,  C: 70 and up,  D: 60 and up,  F: below 60.
char letter(double avg) {
    if (avg >= 90) {
        return 'A';
    } else if (avg >= 80) {
        return 'B';
    } else if (avg > 70) {
        return 'C';
    } else if (avg >= 60) {
        return 'D';
    }
    return 'F';
}

// Prints one student's line: "name: average letter".
// A student with no scores yet (count == 0) should print "name: no scores".
void report(const string &name, int total, int count) {
    cout << "computing " << name << "\n";      // a progress message (see Part 1)
    double avg = average(total, count);
    cout << name << ": " << avg << " " << letter(avg) << "\n";
}

int main() {
    report("Ana", 269, 3);      // expected   Ana: 89.6667 B
    report("Ben", 210, 3);      // expected   Ben: 70 C
    report("Cy", 0, 0);         // expected   Cy: no scores
    report("Dee", 455, 5);      // expected   Dee: 91 A
    cout << "done\n";
    return 0;
}

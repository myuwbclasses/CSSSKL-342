// vectors.cpp -- vector basics. Complete the TODOs in order.

#include <algorithm>
#include <iostream>
#include <stdexcept>
#include <vector>
using namespace std;

// TODO 1: return the average of the values (0.0 for an empty vector).
//         Why is the parameter const vector<int>& ?
double average(const vector<int> &values) {
    return values.empty() ? 0.0 : values[0];    // placeholder: replace
}

// TODO 2: print the values on one line, using a range-based for loop.
void print(const vector<int> &values) {
    cout << values.size() << " values" << endl;              // placeholder: replace
}

int main() {
    vector<int> v = {8, 2, 14, 6, 10};
    cout << "size " << v.size() << ", capacity " << v.capacity() << endl;
    print(v);

    // TODO 3: append five odd numbers (13, 1, 9, 5, 3) with push_back, printing
    //         size and capacity after each one. What pattern do you see?

    // TODO 4: sort v with sort, then print it.

    cout << "average: " << average(v) << endl;

    // TODO 5: print v[1] and v.at(1). Then, inside a try block, print
    //         v.at(100) and catch const out_of_range&. (Do NOT try
    //         v[100]: no check, undefined behavior.)

    // TODO 6: a 3x4 table: vector<vector<int>> with 3 rows of 4
    //         zeros (use the (count, value) constructor). Set table[r][c] to
    //         r * 10 + c and print it as 3 lines.

    return 0;
}

// iterate.cpp -- using iterators on a vector. Complete the TODOs.

#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> v = {3, 8, 1, 6, 9, 7, 2};

    // TODO 1: print v with an explicit iterator loop:
    //             for (vector<int>::iterator it = v.begin(); it != v.end(); ++it)
    //         then rewrite the declaration with auto.

    // TODO 2: double every element by writing through the iterator (*it *= 2).
    //         Print v again.

    // TODO 3: print v backward with rbegin() / rend().

    // TODO 4: remove every element greater than 10 while iterating:
    //             it = v.erase(it);   // erase returns the next valid iterator
    //         and only ++it when you did NOT erase. Print v.
    //         (Q3: what goes wrong if you always ++it after erase?)

    // TODO 5: a const_iterator: write a loop over a const vector<int>&
    //         (cv below). Try to assign through it, read the error, then
    //         remove that line.
    const vector<int> &cv = v;
    (void)cv;

    return 0;
}

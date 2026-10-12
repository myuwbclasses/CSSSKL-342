// arrays.cpp -- C++ arrays: one contiguous block of memory, no length stored
// with it, and no bounds checking. Complete the TODOs in order.
//
// STARTER CODE: the warning about sizeof is on purpose (see step 1 in the
// handout); the unused-parameter warnings go away as you complete the TODOs.

#include <iostream>
using namespace std;

struct Point {
    int x;
    int y;
    Point() : x(0), y(0) {}                    // used for elements you don't initialize
    Point(int px, int py) : x(px), y(py) {}
};

// Given: what does an array parameter really receive? (Step 1.)
void sizeInside(int values[]) {
    cout << "sizeof(values) in a function = " << sizeof(values) << endl;
}

// Given: prints count ints starting at values.
void printArray(const int *values, int count) {
    for (int i = 0; i < count; i++) {
        cout << values[i] << " ";
    }
    cout << endl;
}

// TODO 3: return the sum of the count ints starting at values. Walk the
//         array with a pointer, no []:
//             for (const int *p = values; p < values + count; p++) ...
int sumArray(const int *values, int count) {
    return 0;
}

// TODO 4: reverse the array in place, no []. Use two pointers, one at each
//         end (values and values + count - 1), swap what they point to, and
//         move them toward each other until they meet.
void reverseArray(int *values, int count) {
}

// TODO 5: return a POINTER to the largest element (not its value, not its
//         index). Assume count >= 1.
int *findMax(int *values, int count) {
    return values;              // placeholder: replace
}

// TODO 6: move every point by (dx, dy). Walk with a Point pointer and use ->.
void movePoints(Point *pts, int count, int dx, int dy) {
}

int main() {
    int a[8] = {10, 11, 12, 13, 14, 15, 16, 17};

    cout << "sizeof(a) = " << sizeof(a) << endl;
    cout << "sizeof(a[0]) = " << sizeof(a[0]) << endl;
    sizeInside(a);

    // TODO 1: print the number of elements, computed as sizeof(a) / sizeof(a[0]).
    //         Then print a, &a[0], &a[1], and &a[2], one per line, with labels.

    // TODO 2: point p at a[5] with  int *p = &(a[5]);  then print *p, p[1],
    //         p[-1], p[-2], and *(p - 2), one per line, with labels.

    cout << "sum: " << sumArray(a, 8) << endl;                // 108
    reverseArray(a, 8);
    printArray(a, 8);                                         // 17 16 15 14 13 12 11 10

    int *biggest = findMax(a, 8);
    *biggest = 0;                                             // changes the array itself
    printArray(a, 8);                                         // 0 16 15 14 13 12 11 10

    Point pts[3] = {Point(1, 2), Point(3, 4)};                // pts[2] is Point()
    movePoints(pts, 3, 10, 10);
    for (const Point &pt : pts) {
        cout << "(" << pt.x << ", " << pt.y << ") ";
    }
    cout << endl;                                             // (11, 12) (13, 14) (10, 10)

    // TODO 7: C++ does not check array bounds. Uncomment the loop below: it
    //         runs one step too far. Build, run, and look at r.id. Then run
    //         it under valgrind. Comment the loop out again when you're done.
    struct Record {
        int scores[3];
        int id;
    };
    Record r = {{90, 80, 70}, 1234};
    // for (int i = 0; i <= 3; i++) {
    //     r.scores[i] = 0;
    // }
    cout << "r.id = " << r.id << endl;                        // 1234

    return 0;
}

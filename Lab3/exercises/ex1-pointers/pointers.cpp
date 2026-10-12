// pointers.cpp -- pointer basics: &, *, nullptr, and pointers to structs.
//
// STARTER CODE: this file does not compile as given (see step 1 in the handout).

#include <iostream>
using namespace std;

struct Point {
    int x;
    int y;
};

// Given: prints the int that p points to.
void showThroughPointer(const int *p) {
    cout << "  *p = " << *p << endl;
}

// TODO 1: store value in the int that p points to.
void setThroughPointer(int *p, int value) {
}

// TODO 2: exchange the two ints that a and b point to.
void swapThroughPointers(int *a, int *b) {
}

// TODO 3: return a POINTER to whichever of the two ints is larger (a if
//         they are equal): return the pointer itself, not the value.
int *largerOf(int *a, int *b) {
    return a;                   // placeholder: replace
}

// TODO 4: move the point by (dx, dy). Use the -> operator.
void movePoint(Point *p, int dx, int dy) {
}

int main() {
    int a = 5;
    int *p = &a;

    // TODO 5: print a, &a, p, *p, and &p, one per line, with labels.

    showThroughPointer(a);      // does not compile: fix the CALL, not the function

    setThroughPointer(p, 42);
    cout << "after setThroughPointer: a = " << a << endl;

    *p = *p + 1;
    cout << "after *p = *p + 1: a = " << a << endl;

    int b = 7;
    swapThroughPointers(&a, &b);
    cout << "after swap: a = " << a << ", b = " << b << endl;

    int x = 4;
    int y = 9;
    int *bigger = largerOf(&x, &y);
    *bigger = 0;                // changes y itself
    cout << "after *bigger = 0: x = " << x << ", y = " << y << endl;

    Point pt = {1, 2};
    movePoint(&pt, 10, 20);
    cout << "point: (" << pt.x << ", " << pt.y << ")" << endl;

    int *nothing = nullptr;
    // TODO 6: call showThroughPointer(nothing), run, and record what happens
    //         (Q4). Then remove the call again.
    (void)nothing;

    return 0;
}

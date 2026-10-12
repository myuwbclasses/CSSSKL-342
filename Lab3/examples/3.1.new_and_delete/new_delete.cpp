// new_delete.cpp -- stack vs. heap: new/delete, new[]/delete[], initializing, who releases what.
#include <iostream>
using namespace std;

struct Point {
    int x, y;
    Point(int px, int py) : x(px), y(py) { cout << "  Point(" << x << ", " << y << ")" << endl; }
    ~Point() { cout << "  ~Point(" << x << ", " << y << ")" << endl; }
};

void print(const int *values, int count) {      // only READS values: the caller still owns it
    for (int i = 0; i < count; i++) {
        cout << values[i] << " ";
    }
    cout << endl;
}

void printAndRelease(int *values, int count) {  // RELEASES values: the caller must not use it again
    print(values, count);
    delete[] values;
    values = nullptr;                           // clears only this function's copy of the address
}

int main() {
    int local[3] = {1, 2, 3};                   // 1. on the stack: freed automatically at main's }
    print(local, 3);

    int *num = new int(5);                      // 2. ONE element on the heap: an int set to 5,
    int *one = new int;  *one = 42;             //    an int with no initializer (garbage until set),
    Point *pt = new Point(1, 2);                //    and a Point
    cout << "*num = " << *num << ", *one = " << *one << ", pt->x = " << pt->x << endl;
    delete num;  num = nullptr;                 //    one new, one delete (no []), then nullptr
    delete one;  one = nullptr;
    delete pt;   pt = nullptr;                  //    delete runs ~Point(), then frees the memory

    int *four = new int[4]{10, 20, 30, 40};     // 3. a heap array: list its values,
    int n = 5;
    int *zeros = new int[n]();                  //    or size it with a variable; () makes them all 0,
    int *squares = new int[n];                  //    or no initializer: garbage until you set them
    for (int i = 0; i < n; i++) {
        squares[i] = i * i;
    }

    print(four, 4);                             // 4. pass to a function: only the address travels
    print(zeros, n);
    delete[] four;   four = nullptr;            // 5. released in main, where allocated, after the calls
    delete[] zeros;  zeros = nullptr;
    printAndRelease(squares, n);                // 6. or released inside a function instead,
    squares = nullptr;                          //    so main must clear ITS copy of the address too
    return 0;
}

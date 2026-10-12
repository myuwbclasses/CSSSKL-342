// growing.cpp -- new[] and delete[]: arrays whose size is decided while the
// program runs, and an array that grows. Complete the TODOs.
//
// STARTER CODE: complete TODOs 1 and 2 BEFORE running: until then, the
// program follows a nullptr and writes past the end of an array.

#include <iostream>
using namespace std;

// Given: prints count ints starting at values.
void printArray(const int *values, int count) {
    for (int i = 0; i < count; i++) {
        cout << values[i] << " ";
    }
    cout << endl;
}

// TODO 1: return a NEW array of n ints holding 0, 1, 4, 9, ... (i * i).
//         The caller owns the array and must delete[] it.
int *makeSquares(int n) {
    return nullptr;
}

// TODO 2: grow a dynamic array.
//   - allocate a new array of newCapacity ints with new[]
//   - copy the first count values into it
//   - delete[] the old array
//   - point data at the new array, and set capacity = newCapacity
// data is a REFERENCE to the caller's pointer, so the caller sees the change.
void grow(int *&data, int &capacity, int count, int newCapacity) {
}

int main() {
    int n = 6;                        // could come from the user: known only at run time
    int *squares = makeSquares(n);
    printArray(squares, n);           // 0 1 4 9 16 25

    // TODO 3: release squares, and set the pointer to nullptr.

    // A dynamic array that grows as values are added, like Carrano's
    // resizable ArrayBag.
    int capacity = 2;
    int count = 0;
    int *data = new int[capacity];
    for (int v = 10; v <= 100; v += 10) {
        if (count == capacity) {
            grow(data, capacity, count, capacity * 2);
            cout << "grew to " << capacity << endl;
        }
        data[count] = v;
        count++;
    }
    printArray(data, count);          // 10 20 ... 100

    // TODO 4: release data, and set the pointer to nullptr.

    return 0;
}

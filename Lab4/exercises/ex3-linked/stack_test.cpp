// stack_test.cpp -- tests for LinkedStack. Run it under valgrind too.
// Uncomment each part once the matching TODO is done.

#include <iostream>
#include <string>
#include "LinkedStack.h"
using namespace std;

// Prints from top to bottom by popping a COPY, so the original is untouched.
template <typename T>
void printStack(const string &label, LinkedStack<T> s) {         // by value: copies
    cout << label << " (top first):";
    while (!s.isEmpty()) {
        cout << " " << s.peek();
        s.pop();
    }
    cout << endl;
}

int main() {
    LinkedStack<int> a;
    for (int i = 1; i <= 4; i++) {
        a.push(i * 10);
    }
    cout << "size of a: " << a.size() << ", top: " << a.peek() << endl;             // 4, 40

    // ---- Part 1: destructor (valgrind: no leaks at the end of main)

    // ---- Part 2: copy constructor
    // printStack("a", a);                 // a (top first): 40 30 20 10
    // printStack("a again", a);           // unchanged: 40 30 20 10
    // LinkedStack<int> b = a;
    // b.pop();
    // b.push(99);
    // printStack("b", b);                 // b (top first): 99 30 20 10
    // printStack("a", a);                 // a (top first): 40 30 20 10
    //
    // LinkedStack<int> empty;
    // LinkedStack<int> emptyCopy = empty;
    // cout << "emptyCopy size: " << emptyCopy.size() << endl;             // 0

    // ---- Part 3: copy assignment
    // LinkedStack<string> words;
    // words.push("tree");
    // words.push("queue");
    // LinkedStack<string> other;
    // other.push("old");
    // other = words;
    // other = other;                      // self-assignment
    // printStack("other", other);         // other (top first): queue tree
    // other = LinkedStack<string>();      // assign an empty stack
    // cout << "other size: " << other.size() << endl;             // 0
    return 0;
}

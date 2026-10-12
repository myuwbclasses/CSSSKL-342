// throw_catch.cpp -- throw an exception, catch it by const &, most specific
// handler first, and what happens when nobody catches it.
#include <iostream>
#include <stdexcept>
using namespace std;

int divide(int a, int b) {
    if (b == 0) {
        throw invalid_argument("divide by zero");        // leaves divide() right here
    }
    // You CAN throw for anything, not just errors: uncomment this and
    // average(10, 2) throws a runtime_error, which the exception handler
    // in main catches. Don't: that's an abuse of exceptions. Throw only for a
    // real error, never as an ordinary "return" or a way out of a loop.
    // if (b == 2) {
    //     throw runtime_error("no error but b == 2");
    // }
    return a / b;
}

// A layer between main and divide. When divide throws, average stops too:
// "back from divide" is not printed, and average returns nothing. The
// exception leaves EVERY function between the throw and the matching catch
// (their locals are destroyed on the way out) and lands in main's catch.
int average(int total, int count) {
    cout << "  average: calling divide" << endl;
    int result = divide(total, count);
    cout << "  average: back from divide" << endl;
    return result;
}

int main() {
    try {
        cout << average(10, 2) << endl;                  // 5
        cout << average(1, 0) << endl;                   // throws two calls down: the rest of this try is skipped
        cout << "never printed" << endl;
    } catch (const invalid_argument &e) {                // most specific handler first
        cout << "invalid_argument: " << e.what() << endl;
    } catch (const exception &e) {                       // then the base class of all of them
        cout << "exception: " << e.what() << endl;
    }

    try {
        throw out_of_range("index 7");                   // not an invalid_argument,
    } catch (const invalid_argument &e) {
        cout << "invalid_argument: " << e.what() << endl;
    } catch (const exception &e) {                       // so the base-class handler catches it
        cout << "exception: " << e.what() << endl;
    }

    cout << "now one that nobody catches:" << endl;
    average(1, 0);                                       // no try: the program is aborted
    cout << "never printed" << endl;
    return 0;
}

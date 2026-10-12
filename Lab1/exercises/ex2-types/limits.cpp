// limits.cpp -- explore the ranges of the built-in numeric types.
// Complete each TODO, run the program, and answer the questions in answers.txt.

#include <iostream>
#include <limits>
using namespace std;

// How to read  std::numeric_limits<int>::min()  piece by piece. (This file has
// using namespace std; so the code below writes just numeric_limits<int>::min().)
//
//   std::            The standard library's namespace (see main.cpp in
//                    Exercise 1). Everything from <limits> lives in std.
//   numeric_limits   A "template": a recipe that the standard library uses to
//                    describe ANY numeric type. By itself it isn't complete; it
//                    needs to be told which type you're asking about.
//   <int>            Fills in that type. numeric_limits<int> describes int,
//                    numeric_limits<double> describes double, and so on. The
//                    angle brackets hold a TYPE, not a value. (Java does the
//                    same with ArrayList<Integer>; you'll write your own
//                    templates in Lab 4.)
//   ::               "The thing on the right belongs to the thing on the left."
//                    It reaches INTO a namespace (std::cout) or a type
//                    (numeric_limits<int>::min). Compare with the dot, which
//                    reaches into an OBJECT (s.size()); here there is no object.
//   min()            A function that belongs to numeric_limits<int>: it returns
//                    the smallest int. The () call it, like any function.
//
// Summary:
//   Inside the std namespace there is numeric_limits. You can think of it as
//   a smaller space inside std (strictly speaking, it is a type, not a
//   namespace; Lab 2 explains the difference). <int> selects the
//   numeric_limits for the int type, and min() is a function defined inside
//   numeric_limits<int>. So the whole expression means "in the standard
//   library, the numeric limits of int, call min()". Java's equivalent is
//   Integer.MIN_VALUE.
//
// Note:
//   min is a common function name. Because this one lives inside std and
//   inside numeric_limits<int>, it cannot collide with other functions named
//   min, such as std::min (which returns the smaller of two values) or a
//   min() you write yourself.

int main() {
    // Part A: the range of each type.
    cout << "int:      " << numeric_limits<int>::min() << " to "
         << numeric_limits<int>::max() << endl;
    // TODO: print the same line for unsigned int, long, and long long.
    // TODO: for float and double, print lowest(), max(), and epsilon().
    //       (For floating-point types, min() means something different from
    //       int's min() -- print it too and find out what.)

    // Part B: what happens at the edges?
    unsigned int u = 0;
    u = u - 1;
    cout << "unsigned 0 - 1 = " << u << endl;

    // TODO: print 7 / 2, 7 % 2, -7 / 2, and static_cast<double>(7) / 2.

    // TODO: print whether 0.1 + 0.2 == 0.3 (use boolalpha), then print
    //       0.1 + 0.2 with cout.precision(17).

    int big = 2000000000;
    long long product = big * 2;   // look closely at this line
    cout << "big * 2 = " << product << endl;
    // TODO: change ONE thing on the line above so product is 4000000000.

    return 0;
}

// main.cpp -- prints a small temperature table using the convert and report modules.

// #include <...> (angle brackets): a header from the standard library or the
//   system. The compiler searches only the system include directories.
// #include "..." (quotes): one of YOUR headers. The compiler searches the
//   folder of the file doing the including first, then the system directories.
#include <iostream>
#include "convert.h"
#include "report.h"

// Everything in the standard library is in the namespace std, so the full
// name of cout is std::cout. "using namespace std;" lets this file write just
// cout; both forms appear below. Never write "using namespace std;" in a
// header: it would apply to every file that includes that header.
using namespace std;

int main() {
    unsigned int rows = 5;
    for (int i = 0; i < rows; i++) {
        printRow(i * 25.0);
    }

    cout << "98.6 F = " << fahrenheitToCelsius(98.6) << " C" << endl;
    std::cout << "-300 C is below absolute zero: " << celsiusToFahrenheit(-300.0) << " F" << std::endl;

    // Convert temperatures typed by the user, until they enter -999.
    // - Comparing a double with != is safe here: -999 is a whole number,
    //   stored exactly. (Part 2 explains why == on COMPUTED doubles is not.)
    // - If you type something that is not a number, cin stops reading and the
    //   loop never ends: press Ctrl+C. Lab 5 shows how to handle bad input.
    double fahrenheit = 0.0;
    cout << "Enter a temperature in F (-999 to quit): ";
    cin >> fahrenheit;
    while (fahrenheit != -999) {
        cout << fahrenheit << " F = " << fahrenheitToCelsius(fahrenheit) << " C" << endl;
        cout << "Enter a temperature in F (-999 to quit): ";
        cin >> fahrenheit;
    }
    cout << endl << "Bye!" << endl;
    return 0;
}

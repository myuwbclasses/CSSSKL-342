// temps.cpp -- Exercise 1's temperature program, with everything in ONE file.
//
// Exercise 1 splits this program into main.cpp, convert.h/.cpp, and report.h/.cpp.
// This version puts all of it here: no headers, no Makefile. It prints exactly the
// same output -- the organization of the code doesn't change what the program does.
// README.txt in this folder compares the two.
//
// Build and run (in VS Code's terminal, attached to your container):
//   g++ -std=c++17 -Wall -Wextra temps.cpp -o temps
//   ./temps

#include <iostream>
using namespace std;

// ---------------------------------------------------------------- was convert.cpp

// Nothing can be colder than absolute zero (-273.15 C), so lower
// temperatures are raised to it.
double clampToAbsoluteZero(double celsius) {
    if (celsius < -273.15) {
        return -273.15;
    }
    return celsius;
}

double celsiusToFahrenheit(double celsius) {
    celsius = clampToAbsoluteZero(celsius);
    return celsius * 9.0 / 5.0 + 32.0;
}

double fahrenheitToCelsius(double fahrenheit) {
    return (fahrenheit - 32.0) * 5.0 / 9.0;
}

// ---------------------------------------------------------------- was report.cpp

// Prints the Celsius temperature and its Fahrenheit equivalent on one line.
void printRow(double celsius) {
    cout << celsius << " C = " << celsiusToFahrenheit(celsius) << " F" << endl;
}

// ---------------------------------------------------------------- was main.cpp

int main() {
    int rows = 5;
    for (int i = 0; i < rows; i++) {
        printRow(i * 25.0);
    }

    cout << "98.6 F = " << fahrenheitToCelsius(98.6) << " C" << endl;
    cout << "-300 C is below absolute zero: " << celsiusToFahrenheit(-300.0) << " F" << endl;

    // Convert temperatures typed by the user, until they enter -999.
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

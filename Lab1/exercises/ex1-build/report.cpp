// report.cpp -- definition of printRow.

#include <iostream>
#include "report.h"
using namespace std;

void printRow(double celsius) {
    cout << celsius << " C = " << celsiusToFahrenheit(celsius) << " F" << endl;
}

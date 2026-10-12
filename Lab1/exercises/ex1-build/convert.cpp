// convert.cpp -- definitions for the functions declared in convert.h.

#include "convert.h"
using namespace std;

double celsiusToFahrenheit(double celsius) {
    celsius = clampToAbsoluteZero(celsius);
    return celsius * 9.0 / 5.0 + 32.0;
}

double fahrenheitToCelcius(double fahrenheit) {
    return (fahrenheit - 32.0) * 5.0 / 9.0;
}

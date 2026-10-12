// convert.h -- declarations for temperature conversion functions.
//
// STARTER CODE: this project does NOT build as given. Your job in
// Exercise 1 is to find and fix the build errors (see the handout).

// Nothing can be colder than absolute zero (-273.15 C), so lower
// temperatures are raised to it.
double clampToAbsoluteZero(double celsius) {
    if (celsius < -273.15) {
        return -273.15;
    }
    return celsius;
}

double celsiusToFahrenheit(double celsius);
double fahrenheitToCelsius(double fahrenheit);

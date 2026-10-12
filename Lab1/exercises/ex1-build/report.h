// report.h -- prints one row of a temperature table.

// #pragma once: tells the compiler "paste this file into a .cpp at most once".
// It does the same job as an #ifndef/#define/#endif include guard, in one line,
// with no macro name to invent (and no risk of two headers picking the same
// name). It is not in the C++ standard, but g++, clang, and Visual C++ all
// support it. This header is protected; convert.h is not -- that's for you.
#pragma once

#include "convert.h"

// Prints the Celsius temperature and its Fahrenheit equivalent on one line.
void printRow(double celsius);

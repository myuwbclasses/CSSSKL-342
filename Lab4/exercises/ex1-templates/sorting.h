// sorting.h -- swap, sort (a bubble sort), and print for int arrays.
//
// TODO (Part A): turn all three functions into function templates so they
// work for any type T that has operator< (for sorting) and operator<< (for
// printing). Keep them in this header.
#ifndef SORTING_H
#define SORTING_H

#include <iostream>

void mySwap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

void sortArray(int values[], int count) {
    for (int pass = 0; pass < count - 1; pass++) {
        for (int i = 0; i < count - 1 - pass; i++) {
            if (values[i + 1] < values[i]) {
                mySwap(values[i], values[i + 1]);
            }
        }
    }
}

void printArray(const int values[], int count) {
    for (int i = 0; i < count; i++) {
        std::cout << values[i] << " ";
    }
    std::cout << std::endl;
}

#endif

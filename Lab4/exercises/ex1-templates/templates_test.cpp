// templates_test.cpp -- tests for the sorting templates (Part A) and the
// Entry class template (Part B). Uncomment each block when its step is done.

#include <iostream>
#include <string>
#include "entry.h"
#include "sorting.h"
using namespace std;

int main() {
    // ---- Part A: function templates
    int ints[] = {42, 7, 19, 3, 25};
    sortArray(ints, 5);
    printArray(ints, 5);                 // 3 7 19 25 42

    // double doubles[] = {2.5, -1.0, 3.25, 0.5};
    // sortArray(doubles, 4);
    // printArray(doubles, 4);           // -1 0.5 2.5 3.25

    // string words[] = {"pear", "apple", "fig", "banana"};
    // sortArray(words, 4);
    // printArray(words, 4);             // apple banana fig pear

    // ---- Your templates on your own class: Entry already has operator<
    // ---- (but no operator<< yet, so print the values with getValue)
    // Entry fruit[] = {{"pears", 7}, {"figs", 3}, {"kiwis", 12}};   // TODO 1: make this Entry<int>
    // sortArray(fruit, 3);              // T is Entry: sortArray calls Entry::operator<
    // for (int i = 0; i < 3; i++) {
    //     cout << fruit[i].getValue() << " ";
    // }
    // cout << endl;                     // 3 7 12

    // ---- Part B: the Entry class
    Entry apples("apples", 12);          // TODO 1: once Entry is a template, make this Entry<int>
    apples.setValue(apples.getValue() + 1);
    cout << apples.getValue() << endl;              // 13

    // ---- TODO 1: the same class template, other types for T
    // Entry<double> price("pear", 0.75);
    // Entry<string> nickname("Ann", "annie");
    // cout << price.getValue() << " " << nickname.getValue() << endl;             // 0.75 annie

    // ---- TODO 2: operator<<
    // Entry<int> figs("figs", 3);
    // cout << boolalpha << (figs < apples) << " " << (apples < figs) << endl;                  // true false
    // cout << figs << " " << apples << " " << price << " " << nickname << endl;              // figs=3 apples=13 pear=0.75 Ann=annie

    // ---- Last: arrays of Entry, printed and sorted by your Part A templates
    // Entry<int> stock[] = {{"pears", 7}, {"figs", 3}, {"kiwis", 12}, {"limes", 5}};
    // printArray(stock, 4);             // pears=7 figs=3 kiwis=12 limes=5
    // sortArray(stock, 4);
    // printArray(stock, 4);             // figs=3 limes=5 pears=7 kiwis=12
    //
    // Entry<string> nicknames[] = {{"Ann", "zed"}, {"Bo", "amy"}, {"Cy", "max"}};
    // sortArray(nicknames, 3);
    // printArray(nicknames, 3);         // Bo=amy Cy=max Ann=zed
    return 0;
}

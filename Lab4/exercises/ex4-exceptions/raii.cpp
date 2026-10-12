// raii.cpp -- an exception can skip your delete.
//
// Run under valgrind:  valgrind --leak-check=full ./raii
// Then fix total() with unique_ptr (TODO 4) so nothing leaks, even
// when validate() throws.

#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
using namespace std;

int validate(int score) {
    if (score < 0 || score > 100) {
        throw invalid_argument("bad score " + to_string(score));
    }
    return score;
}

int total(const int *raw, int count) {
    int *checked = new int[count];
    for (int i = 0; i < count; i++) {
        checked[i] = validate(raw[i]);
    }
    int sum = 0;
    for (int i = 0; i < count; i++) {
        sum += checked[i];
    }
    delete[] checked;
    return sum;
}

int main() {
    int good[] = {90, 80, 70};
    int bad[] = {90, -5, 70};

    try {
        cout << "good total: " << total(good, 3) << endl;
        cout << "bad total: " << total(bad, 3) << endl;
    } catch (const invalid_argument &e) {
        cout << "caught: " << e.what() << endl;
    }
    return 0;
}

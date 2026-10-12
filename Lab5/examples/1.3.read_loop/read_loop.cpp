// read_loop.cpp -- open a file named on the command line, and read it with the
// right loop and with the classic wrong one.     Run:  ./read_loop nums.txt
#include <fstream>
#include <iostream>
using namespace std;

int main(int argc, char *argv[]) {
    if (argc != 2) {
        cerr << "usage: " << argv[0] << " <file>" << endl;
        return 1;
    }
    ifstream in(argv[1]);
    if (!in) {                                   // the file didn't open
        cerr << "cannot open " << argv[1] << endl;
        return 1;
    }

    int value;
    int count = 0;
    while (in >> value) {                        // RIGHT: the read itself is the test
        count++;
    }
    cout << "while (in >> value): " << count << " values" << endl;

    ifstream again(argv[1]);                     // read the same file again, the WRONG way
    count = 0;
    while (!again.eof()) {                       // eof() turns true only AFTER a read fails,
        again >> value;                          // so the last read fails, and it's counted too
        count++;
    }
    cout << "while (!in.eof()):   " << count << " values" << endl;
    return 0;
}

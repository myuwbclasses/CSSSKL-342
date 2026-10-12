// lifetime.cpp -- when are objects created and destroyed?
//
// BEFORE you run this program, write down in predictions.txt the exact
// lines you expect each scenario to print. Then run it and compare.

#include <iostream>
#include "tracer.h"
using namespace std;

Tracer global("global");

void byValue(Tracer t) {
    cout << "  in byValue(" << t.name() << ")" << endl;
}

void byConstRef(const Tracer &t) {
    cout << "  in byConstRef(" << t.name() << ")" << endl;
}

Tracer make(const string &name) {
    Tracer t(name);
    return t;
}

// A class with two Tracer members. Note the ORDER of the members below
// and the order of the initializer list.
class Pair {
public:
    Pair() : second_("second"), first_("first") {
        cout << "  Pair constructor body" << endl;
    }
    ~Pair() {
        cout << "  Pair destructor body" << endl;
    }

private:
    Tracer first_;
    Tracer second_;
};

int main() {
    cout << "main starts" << endl;

    cout << "1: a block" << endl;
    {
        Tracer a("a");
        Tracer b("b");
        cout << "  end of block" << endl;
    }

    cout << "2: pass by value, then by const reference" << endl;
    Tracer c("c");
    byValue(c);
    byConstRef(c);

    cout << "3: return by value" << endl;
    Tracer d = make("d");

    cout << "4: a temporary (an object with no name)" << endl;
    Tracer("temp");
    cout << "  next statement" << endl;

    cout << "5: an object with object members" << endl;
    {
        Pair p;
    }

    cout << "main ends" << endl;
    return 0;
}

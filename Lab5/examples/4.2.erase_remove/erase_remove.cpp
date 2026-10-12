// erase_remove.cpp -- remove_if only moves the kept elements to the front;
// erase is what actually shortens the vector.
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

void show(const char *label, const vector<int> &v) {
    cout << label << " (size " << v.size() << "):";
    for (int n : v) { cout << " " << n; }
    cout << endl;
}

int main() {
    vector<int> v = {1, 2, 3, 4, 5, 6};
    show("start       ", v);

    auto newEnd = remove_if(v.begin(), v.end(), [](int n) { return n % 2 == 0; });
    show("remove_if   ", v);           // odd numbers moved forward; same size, leftovers at the end
    cout << "kept " << (newEnd - v.begin()) << " elements" << endl;

    v.erase(newEnd, v.end());          // now really remove the leftovers
    show("after erase ", v);
    return 0;
}

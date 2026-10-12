// objects.cpp -- an array of objects holds real objects, all created with the array.
#include <iostream>
using namespace std;

class Point {
public:
    Point() : x_(0), y_(0) { cout << "  Point()" << endl; }
    Point(int x, int y) : x_(x), y_(y) { cout << "  Point(" << x << ", " << y << ")" << endl; }
    int x() const { return x_; }
    int y() const { return y_; }
    void moveBy(int dx, int dy) { x_ += dx; y_ += dy; }

private:
    int x_;
    int y_;
};

int main() {
    cout << "Point pts[3]; makes:" << endl;
    Point pts[3];                                   // three objects, default constructor for each
    cout << "pts[1] = Point(7, 8); makes:" << endl;
    pts[1] = Point(7, 8);                           // set an element: a new Point, copied into pts[1]

    cout << "Point more[3] = {Point(1, 2), Point(3, 4)}; makes:" << endl;
    Point more[3] = {Point(1, 2), Point(3, 4)};     // the third one gets Point()

    more[1].moveBy(10, 10);                         // an element is an object: use .
    Point *pp = &more[2];
    pp->moveBy(5, 5);                               // through a pointer to an element: use ->

    cout << "pts:  ";
    for (int i = 0; i < 3; i++) {
        cout << "(" << pts[i].x() << ", " << pts[i].y() << ") ";
    }
    cout << endl << "more: ";
    for (int i = 0; i < 3; i++) {
        cout << "(" << more[i].x() << ", " << more[i].y() << ") ";
    }
    cout << endl;
    return 0;
}

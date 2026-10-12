2.2.array_of_objects -- an array of objects holds real objects

Build and run (in the container):
    g++ -std=c++17 -Wall -Wextra objects.cpp -o objects
    ./objects

Output (g++ 11, cssimages/linuxlab):
    Point pts[3]; makes:
      Point()
      Point()
      Point()
    pts[1] = Point(7, 8); makes:
      Point(7, 8)
    Point more[3] = {Point(1, 2), Point(3, 4)}; makes:
      Point(1, 2)
      Point(3, 4)
      Point()
    pts:  (0, 0) (7, 8) (0, 0)
    more: (1, 2) (13, 14) (5, 5)

- Point pts[3]; runs the default constructor three times: the array IS three
  Point objects, side by side, created the moment the array is.
- pts[1] = Point(7, 8); makes a new Point and copies it into pts[1] (copy
  assignment, Lab 2). The array still has exactly three objects.
- With an initializer list, any element left out gets Point(). No default
  constructor would mean a compile error there.
- An element is an object (more[1].moveBy); through a pointer to an element,
  use -> (pp->moveBy).

In Java, new Point[3] makes three null references and no Point objects.

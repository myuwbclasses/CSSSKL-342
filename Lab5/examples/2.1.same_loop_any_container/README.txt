2.1.same_loop_any_container -- one iterator loop for a vector, a list, and a string

Build and run (in the container):
    g++ -std=c++17 -Wall -Wextra same_loop.cpp -o same_loop
    ./same_loop

Output (g++ 11, cssimages/linuxlab):
    3 1 4
    10 50 90
    cba

valgrind: no errors, no leaks.

- for (auto it = c.begin(); it != c.end(); ++it): begin() is the first
  element, end() is ONE PAST the last (never dereference it), *it is the
  element, ++it moves to the next one. The same four operations work on
  every container, whatever is underneath: an array for vector and string,
  linked nodes for list.
- *it = *it * 10; writes through the iterator, changing the list itself.
- for (int n : l) is shorthand for exactly that loop.
- rbegin()/rend() walk backward: "abc" prints as cba.
- The loop tests != rather than <: a list's iterator has no <, only == and !=.

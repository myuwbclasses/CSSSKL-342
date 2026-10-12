2.2.pre_post_increment -- ++c and c++ on your own class

Build and run (in the container):
    g++ -std=c++17 -Wall -Wextra increment.cpp -o increment
    ./increment

Output (g++ 11, cssimages/linuxlab):
    after a = ++c: a = 6, c = 6
    after b = c++: b = 6, c = 7

valgrind: no errors, no leaks.

  Counter &operator++()       pre-increment, ++c: change the object, then
                              return the object itself (*this, by reference)
  Counter operator++(int)     post-increment, c++: the int parameter is never
                              used; it only tells the compiler "postfix". Save
                              a copy, change the object, return the OLD copy
                              (by value: the copy is a local)

So a = ++c gets the new value (6), and b = c++ gets the old value (6) while c
moves on to 7. Post-increment makes an extra copy, which is why loops write
++it. An iterator class overloads the same two operators, the same way, to
move to the next element.

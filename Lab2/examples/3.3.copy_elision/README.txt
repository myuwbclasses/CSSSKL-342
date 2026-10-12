3.3.copy_elision -- returning a local object by value makes no copy

make() builds a Tracer in a local variable and returns it by value. Output from
the course image (cssimages/linuxlab):

$ g++ -std=c++17 -Wall -Wextra elision.cpp -o elision
$ ./elision
Tracer t = make();
  constructor:      new object #1
main ends
  destructor:       object #1

Only ONE object is ever made. The compiler builds make()'s local variable
directly in t's place, so there is nothing to copy. This is copy elision.

Now turn it off, to see the copy it saved:

$ g++ -std=c++17 -Wall -Wextra -fno-elide-constructors elision.cpp -o noelision
$ ./noelision
Tracer t = make();
  constructor:      new object #1
  copy constructor: new object #2, copied from #1
  destructor:       object #1
main ends
  destructor:       object #2

Without elision: the local (#1) is built, copied into t (#2), and destroyed when
make() returns.

What this means for you:
  - Returning objects by value is cheap; write  Tracer make()  without worry.
    (Never return a reference to a local instead -- it would dangle.)
  - Don't put work your program depends on inside a copy constructor and expect
    it to run on return: the compiler is allowed to skip it, and g++ does.
  - Since C++17, elision is GUARANTEED when you return an unnamed temporary
    (return Tracer();); for a named local, as here, it is allowed and g++ does it.

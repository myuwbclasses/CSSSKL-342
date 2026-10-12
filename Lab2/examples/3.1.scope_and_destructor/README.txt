3.1.scope_and_destructor -- when objects are created and destroyed

scope.cpp has a class, Noisy, whose constructor and destructor print a line,
and a { } sub-block inside main. Output from the course image (cssimages/linuxlab):

$ g++ -std=c++17 -Wall -Wextra scope.cpp -o scope
$ ./scope
main starts
  constructed a
inner block starts
  constructed b
  constructed c
inner block ends
  destroyed c          <- the closing } of the inner block
  destroyed b
back in main
  constructed d
main ends
  destroyed d          <- the closing } of main
  destroyed a

What to notice:
  - An object is created where it is defined, and destroyed automatically at the
    closing } of the block it was defined in. Nobody calls the destructor.
  - The inner block's objects are gone before "back in main" prints.
  - Objects in the same block are destroyed in REVERSE order: last created,
    first destroyed (c before b, d before a).
  - a lives for all of main: it is destroyed only after "main ends".

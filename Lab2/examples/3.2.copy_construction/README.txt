3.2.copy_construction -- Tracer t1(t2) vs. Tracer t1 = t2 vs. t1 = t2

copy.cpp gives every new Tracer a number (#1, #2, ...) and prints which
constructor or operator runs. Output from the course image (cssimages/linuxlab):

$ g++ -std=c++17 -Wall -Wextra copy.cpp -o copy
$ ./copy
Tracer t2;
  constructor:      new object #1
Tracer t1(t2);      // copy construction
  copy constructor: new object #2, copied from #1
Tracer t3 = t2;     // ALSO copy construction: t3 is being created
  copy constructor: new object #3, copied from #1
t3 = t1;            // assignment: t3 already exists
  assignment:       existing object #3 gets the value of #2

The key point:
  Tracer t3 = t2;  is NOT assignment, even though it has an = sign. It
  DECLARES t3, so a new object is being created, and creating an object is
  always a constructor's job: here, the copy constructor. It means exactly the
  same as  Tracer t3(t2);
  Only  t3 = t1;  -- where t3 already exists -- is assignment.

Rule of thumb: if the line starts with a type (Tracer t3 = ...), an object is
being created and a constructor runs. If it doesn't (t3 = ...), an existing
object is changed and the assignment operator runs.

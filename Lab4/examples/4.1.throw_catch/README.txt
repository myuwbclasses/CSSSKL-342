4.1.throw_catch -- throw, catch by const &, catch order, unwinding through a
function, and an uncaught exception

Build and run (in the container):
    g++ -std=c++17 -Wall -Wextra -g throw_catch.cpp -o throw_catch
    ./throw_catch

Output (g++ 11, cssimages/linuxlab):
      average: calling divide
      average: back from divide
    5
      average: calling divide
    invalid_argument: divide by zero
    exception: index 7
    now one that nobody catches:
      average: calling divide
    terminate called after throwing an instance of 'std::invalid_argument'
      what():  divide by zero
    Aborted (core dumped)
(exit code 134)

- main calls average, and average calls divide. average(10, 2) returns
  normally: both of its lines print.
- average(1, 0): divide throws, and the exception goes straight out of
  divide AND out of average ("back from divide" is not printed, and average
  never returns a value) to the first catch in main that matches. Every
  function between the throw and the catch is left at once, and its locals
  are destroyed on the way out ("unwinding the stack"; example 4.2 shows the
  destructors running). The rest of main's try block is skipped too.
- Catch by const& (no copy, no slicing). List handlers from most specific
  to least: exception catches every standard exception, so it goes last.
- out_of_range is not an invalid_argument, so the first handler skips it
  and the exception handler catches it.
- e.what() is the message given to the exception's constructor.
- No try around the last average(1, 0): nothing catches it, so the program
  calls terminate and aborts. "never printed" is never printed.

Try it: uncomment the  if (b == 2)  lines in divide. Now average(10, 2)
throws a runtime_error even though nothing is wrong, and the exception
handler catches it; the first lines become
      average: calling divide
    exception: no error but b == 2
C++ lets you throw for anything (even  throw 42;). Doing it for something
that isn't an error is an abuse: exceptions are for errors, not for ordinary
returns or for getting out of loops.

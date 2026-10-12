2.3.rule_of_three -- example 2.2's Numbers, done right

Build and run (in the container):
    g++ -std=c++17 -Wall -Wextra -g three.cpp -o three
    ./three

Output (g++ 11, cssimages/linuxlab):
    Numbers b = a;
      copy constructor
    c = b;
      operator=
    a = a;
      operator=
    a.get(0) = 10, b.get(0) = 99, c.get(0) = 99

valgrind --leak-check=full ./three: no errors, no leaks.

Numbers is the class from example 2.2, word for word, plus the two functions
it was missing. It owns an array, so it needs all three:
  1. ~Numbers(): delete[] what the object owns (2.2 had this already).
  2. Numbers(const Numbers &other): a NEW object gets its OWN array and copies
     the values into it (a deep copy). Runs for  Numbers b = a;  (and
     Numbers b(a);  and pass/return by value).
  3. operator=(const Numbers &other): the object ALREADY exists and already
     owns an array. Runs for  c = b;  on an existing c. It
       - does nothing for a = a (the this != &other check; it still prints),
       - copies into a new array first, then deletes the old array, then
         re-points (so a failed new can't leave the object pointing at freed
         memory); c's old 5 ints are released, and c now holds b's 3,
       - returns *this, so c = b = a works.

Compare with 2.2: the same main, b = a then b.set(0, 99), but now a keeps 10,
and at the end each destructor deletes its own array: no double free.

    a.data_ -----> [ 10 | 0 | 0 ]
    b.data_ -----> [ 99 | 0 | 0 ]
    c.data_ -----> [ 99 | 0 | 0 ]      (its old [0|0|0|0|0] was deleted by operator=)

Alternative: forbid copying with  Numbers(const Numbers &) = delete;  and
Numbers &operator=(const Numbers &) = delete;

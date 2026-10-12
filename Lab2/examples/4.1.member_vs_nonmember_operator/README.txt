4.1.member_vs_nonmember_operator -- operators are functions

Money has + written as a MEMBER function, called both ways: with the operator,
and as an ordinary function call. Output from the course image (cssimages/linuxlab):

$ g++ -std=c++17 -Wall -Wextra operators.cpp -o operators
$ ./operators
a + b
  [member] Money::operator+
a.operator+(b)
  [member] Money::operator+
620 620

a + b is just a shorter way to write a.operator+(b): same function, same result.

The same operator+ could be written either way:

  class Money {
      Money operator+(const Money &rhs) const;   // member: inside the class,
  };                                             //   ONE parameter (the right operand)

  Money operator+(const Money &lhs, const Money &rhs);   // non-member: a GLOBAL
                                                         //   function, TWO parameters

operators.cpp has the non-member version commented out. Swapped in (uncomment it,
comment out the member), it prints "[non-member] global operator+" and gives the
same 620. a + b doesn't change; only the written-out call does: a.operator+(b)
becomes operator+(a, b).

What to notice:
  - A member operator's left operand is the object it's called on, so it lists
    only the right operand as a parameter.
  - A non-member operator is a GLOBAL function -- the same kind of function as
    celsiusToFahrenheit in Lab 1. It belongs to no class, so it can only use the
    class's public members (here, cents()), unless the class makes it a friend.
  - Pick ONE form. With both, C++ says a + b is ambiguous; g++ warns
    ("ISO C++ says that these are ambiguous") and picks one, and other compilers
    may refuse to compile it.
  - -, *, and / work exactly the same way.

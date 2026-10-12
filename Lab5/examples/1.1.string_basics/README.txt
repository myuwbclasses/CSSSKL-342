1.1.string_basics -- string: size, indexing, joining, comparing, pieces, conversions

Build and run (in the container):
    g++ -std=c++17 -Wall -Wextra -g strings.cpp -o strings
    ./strings

Output (g++ 11, cssimages/linuxlab):
    4 pr
    true true
    ea
    2
    no z in pear
    item 42, 18
    invalid_argument: stoi

valgrind --leak-check=full ./strings: no errors, no leaks.

- A string owns its characters (no '\0' to manage, no delete) and knows
  its size(). s[i] doesn't check the index; s.at(i) does, like a vector.
- += and + join. "item " + to_string(42) works because one side is a
  string ("item " + "x", two string literals, does not compile).
- == and < compare the characters: fruit and other are different objects
  holding the same text, so == is true. (In Java, == on two Strings compares
  references; you'd need equals.) < is dictionary order: "apple" < "pear".
- substr(pos, len) copies len characters starting at pos.
- find returns the index where the text starts, or string::npos (a huge
  unsigned value) when it isn't there: always compare with npos.
- to_string turns a number into a string; stoi turns a string into
  an int and throws invalid_argument when it can't ("abc").

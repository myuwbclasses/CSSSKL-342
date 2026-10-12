2.1.signed_unsigned_bug -- mixing signed (int) and unsigned types

An unsigned type can't hold a negative number. When a calculation goes below 0 it
wraps around to a huge positive number, and when you compare an int with an
unsigned value, the int is converted to unsigned first. word.size() returns an
unsigned type (string::size_type, 64 bits here), so this bites with strings
and, later, with every container.

Output below is from the course image (cssimages/linuxlab).

$ g++ -std=c++17 -Wall -Wextra signs.cpp -o signs
signs.cpp:22:46: warning: comparison of unsigned expression in '>= 0' is always true [-Wtype-limits]
   22 |     for (unsigned int i = word.size() - 1; i >= 0; i--) {
signs.cpp:35:18: warning: comparison of integer expressions of different signedness: 'int' and 'std::__cxx11::basic_string<char>::size_type' {aka 'long unsigned int'} [-Wsign-compare]
   35 |     if (position < word.size()) {

$ ./signs
i = 2
i = 1
i = 0
i = 4294967295
i = 4294967294
i = 4294967293
...stopped after 6 steps: this loop never ends on its own
position -1 is NOT less than 3?!

Bug 1: i is unsigned, so i >= 0 is always true. After i = 0, i-- wraps to
4294967295 and the loop goes on (the demo stops it after 6 steps). Using
word[i] there would read far past the end of the string.

Bug 2: before position < word.size() is evaluated, -1 is converted to the
unsigned type of word.size(): it becomes 18446744073709551615, which is not
less than 3. So "not found" looks like a huge index.

Fixes (compile with no warnings; output: i = 2 c / i = 1 b / i = 0 a, then
"position -1 is not a valid index"):

    for (int i = static_cast<int>(word.size()) - 1; i >= 0; i--) { ... }

    if (position >= 0 && position < static_cast<int>(word.size())) { ... }

Lessons: read -Wall -Wextra warnings -- both bugs were flagged before the
program ever ran. Use int for counters that may go below 0, and check for a
negative value before comparing an int with a size.

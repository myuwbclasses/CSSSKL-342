1.1.template_variations -- function templates; T deduced or given explicitly

Build and run (in the container):
    g++ -std=c++17 -Wall -Wextra templates.cpp -o templates
    ./templates

Output (g++ 11, cssimages/linuxlab):
    7
    7
    4.5
    pear
    42 | apples
    42 | apples
    A | 2.5
    3
    B

valgrind: no errors, no leaks.

- template <typename T> makes maxOf work for any type T. For each type you
  use, the compiler writes (instantiates) a real function: maxOf<int>,
  maxOf<double>, maxOf<string>. T must support what the body uses: <.
- Deduced vs. explicit: maxOf(3, 7) works T out from the arguments;
  maxOf<int>(3, 7) names it. Both call the same maxOf<int>.
  Naming T also converts the arguments: maxOf<double>(3, 4.5) turns 3 into
  3.0, and maxOf<string>("pear", "apple") turns both into strings
  ("pear" > "apple": strings compare alphabetically).
- Two type parameters: showBoth<A, B> takes two arguments that may have
  different types. You can name both (showBoth<double, string>), only
  the first (showBoth<char>: A is char, so 65 prints as 'A'; B is deduced),
  or none.
- convertTo<R, T>: R appears only in the return type, so the compiler can't
  deduce it. You must name R; T is still deduced: convertTo<int>(3.99).
  static_cast<int> cuts 3.99 to 3 (it doesn't round).

Try it 1: remove the // in front of  cout << maxOf(3, 4.5)  and build:
    templates.cpp:27:18: error: no matching function for call to 'maxOf(int, double)'
    templates.cpp:8:3: note: candidate: 'template<class T> T maxOf(T, T)'
    templates.cpp:8:3: note:   template argument deduction/substitution failed:
    templates.cpp:27:18: note:   deduced conflicting types for parameter 'T' ('int' and 'double')
3 says T is int, 4.5 says T is double: one T can't be both. The fix is to
name T: maxOf<double>(3, 4.5).

Try it 2: change convertTo<int>(3.99) to convertTo(3.99) and build:
    templates.cpp:33:22: error: no matching function for call to 'convertTo(double)'
    templates.cpp:18:3: note: candidate: 'template<class R, class T> R convertTo(T)'
    templates.cpp:18:3: note:   template argument deduction/substitution failed:
    templates.cpp:33:22: note:   couldn't deduce template parameter 'R'

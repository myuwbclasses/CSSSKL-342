1.3.template_in_cpp -- why templates live in headers

This is the Box<T> class from example 1.2, split the way you'd split a
normal class:
    box.h     the class, with the members and the friend operator<< only DECLARED
    box.cpp   their definitions (the same code as in 1.2)
    main.cpp  the same Box code as 1.2's main; it includes box.h
Only WHERE the definitions are has changed.

Build (in the container):
    g++ -std=c++17 -Wall -Wextra main.cpp box.cpp -o box

Output (g++ 11, cssimages/linuxlab): both files COMPILE, then the LINK fails:
    /usr/bin/ld: /tmp/ccWhT32Y.o: in function `main':
    main.cpp:(.text+0x22): undefined reference to `Box<int>::Box(int const&)'
    /usr/bin/ld: main.cpp:(.text+0x59): undefined reference to `Box<std::__cxx11::basic_string<char, ...> >::Box(...)'
    /usr/bin/ld: main.cpp:(.text+0x7d): undefined reference to `Box<int>::get() const'
    /usr/bin/ld: main.cpp:(.text+0x96): undefined reference to `Box<int>::set(int const&)'
    /usr/bin/ld: main.cpp:(.text+0xa2): undefined reference to `Box<int>::get() const'
    /usr/bin/ld: main.cpp:(.text+0xd4): undefined reference to `Box<std::__cxx11::basic_string<char, ...> >::get() const'
    /usr/bin/ld: main.cpp:(.text+0x10d): undefined reference to `std::ostream& operator<< <int>(std::ostream&, Box<int> const&)'
    /usr/bin/ld: main.cpp:(.text+0x12f): undefined reference to `std::ostream& operator<< <std::__cxx11::basic_string<char, ...> >(...)'
    collect2: error: ld returned 1 exit status
(The three string lines are much longer; "..." marks what's cut.
std::__cxx11::basic_string<char, ...> is the full name of string.)

Why: a template is a recipe, not code. The compiler writes Box<int>'s
members only in a file that both SEES their definitions and USES Box<int>.
main.cpp uses Box<int> but sees only the declarations; box.cpp sees the
definitions but never uses Box<int>. So no object file contains
Box<int>::get or operator<< <int>, and the linker can't find them.

Fix: move the definitions from box.cpp to the end of box.h (below
the class), delete box.cpp, then
    g++ -std=c++17 -Wall -Wextra main.cpp -o box
    ./box
    6 hello
    [6] [hello]
That's exactly how example 1.2 has it, just in a header. Every class
template you write for CSS 342 (ArrayBag, LinkedBag, ...) is the same: the
whole implementation goes in the header.

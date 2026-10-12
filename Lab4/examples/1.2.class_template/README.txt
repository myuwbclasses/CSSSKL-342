1.2.class_template -- Box<T>, a class template, its friend operator<<, and vector<int>

Build and run (in the container):
    g++ -std=c++17 -Wall -Wextra box.cpp -o box
    ./box

Output (g++ 11, cssimages/linuxlab):
    6 hello
    [6] [hello]
    2 20

valgrind: no errors, no leaks.

- template <typename T> class Box { ... } is a recipe for classes. Box<int>
  and Box<string> are two different classes the compiler makes from it.
  Unlike a function template, you always name T: Box<int> a(5);
- A member defined outside the class repeats the template line and is
  qualified with Box<T>::, for example
      template <typename T>
      T Box<T>::get() const { return value_; }
- operator<< is not a member (its left operand is the stream; Lab 2), so it
  can only read value_ because Box makes it a friend. For a class template,
  the friend must itself be a template, with its OWN parameter:
      template <typename U>
      friend ostream &operator<<(ostream &out, const Box<U> &box);
  (T is taken inside the class: reusing it is a "shadows template parameter"
  error.) It is defined after the class with no Box<T>:: (it isn't a member),
  and written there with T: outside the class T is free again, and template
  parameter names don't have to match, only the shape does. cout << a
  binds the parameter to int, so the compiler writes operator<< <int> for
  Box<int>; cout << b writes operator<< <string>. The body uses <<
  on value_, so that type must support << too. The comments in box.cpp say
  all this in detail.
- The whole template stays in one file here. Split into a .h and a .cpp, it
  would fail to link: see example 1.3.
- vector<int> is a class template from the standard library: a growable
  array that knows its own size (push_back, size, [ ]). Carrano's ArrayBag
  is a class template of the same kind.

Try it: in the class, delete the line  template <typename U>  and change
Box<U> to Box<T> in the friend line, the way you'd write it for a normal
class. Build:
    box.cpp:27:63: warning: friend declaration 'std::ostream& operator<<(std::ostream&, const Box<T>&)' declares a non-template function [-Wnon-template-friend]
    box.cpp:27:63: note: (if this is not what you intended, make sure the function template has already been declared and add '<>' after the function name here)
    ... undefined reference to `operator<<(std::ostream&, Box<int> const&)'
    ... undefined reference to `operator<<(std::ostream&, Box<std::__cxx11::basic_string<char, ...> > const&)'
    collect2: error: ld returned 1 exit status
Without its own template line, the friend declares a plain (non-template)
function for each Box<T>: operator<<(ostream &, const Box<int> &), which
nobody defines. Your template operator<< below the class is a different
function, so main calls the plain one and the link fails. Hence: give the
friend its own template <typename U>.

// box.h -- the Box<T> class from example 1.2, but only DECLARED here:
// the member definitions were moved to box.cpp, the way you'd split a
// normal class. This is the mistake this example shows. See README.txt.
#pragma once
#include <iostream>

template <typename T>
class Box {
public:
    explicit Box(const T &value);
    T get() const;
    void set(const T &value);

    // Why template <typename U>, and not T?
    // - Inside the class, T is already taken: it is THIS Box's type (int,
    //   in Box<int>). Writing template <typename T> again is an error:
    //   "declaration of template parameter 'T' shadows template parameter".
    // - Leaving the template line out, as for a normal class:
    //       friend std::ostream &operator<<(std::ostream &out, const Box<T> &box);
    //   declares a plain (non-template) function for each Box: for Box<int>,
    //   operator<<(std::ostream &, const Box<int> &). Nobody writes that
    //   function. The operator<< template we define is a different function,
    //   so g++ warns (-Wnon-template-friend) and the link fails.
    // - So the friend gets a template line of its own, with a new name, U:
    //   "every operator<< <U>, for any U, is a friend of Box<T>". When main
    //   does std::cout << a (a is a Box<int>), U is deduced as int.
    template <typename U>
    friend std::ostream &operator<<(std::ostream &out, const Box<U> &box);

private:
    T value_;
};

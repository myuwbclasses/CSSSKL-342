4.1.lambdas -- a named comparison function, a lambda, and captures

Build and run (in the container):
    g++ -std=c++17 -Wall -Wextra lambdas.cpp -o lambdas
    ./lambdas

Output (g++ 11, cssimages/linuxlab):
    map set list queue vector
    vector set queue map list
    3 words have at least 4 letters
    1 5

valgrind: no errors, no leaks.

- sort(begin, end, shorterFirst): the third argument says when a must
  come BEFORE b (return a.size() < b.size(); use <, never <=). Words of the
  same length (map, set) may come out in either order: sort doesn't
  promise to keep their original order.
- [](const string &a, const string &b) { return a > b; } is a
  lambda: an unnamed function written right where it's needed. Here it
  sorts Z to A.
- [minLength] captures a local variable BY COPY so the lambda can use it;
  count_if counts the words for which the lambda returns true.
- [x] copied x (1) when the lambda was created; [&x] refers to x itself, so
  it sees the later x = 5.

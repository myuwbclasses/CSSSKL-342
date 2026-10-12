4.3.operators_from_each_other -- write the logic once

Money writes the real work in two places only: += (adding) and == (comparing).
The other two operators just reuse them:

  + makes a copy of the left side and does  result += b
  != is simply  !(a == b)

Output from the course image (cssimages/linuxlab):

$ g++ -std=c++17 -Wall -Wextra build_from.cpp -o build_from
$ ./build_from
620
true

Why: if you later fix or change how adding works, you change += only, and +
picks it up automatically. The same goes for == and !=, and for > built from <.

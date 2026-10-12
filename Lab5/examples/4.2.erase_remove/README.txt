4.2.erase_remove -- remove_if doesn't remove; erase does

Build and run (in the container):
    g++ -std=c++17 -Wall -Wextra erase_remove.cpp -o erase_remove
    ./erase_remove

Output (g++ 11, cssimages/linuxlab):
    start        (size 6): 1 2 3 4 5 6
    remove_if    (size 6): 1 3 5 4 5 6
    kept 3 elements
    after erase  (size 3): 1 3 5

valgrind: no errors, no leaks.

- remove_if works only through iterators, so it can't change the
  vector's size. It moves the elements to KEEP (the odd ones) to the front
  and returns an iterator to the new logical end. The values after it
  (here 4 5 6) are leftovers: don't rely on what they are.
- v.erase(newEnd, v.end()) then really removes them: the size drops to 3.
- Together, in one line (the erase-remove idiom):
      v.erase(remove_if(v.begin(), v.end(), isEven), v.end());

3.1.copy_chain -- copying a chain: pushing reverses it, appending keeps the order

Build and run (in the container):
    g++ -std=c++17 -Wall -Wextra -g copy_chain.cpp -o copy_chain
    ./copy_chain

Output (g++ 11, cssimages/linuxlab):
    original: 1 2 3
    pushed:   3 2 1
    appended: 1 2 3

valgrind --leak-check=full ./copy_chain: no errors, no leaks.

Walking the original from the first node, there are two ways to copy:

  push each item at the front      the first item copied ends up LAST:
      pushed = new Node{item, pushed}           3 -> 2 -> 1   (reversed)

  append each item at the end      keep a pointer to the last copy:
      first copy:  appended = copy;             1 -> 2 -> 3   (same order)
      later ones:  last->next = copy;
      always:      last = copy;

A container's copy constructor must give the same order, so it appends.
Each copy makes one new node per item (here 3), and the copy is a completely
separate chain: all 9 nodes are deleted at the end.

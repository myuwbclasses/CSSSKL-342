4.2.change_and_remove -- the same chain: remove the second node, remove the
first node, add a node at the front

Build and run (in the container):
    g++ -std=c++17 -Wall -Wextra -g change_remove.cpp -o change_remove
    ./change_remove

Output (g++ 11, cssimages/linuxlab):
    5 30

valgrind --leak-check=full ./change_remove: no errors, no leaks.

Step by step:

  start                 head --> 10 --> 20 --> 30 --> nullptr

  remove the second     head --> 10 -----------> 30 --> nullptr
  node (20)                            (20 deleted)
      Keep a pointer to it (doomed), link the node BEFORE it around it
      (10's next = 30), then delete it.

  remove the first      head ----------> 30 --> nullptr
  node (10)                  (10 deleted)
      There is no node before it: head itself has to move. Move head to 30
      FIRST, then delete the old first node (kept in old).

  add 5 at the front    head --> 5 --> 30 --> nullptr
      The new node's next is the old head; then head points to the new node.

Two nodes are left at the end, so two deletes.

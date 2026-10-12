4.1.build_and_walk -- a hard-coded chain of 3 nodes: build it, walk it, free it

Build and run (in the container):
    g++ -std=c++17 -Wall -Wextra -g build_walk.cpp -o build_walk
    ./build_walk

Output (g++ 11, cssimages/linuxlab):
    10 20 30
    30

valgrind --leak-check=full ./build_walk: no errors, no leaks.

The chain main builds:

    head --> [ 10 | o-]--> [ 20 | o-]--> [ 30 | o-]--> nullptr
                            n20            n30

- Each node holds an item and a pointer to the next node; the last one's
  next is nullptr. Before the nodes exist, head is nullptr: an empty chain.
- The nodes are built from the last one, so each new node can point to a
  node that already exists.
- The while loop walks the chain: cur starts at head, prints, and moves to
  cur->next until it falls off the end (cur == nullptr).
- head->next->next follows two links, to the node holding 30.
- Three news, so three deletes.

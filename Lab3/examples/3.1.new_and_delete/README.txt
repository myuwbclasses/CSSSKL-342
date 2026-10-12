3.1.new_and_delete -- stack vs. heap, new/delete, new[]/delete[], initializing
a heap array, and who releases what

Build and run (in the container):
    g++ -std=c++17 -Wall -Wextra -g new_delete.cpp -o new_delete
    ./new_delete

Output (g++ 11, cssimages/linuxlab):
    1 2 3
      Point(1, 2)
    *num = 5, *one = 42, pt->x = 1
      ~Point(1, 2)
    10 20 30 40
    0 0 0 0 0
    0 1 4 9 16

valgrind --leak-check=full ./new_delete: no errors, no leaks. Every new has
exactly one delete, every new[] exactly one delete[].

After every delete or delete[], the pointer is set to nullptr. The pointer
still holds the old address otherwise (it dangles); nullptr makes a later
mistake obvious (a crash, not silent corruption), and deleting nullptr is
harmless.

The steps, as numbered in new_delete.cpp:
  1. local[3] is on the stack: no new, no delete, gone at main's }.
  2. ONE element on the heap: new int(5) (set to 5), new int (garbage until
     you set it), and new Point(1, 2). Each returns an address; each gets
     exactly one delete, WITHOUT []. delete pt runs ~Point() first.
  3. Three ways to start a heap array:
       new int[4]{10, 20, 30, 40}   size known: list the values
       new int[n]()                 size from a variable; () sets every int to 0
       new int[n]                   no initializer: the ints are GARBAGE until
                                    you set them (here, with a loop)
  4. print(four, 4) gets only the address, so it needs the count too. It
     only reads: main still owns the array.
  5. main allocated four and zeros, so main releases them, after the calls.
  6. printAndRelease deletes the array it was given. Legal, but its comment
     must say so. Its values = nullptr clears only the FUNCTION'S copy of the
     address (values is a by-value parameter), so main sets its own squares
     to nullptr after the call.

3.2.dangling_and_leak -- a dangling pointer and two leaks, and what valgrind says

Build and run (in the container):
    g++ -std=c++17 -Wall -Wextra -g mistakes.cpp -o mistakes
    ./mistakes

Output (g++ 11, cssimages/linuxlab; the address varies):
    second still points to 0x29d19eb0, which is no longer ours
    end of main

It compiles without a warning and "works". valgrind --leak-check=full
./mistakes tells the real story:
    40 bytes in 1 blocks are definitely lost in loss record 1 of 2
       ...
       by 0x4011D7: forget() (mistakes.cpp:7)
       by 0x401299: main (mistakes.cpp:25)
    400 bytes in 1 blocks are definitely lost in loss record 2 of 2
       ...
       by 0x40126F: main (mistakes.cpp:21)
    ERROR SUMMARY: 2 errors from 2 contexts

  1. Dangling pointer. second = first copies the ADDRESS. After delete first,
     setting first to nullptr doesn't help second: it still holds the freed
     address. Remove the // in front of  cout << *second  and valgrind adds:
         Invalid read of size 4
            at 0x40127A: main (mistakes.cpp:18)
          Address 0x4da0c80 is 0 bytes inside a block of size 4 free'd
            at 0x4848BE1: operator delete(void*, unsigned long)
            by 0x401232: main (mistakes.cpp:15)
     (where it was read, and where it was deleted).
  2. Guaranteed leak (400 bytes = 100 ints, line 21). Overwriting block, the
     ONLY pointer to the first array, means nothing can ever free it.
  3. The most common leak (40 bytes = 10 ints, line 7). temp is a local
     variable: it disappears at forget()'s }, but the array it pointed to
     stays on the heap with no one holding its address. Every call leaks again.

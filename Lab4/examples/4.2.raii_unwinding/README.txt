4.2.raii_unwinding -- stack unwinding, a raw new that leaks, and a unique_ptr that doesn't

Build and run (in the container):
    g++ -std=c++17 -Wall -Wextra -g raii.cpp -o raii
    ./raii

Output (g++ 11, cssimages/linuxlab):
      make local
      destroy local
    caught: something failed

valgrind --leak-check=full ./raii:
    400 bytes in 1 blocks are definitely lost in loss record 1 of 1
       ...
       by 0x40125B: work() (raii.cpp:17)
       by 0x401306: main (raii.cpp:27)
    ERROR SUMMARY: 1 errors from 1 contexts

- When the exception leaves work(), C++ destroys work()'s local objects on
  the way out (stack unwinding): "destroy local" prints BEFORE "caught".
- raw is just a pointer: destroying a pointer frees nothing, and the
  delete[] line is never reached. Its 100 ints (400 bytes, line 17) leak.
- safe is a unique_ptr<int[]>, an OBJECT that owns the array; its
  destructor runs during unwinding and frees it. valgrind reports only raw.
- That is RAII (resource acquisition is initialization): give every resource
  to an object whose destructor releases it. Classes like IntArray and
  LinkedStack, with the rule of three, are RAII classes too.

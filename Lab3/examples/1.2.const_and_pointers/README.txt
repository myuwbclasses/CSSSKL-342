1.2.const_and_pointers -- const int *p vs. int *const p

Build and run (in the container):
    g++ -std=c++17 -Wall -Wextra const_ptr.cpp -o const_ptr
    ./const_ptr

Output (g++ 11, cssimages/linuxlab):
    *p = 2, *q = 10, a = 10

Read each declaration from the name, right to left:
    const int *p     p is a pointer to an int that is const   (the int is locked)
    int *const q     q is a const pointer to an int            (the pointer is locked)

Try it: remove the // in front of  *p = 10;  and  q = &b;  and build again:
    const_ptr.cpp:11:8: error: assignment of read-only location '* p'
    const_ptr.cpp:16:7: error: assignment of read-only variable 'q'

You'll use const int *p (and const Node *cur) all the time: it is the
pointer version of const int &r, "look but don't change". int *const p is rare.

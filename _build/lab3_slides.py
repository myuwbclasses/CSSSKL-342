"""Builds Lab3/Lab3-Slides.pptx.  Run:  python lab3_slides.py"""
import os
from slidekit import Deck

d = Deck("Lab 3: Pointers, Arrays, and Dynamic Memory")

d.title("CSS SKL 342 · Lab 3", "Pointers, Arrays, and Dynamic Memory",
        "Addresses · & and * · arrays · new and delete · linked nodes",
        notes="Array-based and linked bags, stacks, and lists in CSS 342 are built from exactly these pieces: "
              "pointers, arrays, new/delete, and nodes.")

d.agenda([
    (1, "Pointers", [("Lecture", "1:15", "25 min", "Addresses; & and * at a glance"),
                     ("Hands-on", "1:40", "20 min", "Pointer basics"),
                     ("Solutions", "2:00", "10 min", "Walkthrough + self-test")]),
    (2, "Arrays", [("Lecture", "2:10", "15 min", "Arrays are memory"),
                   ("Hands-on", "2:25", "30 min", "Arrays and pointers"),
                   ("Solutions", "2:55", "10 min", "Walkthrough + self-test")]),
    (3, "Dynamic memory", [("Lecture", "3:15", "15 min", "new and delete"),
                           ("Hands-on", "3:30", "25 min", "new[], valgrind"),
                           ("Solutions", "3:55", "10 min", "Walkthrough + self-test")]),
    (4, "Linked nodes", [("Lecture", "4:05", "15 min", "Chains of nodes"),
                         ("Hands-on", "4:20", "35 min", "Node functions"),
                         ("Solutions", "4:55", "10 min", "Walkthrough; catch-up 5:05")]),
], notes="Break 3:05-3:15. 5:05-5:15 is catch-up and wrap-up. Students need valgrind working today. "
         "The lecture examples are in each lab's examples/ folder (they come with the starter zip).")

# ------------------------------------------------------------------ Part 1
d.divider(1, "Pointers",
          ["Take an address with `&` and follow it with `*`",
           "Tell the jobs of `&` and `*` apart wherever you see them",
           "Use `nullptr` and `->` correctly, and find a crash with gdb"],
          why='Pointers reach memory made at run time and build structures that grow, like lists and trees',
          notes='Java hides addresses: every object variable is a reference the language manages for you. C++ lets you hold an address yourself, in a pointer, and that is how you reach memory you allocate while the program runs and how you build structures that grow and change shape, such as linked lists and trees. Pointers are also the most common cause of C++ crashes, so it pays to be exact about what `&` and `*` mean.')

d.bullets_code("A pointer holds an address",
               ["`&a` is the address of `a`; `int *p = &a;` stores it",
                "`*p` is the thing `p` points to: `*p = 7` changes `a`",
                "`int *q(&a);` initializes the same way",
                "`p` is a variable too: `&p` is a different address",
                "In `int* p, r;`, `r` is a plain `int`: the `*` belongs to the name"],
               """int a = 5;
int *p = &a;
int *q(&a);          // same: q also holds a's address

a    // 5
&a   // 0x7ffdec2be760
p    // 0x7ffdec2be760
*p   // 5
&p   // 0x7ffdec2be758

*p = 7;              // a is now 7 (so *q is 7)""",
               notes="Draw two boxes: a (value 5) and p (value = a's address), with an arrow from p to a. "
                     "This course writes int *p, like Carrano: the star sits next to the name it belongs to.")

d.bullets_code("nullptr, ->, and pointer parameters",
               ["`nullptr` points at nothing; following it crashes (Segmentation fault, exit 139)",
                "gdb: `run`, then `bt` shows the line that crashed",
                "An uninitialized pointer is worse: it points somewhere random",
                "`p->x` is short for `(*p).x`",
                "Prefer a reference parameter, unless \"nothing\" is valid or the pointer itself must move"],
               """int *q = nullptr;
*q = 1;              // crash

struct Point { int x; int y; };
Point pt = {1, 2};
Point *pp = &pt;
pp->x = 10;          // same as (*pp).x = 10

void set(int *p, int v) { *p = v; }
void set(int &r, int v) { r = v; }
set(&a, 3);          // pointer version
set(a, 3);           // reference version""")

d.compare("& and * in declarations",
          "Reference: &",
          ["`DataType &r(aVar);`  another name for `aVar`; always initialized, never re-seated",
           "`DataType &MyFunc();`  returns a reference",
           "`void YourFunc(DataType &v);`  can change the caller's variable",
           "`void HerFunc(const DataType &v);`  reads it, no copy"],
          "Pointer: *",
          ["`DataType *bPtr(aPtr);`  holds an address; can point elsewhere later",
           "`DataType* MyFunc();`  returns a pointer",
           "`void YourFunc(DataType *v);`  can change `*v`; call with `&aVar`",
           "`void HerFunc(const DataType *v);`  reads `*v`, doesn't change it"],
          notes="Built from the instructor's two tables. Both columns are DECLARATIONS: a name is being introduced. "
                "Never return a reference or a pointer to one of the function's own locals. "
                "Example: Lab3/examples/1.1.amp_and_star uses every row of both tables.")

d.compare("& and * in statements",
          "Address: &",
          ["`DataType *aPtr = &aVar;`  a pointer initialized with `aVar`'s address",
           "`aPtr = &aVar;`  assigns the address",
           "`&aVar = ...;`  NOT legal: an address can't be assigned to",
           "`return &aVar;`  dangles if `aVar` is a local"],
          "Dereferencing: *",
          ["`DataType bVar = *aPtr;`  the value `aPtr` points to",
           "`bVar = *aPtr;`  read through the pointer",
           "`*aPtr = aVar;`  legal: write through the pointer",
           "`return *aPtr;`  `aPtr` must point at something alive"],
          notes="Both columns are STATEMENTS (code that runs). g++ for &aVar = ...: "
                "error: lvalue required as left operand of assignment. An address can appear anywhere a value can "
                "(f(&aVar), aPtr == &aVar), just never on the left of =.")

d.compare("Reading & and * in code: where is it?",
          "&",
          ["After a type (declaration): reference",
           "In front of one variable: address of",
           "Between two integers: bitwise AND, `6 & 3` is 2",
           "`&&` between conditions: logical AND",
           "Also seen: `T&&`, `[&]` (later)"],
          "*",
          ["After a type (declaration): pointer; `int **pp` points to a pointer",
           "In front of one pointer: dereference (`*this` is the current object)",
           "Between two values: multiplication; in `*p * 2` the first `*` dereferences",
           "`/* ... */`: a comment",
           "`*p++` is `*(p++)`; use `(*p)++` to add to the value"],
          notes="The page's Context and meaning of & / of * tables; the rare rows are collapsed there. "
                "const int *p: can't change the int through p, p can move. int *const p: the reverse. "
                "Example: Lab3/examples/1.2.const_and_pointers.")

d.compare("Coming from Java",
          "Java",
          ["Every object variable is secretly a pointer",
           "`null`",
           "No pointers to `int`s or other primitives",
           "No pointer arithmetic, no address-of",
           "Null dereference: `NullPointerException`"],
          "C++",
          ["Pointers are explicit: `Node *head`",
           "`nullptr`",
           "Point at anything: `int *`, `Point *`, `Node *`",
           "`&` takes addresses; `p + 1` moves along an array",
           "Null dereference: undefined behavior, usually a crash"])

d.exercise(1, "Pointer basics", "20 min", "Lab3/exercises/ex1-pointers/",
           ["`make`: one call doesn't compile. Fix the call, not the function",
            "Print `a`, `&a`, `p`, `*p`, `&p`",
            "Write `setThroughPointer`, `swapThroughPointers`, `largerOf`, `movePoint`",
            "Call `showThroughPointer(nothing)`; run it in gdb, `bt`; remove it"],
           "Confirm that the output, including the five address/value lines, is what you expect, and that you can explain each line.")

d.walkthrough("Walkthrough 1",
              ["`showThroughPointer(a)`: invalid conversion from `int` to `const int*`. Pass `&a`",
               "`&a == p`, `*p == a`; `&p` is the pointer's own address",
               "`largerOf` returns the address of the caller's `y`, so `*bigger = 0` changes `y`",
               "`showThroughPointer(nullptr)`: exit 139; gdb `bt` points at `*p` with `p=0x0`"],
              code="""int *largerOf(int *a, int *b) {
    if (*b > *a) {
        return b;
    }
    return a;
}

int x = 4;
int y = 9;
int *bigger = largerOf(&x, &y);
*bigger = 0;        // y is now 0""")

d.selftest(1, ["After `int x = 3; int *p = &x; int **pp = &p; **pp = 9;`, what is `x`?",
               "What is wrong with `int *p; *p = 5;`?",
               "In `int* a, b;`, what are the types of `a` and `b`?",
               "In `int n = 4; int &r = n; int *p = &r; *p = *p * 2;`, name each `&` and `*`. What is `n`?"])

# ------------------------------------------------------------------ Part 2
d.divider(2, "Arrays",
          ["See an array as what it is: one block of memory, no length, no bounds checks",
           "Use indexing and pointer arithmetic interchangeably, even negative indexes",
           "Work with arrays of objects and 2D arrays"],
          why='The fastest container, under `vector` and `string`, with no length and no bounds checks',
          notes="An array is the simplest and fastest container: elements side by side in memory, each reached by its index in one step. Underneath `vector`, `string`, and the array-based containers you'll write for CSS 342 is a plain C++ array. Unlike a Java array, it carries no length and checks no index, so knowing what it is in memory is how you avoid writing past its end.")

d.bullets_code("Arrays are memory",
               ["One contiguous block: `int a[8];` is 32 bytes, nothing else",
                "The name is the address of the first element: `a` is `&a[0]`",
                "But `sizeof(a)` is 32, `sizeof(p)` is 8",
                "`a[i]` is defined as `*(a + i)`; `p + 1` moves one element",
                "From a pointer into the middle, an index can be negative",
                "An array parameter is a pointer: always pass the count"],
               """int a[8] = {10, 11, 12, 13, 14, 15, 16, 17};
int *p = &(a[5]);   // *p is 15
p[1];               // 16: *(p + 1), a[6]
p[-2];              // 13: *(p - 2), a[3]

void f(int values[]);   // means void f(int *values)""",
               notes="Example: Lab3/examples/2.1.index_is_pointer_arithmetic (a[3] and *(a + 3); p[-2] from a[2]). "
                     "Carrano's ArrayBag keeps an itemCount for exactly this reason: the array can't tell you its length.")

d.bullets("Warning: C++ does not check array bounds",
          ["`int b[4];` has `b[0]` to `b[3]`",
           "`b[4] = 10;` and `b[-1] = 5;` compile with no warning and run with no crash",
           "They silently overwrite whatever memory is next to `b`",
           "valgrind doesn't see it either, for a local array (it checks heap memory)",
           "Java throws `ArrayIndexOutOfBoundsException`; C++ says nothing"],
          callout=("Keeping every index between 0 and size - 1 is YOUR job",
                   "The damage may show up much later, somewhere else, or only in the grader's run."),
          notes="Example 2.1 ends with b[4] = 10 and b[-1] = 5: exit code 0, valgrind ERROR SUMMARY: 0 errors. "
                "Exercise 2's TODO 7 shows an off-by-one overwriting a neighbor.")

d.bullets_code("Arrays of objects and 2D arrays",
               ["`Point pts[3];` makes three real `Point` objects (default constructor each)",
                "Java's `new Point[3]` makes three `null` references",
                "`int a[2][3]`: 2 rows of 3 ints, ONE block, row after row",
                "`int **p(a);` doesn't compile: `a` holds ints, not pointers",
                "Put row pointers in the middle, and `int **` works"],
               """int a[2][3] = {{1, 2, 3}, {4, 5, 6}};
a[1][2] = 60;                  // (a[1])[2]

int *rows[2] = {a[0], a[1]};
int **p(rows);                 // legal

  p          rows             a (one block)
[ o-]--> [ o-]------> [ 1 | 2 | 3 ]
         [ o-]------> [ 4 | 5 |60 ]

p[1][2]   // p -> rows[1] -> 60""",
               notes="Examples: 2.2.array_of_objects (prints each constructor call), 2.3.array_2d "
                     "(g++: cannot convert 'int (*)[3]' to 'int**'; the memory sketch is at the end of the file).")

d.exercise(2, "Arrays and pointers", "30 min", "Lab3/exercises/ex2-arrays/",
           ["`make`: read the `sizeof` warning (on purpose), run, Q1, then delete `sizeInside`",
            "TODO 1-2: element count, addresses, then `p[-2]` from `p = &(a[5])`",
            "TODO 3-6: `sumArray`, `reverseArray`, `findMax` with pointers and no `[]`; `movePoints`",
            "TODO 7: uncomment the off-by-one loop; look at `r.id`; run valgrind; comment it out",
            "`make check`"],
           "Sum 108; reversed 17 16 ... 10, then 0 16 ... 10 after findMax; points (11, 12) (13, 14) (10, 10); r.id back to 1234; make check clean.")

d.walkthrough("Walkthrough 2",
              ["`sizeof(a)` is 32 in `main`, `sizeof(values)` is 8 in the function: g++ warns",
               "`&a[0]`, `&a[1]`, `&a[2]` are 4 bytes apart: one contiguous block",
               "`p[-2]` and `*(p - 2)` are both `a[3]`, counted back from `a[5]`",
               "TODO 7: `r.id` became 0 and valgrind said 0 errors. No one reports it"],
              code="""void reverseArray(int *values, int count) {
    int *front = values;
    int *back = values + count - 1;
    while (front < back) {
        int temp = *front;
        *front = *back;
        *back = temp;
        front++;
        back--;
    }
}""")

d.selftest(2, ["After `int a[4] = {1, 2, 3, 4}; int *p = a + 1;`, what are `p[2]` and `p[-1]`?",
               "What does `int b[5] = {7};` contain?",
               "In `void f(int values[10])`, what is `sizeof(values)`?",
               "`int scores[3]; scores[3] = 100;` What happens?"])

# ------------------------------------------------------------------ Part 3
d.divider(3, "Dynamic memory",
          ["Allocate and release memory with `new`/`delete` and `new[]`/`delete[]`",
           "Size and initialize an array at run time, and grow it",
           "Find memory bugs with valgrind"],
          why='Memory sized at run time, or that outlives a function, comes from the heap, and you free it',
          notes="A local variable dies at the end of its scope, and a local array's size must be known when you compile. Many programs need memory whose size is only known at run time (room for every line of a file) or that must outlive the function that made it (a node added to a list). The heap provides that memory, but in C++ you, not a garbage collector, decide when it's released, and `valgrind` checks that you got it right.")

d.bullets_code("The heap: new and delete",
               ["Locals live on the stack and die at the end of their scope",
                "`new` allocates on the heap; it lives until YOU `delete` it",
                "`new` pairs with `delete`, `new[]` with `delete[]`, exactly once",
                "After `delete`, set the pointer to `nullptr`",
                "Java's garbage collector does this for you; C++ doesn't"],
               """int *num = new int(5);           // one int, set to 5
Point *pt = new Point(1, 2);     // one object
delete num;  num = nullptr;
delete pt;   pt = nullptr;       // runs ~Point()

int *four = new int[4]{10, 20, 30, 40};
int *zeros = new int[n]();       // all 0
int *junk = new int[n];          // garbage until set
delete[] four;  four = nullptr;  // [] because new[]""",
               notes="Example: Lab3/examples/3.1.new_and_delete: stack array, one int and one Point on the heap, "
                     "three ways to start a heap array, passing it to a function, releasing it in main or in a function.")

d.compare("Memory bugs, and how valgrind reports them",
          "The bug",
          ["Leak: `new` with no `delete`",
           "Reading or writing past the end",
           "`delete` for memory from `new[]`",
           "Using memory after `delete` (a dangling pointer)",
           "Deleting twice"],
          "valgrind --leak-check=full ./prog",
          ["`definitely lost: 32 bytes in 1 blocks`",
           "`Invalid read of size 4` / `Invalid write`",
           "`Mismatched free() / delete / delete []`",
           "`Invalid read` ... `inside a block of size 4 free'd`",
           "`Invalid free() / delete / delete[]`"],
          notes="Every message comes with a stack trace: the line where it happened and where the block was allocated. "
                "Compile with -g. Example: Lab3/examples/3.2.dangling_and_leak (a dangling pointer, an overwritten "
                "pointer, and a local pointer that dies while its block doesn't).")

d.bullets("Growing an array: the steps",
          ["An array can't change its size, so growing means moving to a bigger one, in this order:",
           "Allocate a bigger array with `new[]`",
           "Copy the items from the old array into it",
           "`delete[]` the old array",
           "Re-point the pointer at the new array (and update the capacity)",
           "The function takes `int *&data`: the caller's pointer must move to the new array"],
          callout=("Carrano's resizable ArrayBag does exactly this",
                   "You write it yourself in Exercise 3 (TODO 2, grow)."))

d.exercise(3, "Dynamic arrays and memory bugs", "25 min", "Lab3/exercises/ex3-dynamic/",
           ["`growing.cpp`: write `makeSquares` and `grow` BEFORE running",
            "Release both arrays; `valgrind --leak-check=full ./growing` until clean",
            "`leaky.cpp`: looks fine when run. Find and fix its 3 bugs with valgrind"],
           "Confirm that valgrind reports `ERROR SUMMARY: 0 errors` and no leaks for both programs.")

d.walkthrough("Walkthrough 3",
              ["`makeSquares` must use `new[]`: a local array dies when the function returns",
               "`leaky` printed the right sum by luck; valgrind found all three bugs",
               "`Invalid read of size 4`: the loop ran to `i <= n`",
               "`Mismatched free() / delete / delete []`: `delete scores` for a `new[]` array",
               "`definitely lost`: `greeting` was never deleted"])

d.selftest(3, ["What is wrong with `int *p = new int[10]; p++; delete[] p;`?",
               "A function `new`s a buffer, `return`s early if loading fails, and `delete`s at the end. When does it leak?",
               "After `delete p;`, what does `p` hold? Is a second `delete p;` OK?"])

# ------------------------------------------------------------------ Part 4
d.divider(4, "Linked nodes",
          ["Build, walk, and free a chain of nodes",
           "Insert and remove anywhere, including the first node",
           "Prove it with valgrind: no leaks, no invalid reads"],
          why="Nodes linked by pointers grow and insert without moving everything: the base of CSS 342's lists",
          notes='An array is one fixed block, so growing it or inserting in the middle means moving or copying everything. A chain of nodes linked by pointers grows one node at a time, and inserting anywhere means changing just a couple of pointers. The linked stacks, queues, lists, and trees in CSS 342 are all built from such nodes, so these pointer patterns come back in almost every assignment.')

d.bullets_code("A chain of nodes",
               ["Each node holds an item and a pointer to the next node",
                "The last node's `next` is `nullptr`; an empty chain has `head == nullptr`",
                "Walk: start at `head`, move to `next` until `nullptr`",
                "Every linked traversal in your CSS 342 assignments is this loop"],
               """struct Node {
    int item;
    Node *next;
};

Node *n30 = new Node{30, nullptr};
Node *n20 = new Node{20, n30};
Node *head = new Node{10, n20};
// head -> 10 -> 20 -> 30 -> nullptr

Node *cur = head;
while (cur != nullptr) {
    cout << cur->item << " ";
    cur = cur->next;
}""",
               notes="Example: Lab3/examples/4.1.build_and_walk (all in main, no functions).")

d.bullets_code("Changing a chain means changing pointers",
               ["Remove a node: link the node BEFORE it around it, then `delete` it",
                "Removing the first node is a special case: `head` itself moves",
                "Add at the front: the new node points at the old first node",
                "A function that can change the first node takes `Node *&head`",
                "Check three cases every time: empty, one node, many nodes"],
               """// head -> 10 -> 20 -> 30
Node *doomed = head->next;      // remove 20
head->next = doomed->next;
delete doomed;                  // head -> 10 -> 30

Node *old = head;               // remove 10
head = head->next;              // move head FIRST
delete old;                     // head -> 30

head = new Node{5, head};       // head -> 5 -> 30""",
               notes="Example: Lab3/examples/4.2.change_and_remove (all in main). Draw boxes and arrows for each step.")

d.exercise(4, "Node functions", "35 min", "Lab3/exercises/ex4-nodes/",
           ["Draw each function first, with boxes and arrows",
            "Write `length`, `contains`, `pushBack`, `removeFirst`, `deleteChain`",
            "`make` and `./chain_test`; compare with the comments",
            "`make check`: valgrind must show no errors and no leaks"],
           "Confirm that `./chain_test`'s output matches the comments, and that `make check` is clean.")

d.walkthrough("Walkthrough 4",
              ["`pushBack` on an empty chain is a special case; otherwise walk to the last node",
               "Removing the head changes `head`; any other node changes `prev->next`",
               "`delete cur; cur = cur->next;` reads freed memory: valgrind says `Invalid read of size 8`",
               "Before `deleteChain` worked: `definitely lost` and `indirectly lost`"],
              code="""bool removeFirst(Node *&head, int value) {
    if (head == nullptr) return false;
    if (head->item == value) {
        Node *doomed = head;
        head = head->next;
        delete doomed;
        return true;
    }
    Node *prev = head;
    while (prev->next != nullptr &&
           prev->next->item != value) {
        prev = prev->next;
    }
    if (prev->next == nullptr) return false;
    Node *doomed = prev->next;
    prev->next = doomed->next;
    delete doomed;
    return true;
}""")

d.selftest(4, ["From empty: `pushFront(h, 1); pushFront(h, 2); pushBack(h, 3);`. What is the chain?",
               "`void pushFront(Node *head, int value)` sets `head = n;`. What goes wrong?",
               "`pushBack` starts with `while (last->next != nullptr)` on an empty chain. What happens?",
               "How many `new` and `delete` calls to build a 5-node chain and free it?"])

# ------------------------------------------------------------------ wrap-up
d.submission(3,
             """Lab3/
└── exercises/
    ├── ex1-pointers/
    │     pointers.cpp Makefile
    ├── ex2-arrays/
    │     arrays.cpp Makefile
    ├── ex3-dynamic/
    │     growing.cpp leaky.cpp
    │     Makefile
    └── ex4-nodes/
          nodes.h nodes.cpp chain_test.cpp
          Makefile""",
             ["Your work is in `Lab3/exercises`, with subfolders named like the starter folders",
              "Run `make clean` in each; delete executables and core dumps; delete the `examples` folder",
              "Check: no warnings with `-Wall -Wextra`, and valgrind is clean",
              "Zip the whole folder: `zip -r Lab3-netid.zip Lab3`",
              "Upload that one zip to the Lab 3 assignment on Canvas"])

d.takeaways(["`&` takes an address and `*` follows one. In a declaration, they make a reference and a pointer.",
             "`a[i]` is `*(a + i)`: an array is one block, with no length and no bounds checks. Pass the count.",
             "Every `new` needs one `delete`, every `new[]` one `delete[]`. Run valgrind on everything.",
             "Linked structures are pointer rewiring: draw it, handle empty and first-node cases."])

out = os.path.join(os.path.dirname(__file__), "..", "Lab3", "Lab3-Slides.pptx")
d.save(os.path.abspath(out))
print("wrote", os.path.abspath(out), len(d.prs.slides), "slides")

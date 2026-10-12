"""Builds Lab4/Lab4-Slides.pptx.  Run:  python lab4_slides.py"""
import os
from slidekit import Deck

HERE = os.path.dirname(os.path.abspath(__file__))

d = Deck("Lab 4: Templates and Classes That Own Memory")

d.title("CSS SKL 342 · Lab 4", "Templates and Classes That Own Memory",
        "Function and class templates · the rule of three · copying linked chains · exceptions and RAII",
        notes="Every array-based and linked container you'll write in CSS 342 is a class template that owns memory, "
              "so it needs all of this. Carrano's ADTs also throw PrecondViolatedExcept.")

d.agenda([
    (1, "Templates", [("Lecture", "1:15", "15 min", "Generic code"),
                      ("Hands-on", "1:30", "35 min", "Sort templates, Entry<T>"),
                      ("Solutions", "2:05", "10 min", "Walkthrough + self-test")]),
    (2, "The rule of three", [("Lecture", "2:15", "20 min", "Shallow vs. deep copy"),
                              ("Hands-on", "2:35", "35 min", "Copying an IntArray"),
                              ("Solutions", "3:10", "10 min", "Walkthrough + self-test")]),
    (3, "Copying a linked chain", [("Lecture", "3:30", "10 min", "Deep-copying a chain"),
                                   ("Hands-on", "3:40", "30 min", "LinkedStack"),
                                   ("Solutions", "4:10", "5 min", "Walkthrough + self-test")]),
    (4, "Exceptions and RAII", [("Lecture", "4:15", "15 min", "Throw, catch, clean up"),
                                ("Hands-on", "4:30", "25 min", "Exceptions"),
                                ("Solutions", "4:55", "10 min", "Walkthrough; catch-up 5:05")]),
], notes="Break 3:20-3:30. 5:05-5:15 is catch-up and wrap-up. Every exercise folder has 'make check' for valgrind. "
         "The lecture examples are in Lab4/examples/ (they come with the starter zip).")

# ------------------------------------------------------------------ Part 1
d.divider(1, "Templates",
          ["Write function templates, and call them with `T` deduced or named",
           "Turn a working class into a class template, with a friend `operator<<`",
           "Explain why a template lives entirely in its header"],
          why="Write a container or an algorithm once, and use it for `int`, `string`, or `Student`",
          notes="A stack of int values, a stack of strings, and a stack of Student objects differ only in the type of "
                "item they hold, and writing (and fixing) three copies of the same code is wasteful and error-prone. "
                "A template lets you write the code once with the type as a parameter; the compiler produces a version "
                "for each type you use. That is how the standard library gets vector<int> and "
                "vector<string> from one definition, and how the containers in your CSS 342 textbook, like "
                "ArrayBag<ItemType>, are written.")

d.bullets_code("Function templates",
               ["Write it once with a type parameter `T`; the compiler writes (instantiates) a real function for each type you use",
                "`T` is usually deduced from the arguments; `maxOf<double>(3, 4.5)` names it",
                "A parameter used only in the return type must be named: `convertTo<int>(3.99)`",
                "`T` must support whatever the body uses: `maxOf` and a sort need `<`, printing needs `<<`"],
               """template <typename T>             // one type parameter
T maxOf(T a, T b) { return (a < b) ? b : a; }

template <typename A, typename B> // two
void showBoth(A a, B b) {
    cout << a << " | " << b << endl;
}

template <typename R, typename T> // R: return only
R convertTo(T value) { return static_cast<R>(value); }

maxOf(3, 7);                 // deduced: T is int
maxOf<int>(3, 7);            // named: same maxOf<int>
maxOf<double>(3, 4.5);       // 3 becomes 3.0
showBoth<char>(65, 2.5);     // A named, B deduced
convertTo<int>(3.99);        // R named, T deduced: 3""",
               caption="Example 1.1.template_variations: its README has the errors for maxOf(3, 4.5) and convertTo(3.99).",
               code_size=13)

d.bullets_code("Class templates",
               ["Used as `Box<int>`: you always name `T`",
                "The class's name is `Box<T>`: each member defined outside repeats the template line and says `Box<T>::`",
                "A friend `operator<<` needs a template line of its own, with a new name (`U`): `T` is taken inside the class",
                "Without it: a `-Wnon-template-friend` warning, then a link error"],
               """template <typename T>
class Box {
public:
    explicit Box(const T &value);
    T get() const;
    template <typename U>
    friend ostream &operator<<(ostream &out,
                                    const Box<U> &box);
private:
    T value_;
};

template <typename T>
T Box<T>::get() const { return value_; }

template <typename T>     // its own template: T is fine
ostream &operator<<(ostream &out,
                         const Box<T> &box) {
    out << "[" << box.value_ << "]";
    return out;
}""",
               caption="Example 1.2.class_template (box.cpp): prints 6 hello, then [6] [hello].",
               code_size=13)

d.bullets("Templates live in headers",
          ["The compiler needs the whole definition wherever the template is used: put it all in the `.h`",
           "Split into a `.cpp`, both files compile, but the link fails with `undefined reference` "
           "(example 1.3 splits example 1.2's `Box`)",
           "Template errors point inside the template: find the `required from here` line that points at your code",
           "The standard library is full of class templates: `vector<int>`, and even `string` "
           "(short for `basic_string<char>`)",
           "Java generics work only with objects and are checked once; C++ templates work with any type, including `int`"],
          callout=("In your CSS 342 course",
                   "Carrano's ArrayBag, LinkedBag, LinkedStack, and Node are class templates, defined entirely in their "
                   "headers. Exercise 1 is the same step: a working class becomes a class template."))

d.exercise(1, "Sort templates and a class template", "35 min", "Lab4/exercises/ex1-templates/",
           ["Part A: make `mySwap`, `sortArray`, and `printArray` function templates; sort doubles and strings",
            "Sort plain `Entry` objects (it has `operator<`); try `printArray(fruit, 3)` and read the error",
            "TODO 1: make `Entry` a class template `Entry<T>`; move the definitions into `entry.h`, delete `entry.cpp`",
            "TODO 2: a friend `operator<<` that prints `label=value`",
            "Last block: sort and print `Entry<int>` and `Entry<string>` arrays; `make check`"],
           "Confirm that `./templates_test` matches every comment with all blocks uncommented, and that `make check` is clean.")

d.walkthrough("Walkthrough 1",
              ["One `sortArray` sorts `int`, `double`, `string`, and `Entry<int>`",
               "`printArray` on the plain `Entry`: `no match for 'operator<<'`, inside `sorting.h`",
               "`int` becomes `T` only where it's the value's type: the label stays `string`",
               "`Entry fruit[]` must become `Entry<int> fruit[]`: an array's type can't be deduced",
               "Definitions left in `entry.cpp`: 12 `undefined reference` errors (example 1.3)"],
              code="""template <typename T>
class Entry {
public:
    Entry(const std::string &label, const T &value);
    T getValue() const;
    void setValue(const T &value);
    bool operator<(const Entry<T> &other) const;

    template <typename U>
    friend std::ostream &operator<<(std::ostream &out,
                                    const Entry<U> &entry);
private:
    std::string label_;
    T value_;
};

template <typename T>
std::ostream &operator<<(std::ostream &out,
                         const Entry<T> &entry) {
    out << entry.label_ << "=" << entry.value_;
    return out;
}""")

d.selftest(1, ["Given `template <typename T> T maxOf(T a, T b)`, does `maxOf(3, 4.5)` compile?",
               "What must `Rational` provide so that an array of `Entry<Rational>` can be sorted and printed?",
               "Member definitions in `Stack.cpp` give `undefined reference to Stack<int>::push(int const&)`. Why? The fix?",
               "What's wrong with `vector<int> v; v[0] = 5;`?"])

# ------------------------------------------------------------------ Part 2
d.divider(2, "The rule of three",
          ["Tell a shallow copy from a deep copy, in a memory diagram",
           "Explain why the compiler-written copy breaks a class that owns memory",
           "Write a deep-copying copy constructor and `operator=`, or forbid copying"],
          why="C++ copies objects by default, and the default copy is wrong for a class that owns memory",
          notes="In C++, copying an object is the default: passing by value, returning, and = all make copies. For most "
                "classes the compiler-written copy is right, but for a class that owns memory through a pointer it "
                "copies only the address, leaving two objects that share one block of memory and both delete it. Every "
                "CSS 342 container that uses new needs its own copy rules, and this part shows how to write them.")

d.image("Shallow vs. deep copy", os.path.join(HERE, "lab4_memfig.png"),
        caption="Example 2.1.shallow_vs_deep: after original[0] = 99, shallow (same address) sees 99; "
                "deep (its own array) keeps 10.",
        notes="Copying a pointer copies the address it holds, not what it points at. Shallow: two pointers, one array. "
              "Deep: new memory, then copy the values. Run copies.cpp: original and shallow print the same address, "
              "deep a different one. One array means one delete[].")

d.bullets_code("The compiler's copy is shallow",
               ["A class that allocates memory owns it and frees it in its destructor",
                "No copy constructor? The compiler writes one that copies each member",
                "A pointer member is copied as an address: two objects, one array",
                "Change one and the other changes; destroy both and the array is freed twice"],
               """class Numbers {
public:
    explicit Numbers(int n)
        : data_(new int[n]()), size_(n) {}
    ~Numbers() { delete[] data_; }
    void set(int i, int value) { data_[i] = value; }
    int get(int i) const { return data_[i]; }
private:
    int *data_;
    int size_;
};

Numbers a(3);
a.set(0, 10);
Numbers b = a;     // b.data_ is a.data_: ONE array
b.set(0, 99);      // a.get(0) is now 99 too
                   // end of main: ~b, then ~a
                   // free(): double free detected""",
               caption="Example 2.2.shallow_copy: exit code 134; valgrind points at both deletes.")

d.bullets_code("The rule of three, done right",
               ["Same `Numbers`, plus the two functions it was missing",
                "Copy constructor: a NEW object gets its own array and copies the values",
                "`operator=`: the object already owns an array. Skip `a = a`; copy first, then delete the old array; "
                "return `*this` so `c = b = a` works",
                "Need one of destructor, copy constructor, `operator=`? You need all three"],
               """Numbers(const Numbers &other)
    : data_(new int[other.size_]), size_(other.size_) {
    for (int i = 0; i < size_; i++) {
        data_[i] = other.data_[i];
    }
}

Numbers &operator=(const Numbers &other) {
    if (this != &other) {
        int *copy = new int[other.size_];
        for (int i = 0; i < other.size_; i++) {
            copy[i] = other.data_[i];
        }
        delete[] data_;
        data_ = copy;
        size_ = other.size_;
    }
    return *this;
}""",
               caption="Example 2.3.rule_of_three: same main as 2.2, and now a keeps 10.")

d.compare("Copy constructor or operator=?",
          "Copy constructor: a NEW object",
          ["`Numbers b = a;` and `Numbers b(a);`",
           "Passing or returning by value",
           "Nothing to clean up: the object is brand new",
           "Not for `const&` parameters: no copy at all"],
          "operator=: an object that already EXISTS",
          ["`c = a;` when `c` already owns memory",
           "Must release the old memory, or it leaks",
           "Must survive `a = a`",
           "Returns `*this`, so `c = b = a` chains"])

d.bullets_code("Or forbid copying",
               ["`= delete` both: the compiler won't write the shallow versions",
                "Any copy is then a compile error, instead of a double free at run time",
                "Passing by `const&` makes no copy, so it still works; passing by value doesn't compile",
                "Members that manage themselves (`string`, `vector`) need none of the three"],
               """class Numbers {
public:
    explicit Numbers(int n)
        : data_(new int[n]()), size_(n) {}
    ~Numbers() { delete[] data_; }
    Numbers(const Numbers &) = delete;
    Numbers &operator=(const Numbers &) = delete;
    ...
};

void show(const Numbers &nums);   // fine: no copy

Numbers b = a;    // error: use of deleted function
                  //   'Numbers::Numbers(const Numbers&)'
c = a;            // error: use of deleted function
                  //   'Numbers& Numbers::operator=(...)'""",
               caption="Example 2.4.forbid_copy: its README has both errors.")

d.exercise(2, "Copying and assigning an IntArray", "35 min", "Lab4/exercises/ex2-copy/",
           ["`make` and `./copy_test`: compare with the comments; how does it end?",
            "`make check`: what kinds of errors does valgrind report?",
            "TODO 1: a deep-copying copy constructor; `./copy_test` again",
            "TODO 2: `operator=`; uncomment Part B",
            "`./copy_test` and `make check`: correct and clean"],
           "Confirm that the output matches the comments in `copy_test.cpp` with Part B uncommented, and that `make check` is clean.")

d.walkthrough("Walkthrough 2",
              ["`b.set(0, 99)` changed `a`: one shared array",
               "`b.add(5)` grew `b`: it deleted the shared array, so `a` printed garbage",
               "`printByValue`'s copy deleted it again: \"double free detected\", abort (exit 134)",
               "valgrind: `Invalid read of size 4` and `Invalid free()`",
               "`operator=` copies before it deletes: `a = a` is safe even without the check, and `*this` survives a failed `new`",
               "Copy constructor only, Part B uncommented: `-Wdeprecated-copy`, and the arrays are shared again"])

d.selftest(2, ["`Buffer b = a;` in an inner block, then `a.write(\"hi\")`. Buffer has no copy constructor. What happens?",
               "Which call the copy constructor: `IntArray b = a;`, `IntArray c(a);`, `d = a;`, `f(a)` with `const IntArray &`?",
               "`operator=` deletes `data_` first, then copies from `other`. What does `a = a;` do?",
               "Does a class with only a `string` and an `int` need its own destructor, copy constructor, or `operator=`?",
               "Which functions run for `IntArray x = y;`? For `IntArray x; x = y;`?"])

# ------------------------------------------------------------------ Part 3
d.divider(3, "Copying a linked chain",
          ["Free every node in a destructor",
           "Deep-copy a chain without reversing it",
           "Write `operator=` for a linked container"],
          why="A linked container owns every node, so copying it means rebuilding the chain node by node",
          notes="A linked container owns not one block of memory but a whole chain of nodes, so copying it means "
                "rebuilding the chain node by node. It's the rule of three again, applied to the structure you'll use "
                "most in CSS 342: linked stacks, queues, and lists all need a destructor, a copy constructor, and an "
                "operator= that handle every node. Keeping the order and handling the empty chain are where most of "
                "the bugs are.")

d.bullets_code("Copying a chain keeps the order",
               ["Destructor: delete every node (pop until empty)",
                "Walk the original and PUSH each item: the copy is reversed",
                "Walk the original and APPEND, remembering the last node copied: same order",
                "`operator=`: self-check, clear, copy; share the work in private helpers",
                "One `new` per node: pass containers by `const&`"],
               """Node *appended = nullptr;
Node *last = nullptr;
for (const Node *cur = original; cur != nullptr;
     cur = cur->next) {
    Node *copy = new Node{cur->item, nullptr};
    if (last == nullptr) {
        appended = copy;      // first copy: the head
    } else {
        last->next = copy;    // later: after the last
    }
    last = copy;
}
// original: 1 2 3   pushed: 3 2 1   appended: 1 2 3""",
               caption="Example 3.1.copy_chain: both copies of a three-node chain, all in main.")

d.exercise(3, "LinkedStack", "30 min", "Lab4/exercises/ex3-linked/",
           ["`make`, `./stack_test`, `make check`: what does valgrind report?",
            "Write the destructor; `make check` is clean",
            "Write the copy constructor (same order!); uncomment Part 2",
            "Write `operator=`; uncomment Part 3; final `make check`"],
           "Confirm that `./stack_test` matches the comments with all parts uncommented, and that `make check` is clean.")

d.walkthrough("Walkthrough 3",
              ["Starter: `64 (16 direct, 48 indirect) bytes ... definitely lost`: 4 nodes, no destructor",
               "Destructor and `operator=` share a private `clear()`",
               "`printStack` pops a COPY, so `a` prints `40 30 20 10` twice",
               "Without the guard, `other = other` clears, then copies an empty stack",
               "Copying n items costs n `new` calls: pass containers by `const&`"],
              code="""~LinkedStack() {
    clear();
}

LinkedStack(const LinkedStack &other)
    : top_(nullptr), count_(0) {
    copyFrom(other);
}

LinkedStack &operator=(const LinkedStack &other) {
    if (&other != this) {
        clear();
        copyFrom(other);
    }
    return *this;
}""")

d.selftest(3, ["A copy pushes each item of `other` from the top. `other` is 3, 2, 1 (top first). What's the copy?",
               "The destructor is just `delete top_;`. What does valgrind report for 4 items?",
               "Why would `printStack(LinkedStack<int> s)` damage the original without a copy constructor?",
               "How many `new` calls does copying a 1000-item stack make?"])

# ------------------------------------------------------------------ Part 4
d.divider(4, "Exceptions and RAII",
          ["Throw and catch standard and custom exceptions",
           "Order catch clauses correctly",
           "Keep memory safe when exceptions fly, with RAII and `unique_ptr`"],
          why="Send an error to the code that can handle it, and still release every resource on the way",
          notes="Some errors can't be handled where they're detected: a stack's pop doesn't know what its caller wants "
                "to do when the stack is empty. An exception carries the error up to code that does know, without every "
                "function in between checking a return value. Because an exception can cut a function short, C++ also "
                "needs a way to make sure memory is still released, and that is RAII: let destructors do the cleanup.")

d.bullets_code("throw and catch",
               ["`throw` stops the function right there",
                "It leaves EVERY function between the `throw` and the matching `catch`, unfinished, with no return value",
                "Nobody catches it: `terminate`, abort (exit 134)",
                "Catch by `const&`, most specific handler first",
                "Throw only for real errors: `throw 42;` compiles, but exceptions as ordinary returns are an abuse"],
               """int divide(int a, int b) {
    if (b == 0) {
        throw invalid_argument("divide by zero");
    }
    return a / b;
}

int average(int total, int count) {
    cout << "  average: calling divide\\n";
    int result = divide(total, count);
    cout << "  average: back from divide\\n";       // skipped
    return result;
}

try {
    cout << average(1, 0) << endl;
} catch (const invalid_argument &e) {
    cout << "invalid_argument: " << e.what();
} catch (const exception &e) {
    cout << "exception: " << e.what();
}""",
               caption="Example 4.1.throw_catch: \"back from divide\" never prints; the exception lands in main's catch.",
               code_size=13)

d.compare("The exception hierarchy",
          "logic_error: the caller's bug",
          ["`invalid_argument`",
           "`out_of_range`",
           "`length_error`",
           "Carrano's `PrecondViolatedExcept` (e.g. `peek()` on an empty stack)"],
          "runtime_error: not preventable",
          ["Disk full, file missing, network down",
           "All derive from `exception`, which has `what()`",
           "A handler for a base class also catches derived classes",
           "So list handlers most specific first; g++ warns otherwise (`-Wexceptions`)"])

d.bullets_code("RAII: destructors clean up",
               ["As an exception leaves a scope, local objects' destructors run (stack unwinding)",
                "A raw `new` has no destructor: the `delete[]` after the throw never runs",
                "RAII: tie each resource to an object that frees it",
                "`IntArray` and `LinkedStack` are RAII classes; `unique_ptr` is RAII for one allocation",
                "C++ has no `finally`: destructors do the cleanup"],
               """void work() {
    Tracer local("local");          // destroyed on the way out
    int *raw = new int[100];        // leaks: never deleted
    unique_ptr<int[]> safe =
        make_unique<int[]>(100);       // freed by ~unique_ptr
    raw[0] = 1;
    safe[0] = 1;
    throw runtime_error("something failed");
    delete[] raw;                   // never reached
}

int main() {
    try {
        work();
    } catch (const runtime_error &e) {
        cout << "caught: " << e.what() << endl;
    }
}""",
               caption="Example 4.2.raii_unwinding: \"destroy local\" prints before \"caught\"; valgrind: 400 bytes lost, all from raw.",
               code_size=13)

d.exercise(4, "Exceptions", "25 min", "Lab4/exercises/ex4-exceptions/",
           ["TODO 1: `Rational` throws on a zero denominator. Run once uncaught, then catch it",
            "TODO 2: `ArrayStack` `peek`/`pop` throw `PrecondViolatedExcept`; catch it",
            "TODO 3: `risky(0..3)` with one `try`, three `catch` clauses. Try `exception` first",
            "TODO 4: `make check` on `raii`; fix the leak with `unique_ptr<int[]>`"],
           "Confirm that `./exceptions_test` handles all four choices, and that `make check` is clean for `raii`.")

d.walkthrough("Walkthrough 4",
              ["Uncaught: \"terminate called after throwing an instance of 'std::invalid_argument'\"",
               "`out_of_range` lands in the `logic_error` handler: it's a `logic_error`",
               "`exception` first: \"will be caught by earlier handler\"",
               "`raii`: 12 bytes definitely lost, fixed by `unique_ptr`",
               "The whole lab: a class template that owns memory needs the rule of three; RAII makes it exception-safe"])

d.selftest(4, ["Does `catch (const logic_error &e)` catch a thrown `out_of_range`?",
               "An exception is thrown three calls deep and caught in `main`. What runs on the way?",
               "What is lost by writing `catch (exception e)`?",
               "Should a destructor throw?"])

# ------------------------------------------------------------------ wrap-up
d.submission(4,
             """Lab4/
└── exercises/
    ├── ex1-templates/
    │     sorting.h entry.h templates_test.cpp
    │     Makefile     (no entry.cpp)
    ├── ex2-copy/
    │     intarray.h intarray.cpp copy_test.cpp
    │     Makefile
    ├── ex3-linked/
    │     LinkedStack.h stack_test.cpp
    │     Makefile
    └── ex4-exceptions/
          PrecondViolatedExcept.h ArrayStack.h
          rational.h rational.cpp raii.cpp
          exceptions_test.cpp Makefile""",
             ["Your work is in `Lab4/exercises`, with subfolders named like the starter folders",
              "Run `make clean` in each; delete executables and core dumps; delete the `examples` folder",
              "Check: no warnings, and `make check` clean everywhere",
              "Zip the whole folder: `zip -r Lab4-netid.zip Lab4`",
              "Upload that one zip to the Lab 4 assignment on Canvas"])

d.takeaways(["A template is written once and instantiated per type; `T` must support what the body uses; it all lives in the header.",
             "Own memory? Write the destructor, a deep copy constructor, and `operator=`, or `= delete` copying.",
             "`operator=`: self-check, copy then delete, return `*this`. Copy a chain by appending, in order.",
             "Catch by `const&`, most specific first. Destructors (RAII) do the cleanup."])

out = os.path.join(HERE, "..", "Lab4", "Lab4-Slides.pptx")
d.save(os.path.abspath(out))
print("wrote", os.path.abspath(out), len(d.prs.slides), "slides")

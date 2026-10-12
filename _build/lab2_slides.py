"""Builds Lab2/Lab2-Slides.pptx.  Run:  python lab2_slides.py"""
import os
from slidekit import Deck

HERE = os.path.dirname(os.path.abspath(__file__))
LAB2 = os.path.join(HERE, "..", "Lab2")

d = Deck("Lab 2: Debugging, Classes, and Operators")

d.title("CSS SKL 342 · Lab 2", "Debugging, Classes, and Operators",
        "cerr and the debugger · writing a class · object lifetime · operators",
        notes="Students find bugs with gdb and the VS Code debugger first, then build classes: the pieces every "
              "CSS 342 data structure is made of. The debugger is used again in Part 3 to watch destructors run.")

d.agenda([
    (1, "Finding bugs", [("Lecture", "1:15", "15 min", "cerr and the debugger"),
                         ("Hands-on", "1:30", "30 min", "Debug grades.cpp"),
                         ("Solutions", "2:00", "10 min", "Walkthrough + self-test")]),
    (2, "Classes in C++", [("Lecture", "2:10", "20 min", "Writing a class"),
                           ("Hands-on", "2:30", "30 min", "The Rational class"),
                           ("Solutions", "3:00", "10 min", "Walkthrough + self-test")]),
    (3, "Object lifetime", [("Lecture", "3:10", "15 min", "Birth and death"),
                            ("Hands-on", "3:25", "30 min", "Tracer and Counter"),
                            ("Solutions", "3:55", "10 min", "Walkthrough + self-test")]),
    (4, "Operator overloading", [("Lecture", "4:15", "15 min", "Operators are functions"),
                                 ("Hands-on", "4:30", "30 min", "Rational operators"),
                                 ("Solutions", "5:00", "5 min", "Walkthrough; catch-up 5:05")]),
], notes="Break 4:05-4:15. 5:05-5:15 is catch-up and wrap-up. One submission at the end of the lab.")

# ------------------------------------------------------------------ Part 1
d.divider(1, "Finding bugs",
          ["Send debug messages to `cerr`, and say why",
           "Find the line a program crashed on with gdb's `bt`",
           "Set breakpoints, step, and watch variables in VS Code"],
          why='A C++ crash often says only "Segmentation fault"; you need tools that find the line',
          notes="Your programs will crash or print wrong answers, and rereading the code is the slowest way to find out why. Two tools are faster: printing what the program is doing, in a way that doesn't mix with its real output, and a debugger, which stops the program at any line and shows every variable. C++ makes them more important than in Java, because a crash often comes with nothing but `Segmentation fault` and no stack trace.")

d.bullets_code("cout vs. cerr",
               ["`cout`: the program's real output, what a grader compares",
                "`cerr`: errors and debug messages; still on the screen with `>`",
                "`cout` text can wait in a buffer; a crash loses it (`endl` writes it)",
                "`cerr` is written immediately: debug messages go there",
                "Java: `System.out` and `System.err`"],
               """$ ./grades
computing Ana
Ana: 89 B
computing Ben
Ben: 70 D
computing Cy
Floating point exception (core dumped)

$ ./grades > out.txt
$ cat out.txt
$                       # empty: all lost!""", code_size=14,
               notes="Examples: Lab2/examples/1.1.cerr_vs_cout (> and 2> separate the streams) and 1.2.cout_lost_on_crash "
                     "(cout without a newline is lost even on the terminal when the program crashes). "
                     "Verified in the image: with output redirected, everything sent to cout is lost when the program "
                     "crashes. After the progress message moves to cerr, out.txt keeps Ana and Ben (writing to cerr "
                     "also flushes cout first).")

d.bullets_code("gdb: find the crash",
               ["Compile with `-g` (our Makefiles do): file, line, and variable names",
                "`gdb ./grades`, then `run`; it stops where the program crashes",
                "`bt`: which function, and every line that called it",
                "`frame 1`, `print name`: look at the caller's variables",
                "`break average`, `next`, `step`, `continue`, `quit`"],
               """$ gdb ./grades
(gdb) run
Program received signal SIGFPE, Arithmetic exception.
average (total=0, count=0) at grades.cpp:13
13	    return total / count;
(gdb) bt
#0  average (total=0, count=0) at grades.cpp:13
#1  report (name="Cy", total=0, count=0)
        at grades.cpp:35
#2  main () at grades.cpp:42
(gdb) print total / count""", code_size=13,
               notes="Inside the container gdb may warn 'Error disabling address space randomization': harmless.")

d.image("The VS Code debugger", os.path.join(LAB2, "images", "vscode-debug-paused.png"),
        caption="▷ menu → Debug C/C++ File. Breakpoint: click left of a line number. F10 next · F11 step into · Shift+F11 out · F5 continue.",
        notes="For one-file programs. Needs the C/C++ extension installed IN THE CONTAINER (Pre-Lab step 7); without it there is no ▷ button and no Debug C/C++ File: Extensions -> C/C++ Extension Pack -> Install in Container. The first time, choose 'C/C++: g++ build and debug active file'. Outlined: "
              "Locals (total = 269, count = 3), the toolbar, the paused line, and the Call Stack (average called from report).")

d.exercise(1, "Debug grades.cpp", "30 min", "Lab2/exercises/ex1-debug/",
           ["`make`, `./grades`: compare with the expected lines in `main`",
            "`./grades > out.txt`, `cat out.txt`; move the progress message to `cerr` and repeat",
            "gdb: `run`, `bt`, `frame 1`, `print name`",
            "VS Code: breakpoint on `return total / count;`, Debug C/C++ File, watch the values; then step through `letter`",
            "Fix the three bugs (not `main`)"],
           "Prints `Ana: 89.6667 B`, `Ben: 70 C`, `Cy: no scores`, `Dee: 91 A`, `done`; `out.txt` holds only those five lines.",
           notes="Bugs: integer division in average, > instead of >= for C, no check for count == 0 (SIGFPE).")

d.walkthrough("Walkthrough 1",
              ["`out.txt` was empty: the crash lost everything `cout` was holding",
               "`bt` points at `average (total=0, count=0)`, called for Cy",
               "Ana: `total / count` is 89 in `int`; fix: `static_cast<double>(total) / count`",
               "Ben: `avg > 70` misses 70; fix: `>=`",
               "Cy: check `count == 0` before dividing, and print `no scores`"])

d.selftest(1, ["`cout << \"step 3 done\\n\";` then a crash: the line shows on screen but not in `out.txt`. Why? Two fixes?",
               "Stopped on `double avg = average(total, count);`: what's the difference between `next` and `step`?",
               "A program dies with `Segmentation fault`. Fastest way to find the line?",
               "What do you lose in gdb without `-g`?"])

# ------------------------------------------------------------------ Part 2
d.divider(2, "Classes in C++",
          ["Split a class into a header and a `.cpp` file",
           "Initialize every member with an initializer list",
           "Make member functions `const` whenever they don't change the object"],
          why='A class keeps its data valid; C++ writes classes a little differently from Java',
          notes="A class bundles data with the functions that keep it valid: if only `Rational`'s own functions can set the denominator, it can never be zero. The ideas are the ones you know from Java, but C++ splits a class across a header and a `.cpp` file and adds details Java doesn't have, such as initializer lists and `const` member functions. Every CSS 342 assignment is built from classes written this way.")

d.bullets_code("A class in two files",
               ["The header declares the class: data members and member function declarations",
                "The `.cpp` defines each member function, prefixed with `Rational::`",
                "`public:` and `private:` label whole sections; data is private",
                "Don't forget the `;` after the class's closing brace"],
               """// rational.h
class Rational {
public:
    Rational();
    Rational(int num, int den);
    int numerator() const;
    std::string toString() const;
private:
    int num_;
    int den_;
    void normalize();
};

// rational.cpp
int Rational::numerator() const {
    return num_;
}""")

d.bullets_code("Constructors and initializer lists",
               ["A constructor has the class's name and no return type; overload freely",
                "The initializer list runs before the body and initializes each member",
                "Members are NOT set to zero for you: a forgotten `int` holds garbage",
                "Older code assigns in the body (`num_ = num;`): it still works, but write the list; `const` members require it",
                "`Rational r;` uses the default constructor; `Rational r();` declares a function!"],
               """Rational::Rational() : num_(0), den_(1) {
}

Rational::Rational(int num, int den)
    : num_(num), den_(den) {
    normalize();
}

Rational a;         // 0/1
Rational b(6, -8);  // -3/4
Rational c = 5;     // 5/1 (needs Rational(int))""",
               notes="Older code assigns members in the constructor body (num_ = num;). It still works for int members, "
                     "so students must be able to read it, but it creates then assigns, and fails for const members "
                     "('assignment of read-only member'). Write the initializer list.")

d.bullets_code("const member functions",
               ["`const` after the parameter list promises not to change the object",
                "A `const` object or `const&` parameter can call only const members",
                "Otherwise: \"passing 'const Rational' as 'this' argument discards qualifiers\"",
                "Rule: every member function that doesn't change the object is `const`, in both the `.h` and the `.cpp`"],
               """void show(const Rational &r) {
    cout << r.toString();       // needs toString() const
}

int Rational::numerator() const {
    num_ = 0;      // error: read-only object
    return num_;
}""")

d.compare("Coming from Java",
          "Java",
          ["`Rational r = new Rational(1, 2);` creates the object on the heap",
           "Fields default to 0 / null",
           "Methods can always be called on any reference",
           "One file per class; no headers"],
          "C++",
          ["`Rational r(1, 2);` creates a local object, destroyed at the end of the scope",
           "Members hold garbage unless you initialize them",
           "Only `const` members can be called on `const` objects",
           "Class declaration in `.h`, member definitions in `.cpp`"])

d.exercise(2, "The Rational class", "30 min", "Lab2/exercises/ex2-classes/",
           ["Run `make`: `main.cpp` does not compile. Fix it by changing only `rational.h` and `rational.cpp`",
            "Leave the default constructor empty, run, and note what `default:` prints",
            "Complete the TODOs: initializer lists, `toDouble`, `toString`, `normalize`",
            "Check the output against the comments in `main.cpp`"],
           "Confirm that `./rational_app` prints the five expected values.",
           notes="Planted: getters not const, so show(const Rational &) fails to compile.")

d.walkthrough("Walkthrough 2",
              ["Error: `discards qualifiers`. Fix: add `const` to the four read-only members, in the `.h` and the `.cpp`",
               "Empty default constructor: garbage, different every run, and `-Wall` says nothing",
               "`normalize` changes the object, so it can't be `const`; it's private because the class keeps its own invariant",
               "`gcd(0, 7)` is 7, so `0/7` becomes `0/1` with no special case"],
              code="""void Rational::normalize() {
    if (den_ < 0) {
        num_ = -num_;
        den_ = -den_;
    }
    int g = gcd(num_, den_);
    num_ /= g;
    den_ /= g;
}""")

d.selftest(2, ["`report(const Box &b)` calls `b.width()` and gets \"discards qualifiers\". What's the fix, and where?",
               "Does `int Rational::numerator() const { num_ = 0; return num_; }` compile?",
               "A constructor body says `int num_ = n; int den_ = d;`. What's wrong?",
               "Name two kinds of members that must be initialized in the initializer list"])

# ------------------------------------------------------------------ Part 3
d.divider(3, "Object lifetime",
          ["Predict exactly when objects are constructed, copied, and destroyed",
           "Watch a destructor run in the debugger",
           "Return references from member functions safely"],
          why='C++ objects die at a known moment, so their destructors can clean up on time',
          notes="In Java an object lives until the garbage collector decides it's unreachable, and you never know exactly when. In C++ an object dies at a precise moment, usually a closing `}`, and its destructor runs right then. That is what lets a C++ class release memory and other resources on time, and it means you need to know exactly when your objects are created, copied, and destroyed.")

d.bullets_code("Objects die at the end of their scope",
               ["Locals are created at their definition and destroyed at the closing `}`",
                "Destruction runs in reverse order of construction",
                "A temporary (an object with no name) dies at the end of its statement",
                "Globals are built before `main` and destroyed after it",
                "The destructor `~Tracer()` runs automatically, every time; there is no garbage collector"],
               """{
    Tracer a("a");     // + a
    Tracer b("b");     // + b
}                      // - b
                       // - a
Tracer("temp");        // + temp  - temp

class Tracer {
public:
    Tracer(const std::string &name);
    Tracer(const Tracer &other);  // copy ctor
    ~Tracer();                    // destructor
};""",
               notes="Example: Lab2/examples/3.1.scope_and_destructor (a { } sub-block inside main; every constructor "
                     "and destructor prints). Have students predict the order first.")

d.bullets_code("Copies, and when they happen",
               ["`Tracer t1(t2);` and `Tracer t1 = t2;` are BOTH copy construction, not assignment: `t1` is being created",
                "Only `t1 = t2;` on an object that already exists is assignment; pass by value also copy-constructs",
                "Pass by `const&`: no copy, no destructor call",
                "Returning a local by value usually makes no copy (copy elision)",
                "Members are built in DECLARATION order, whatever the initializer list says; `-Wall` warns (`-Wreorder`)"],
               """void byValue(Tracer t);           // + copy of c ... - copy of c
void byConstRef(const Tracer &t);  // nothing

Tracer make(const string &n) {
    Tracer t(n);
    return t;                      // no copy
}

class Pair {
    Tracer first_;                 // built 1st
    Tracer second_;                // built 2nd
public:
    Pair() : second_("second"), first_("first") {}
};""", code_size=13,
               notes="Examples: Lab2/examples/3.2.copy_construction (numbered objects: t1(t2) and t1 = t2 both print "
                     "'copy constructor'; t3 = t1 prints 'assignment') and 3.3.copy_elision (build with "
                     "-fno-elide-constructors to see the copy that elision saves).")

d.bullets_code("Returning references from members",
               ["Non-const version returns `int&`: the caller can assign through it",
                "Const version returns `int` (or `const int&`): read-only",
                "The compiler picks by the object's constness",
                "This is exactly how `operator[]` works on containers",
                "Never keep the reference longer than the object lives"],
               """class Counter {
public:
    int &value()       { return count_; }
    int  value() const { return count_; }
private:
    int count_ = 0;
};

Counter c;              // not const
c.value() = 4;          // -> non-const version
int n = c.value();      // -> non-const too: c isn't const
const Counter k;        // const
int m = k.value();      // -> const version
k.value() = 9;          // error: lvalue required""",
               notes="The choice depends on whether the OBJECT is const, not on reading vs. writing: "
                     "int n = c.value() only reads but still calls the non-const version (verified).")

d.exercise(3, "Tracer and Counter", "30 min", "Lab2/exercises/ex3-lifetime/",
           ["Read `lifetime.cpp`; write your predictions in `predictions.txt` BEFORE running",
            "`make lifetime`, read the warning, run `./lifetime`, mark wrong predictions",
            "gdb: `break Tracer::~Tracer`, `run`, `bt`, `print name_`, `continue`",
            "Complete the two TODOs in `counter.h`; `make counter_test`; try the Q6 line"],
           "Compare your predictions with the real output, and confirm that `./counter_test` prints `count = 5` and `count = 0`.",
           notes="lifetime is built from two .cpp files, so gdb rather than VS Code's one-file debug button. "
                 "First stop: name_ = \"b\", called from main () at lifetime.cpp:49, the closing } of the block.")

d.walkthrough("Walkthrough 3",
              ["`+ global` appears before \"main starts\"; `- global` after \"main ends\"",
               "Scenario 2: one copy for `byValue`, none for `byConstRef`; scenario 3: only `+ d` (copy elided)",
               "Scenario 4: `+ temp` `- temp` before the next statement",
               "Scenario 5: `first_` then `second_` (declaration order), destroyed in reverse after the Pair destructor body",
               "gdb: `bt` shows `main () at lifetime.cpp:49`: the destructor runs at the closing `}`"])

d.selftest(3, ["`Tracer x(\"x\"); { Tracer y(\"y\"); } Tracer z(\"z\");` in `main`: what's printed, including at the end?",
               "How many constructor and destructor calls does `f(x)` cause for `void f(Tracer t)`? For `g(const Tracer &)`?",
               "Members declared `b_` then `a_`, initializer list `: a_(...), b_(...)`. Construction and destruction order?",
               "`const string &name() const` returns a member. When is using the result unsafe?"])

# ------------------------------------------------------------------ Part 4
d.divider(4, "Operator overloading",
          ["Write `+=`, `+`, `==`, `<`, and `<<` with the right signatures",
           "Choose between member and non-member operators",
           "Know when `friend` is needed"],
          why='Let your own types use `+`, `<`, and `<<` like `int` does; sorting, maps, and printing rely on it',
          notes='A class for fractions, money, or dates is easier to use when `a + b`, `a < b`, and `cout << a` work just as they do for `int`. C++ lets you define what operators mean for your own types, and the standard library counts on it: sorting and `map` use `<`, and printing uses `<<`. CSS 342 assignments regularly ask for `==`, `<`, and `<<` on your classes.')

d.bullets_code("Operators are just functions",
               ["`a + b` calls `operator+(a, b)` or `a.operator+(b)`",
                "Compound `+=` is a member: changes the object, returns it by reference",
                "`return *this;`: read `*this` as \"the current object\" (the `*` comes with pointers)",
                "`+` is a non-member: makes a new object, returns it by value",
                "Build `+` from `+=`, `!=` from `==`, `>` from `<`; `<<` returns the stream so calls chain"],
               """Rational &Rational::operator+=(const Rational &rhs) {
    num_ = num_ * rhs.den_ + rhs.num_ * den_;
    den_ = den_ * rhs.den_;
    normalize();
    return *this;
}

Rational operator+(const Rational &a, const Rational &b) {
    Rational result = a;
    result += b;
    return result;
}

ostream &operator<<(ostream &out,
                         const Rational &r) {
    return out << r.toString();
}""", code_size=13,
               notes="Examples: 4.1.member_vs_nonmember_operator (a + b IS a.operator+(b); the non-member version is "
                     "commented out, ready to swap in), 4.2.return_this ((total += a) += b gives 123; returning by value "
                     "gives 120), 4.3.operators_from_each_other (+ from +=, != from ==).")

d.compare("Member or non-member?",
          "Member",
          ["`+=`, `-=`, `*=`, `=`: change the left operand; return `T&`",
           "`[]`: const and non-const versions",
           "The left operand must already be your type: no conversion",
           "Has access to private data"],
          "Non-member",
          ["`+`, `-`, `*`: return a new `T` by value",
           "`==`, `!=`, `<`: return `bool`",
           "`<<`: the left operand is a stream, not your class",
           "Conversions work on both sides: `2 + half` and `half + 2`",
           "Needs `friend` only if it must read private data"],
          notes="Example: 4.4.why_nonmember. With + as a member, 2 + m fails: no match for 'operator+' "
                "(operand types are 'int' and 'MemberMoney'); the compiler never converts the object a member is called on.")

d.bullets_code("friend, and operator<<",
               ["`operator<<` is always a non-member: its left operand is the stream",
                "With public accessors it needs nothing special",
                "Without them, the class declares it a `friend`: \"this global function may use my private members\"",
                "`friend` does NOT make it a member: the definition has no `friend` and no `Secret::`",
                "Use `friend` only when accessors aren't enough"],
               """class Point {                       // accessors: no friend
public:
    int x() const { return x_; }
    int y() const { return y_; }
private:
    int x_, y_;
};
ostream &operator<<(ostream &out, const Point &p) {
    return out << "(" << p.x() << ", " << p.y() << ")";
}

class Secret {                      // no accessors: friend
public:
    friend ostream &operator<<(ostream &out, const Secret &s);
private:
    int code_;
};
ostream &operator<<(ostream &out, const Secret &s) {
    return out << "Secret #" << s.code_;   // a global function
}""", code_size=12, split=0.42,
               notes="Example: 4.5.friend_operator_output (both classes, one driver). Its README has the real errors for "
                     "the three usual mistakes: no friend line -> 'int Secret::code_' is private within this context; "
                     "friend on the definition -> 'friend' used outside of class; Secret:: on the definition -> "
                     "'... must have exactly one argument' (as a member its left operand would be a Secret).")

d.exercise(4, "Rational operators", "30 min", "Lab2/exercises/ex4-operators/",
           ["Implement `+=`, `+`, `==`, `<`, `<<` in `rational.cpp`; `make` and run `./test_operators`",
            "Declare and define `-`, `*`, `!=`, `*=` yourself",
            "Uncomment the remaining tests and get all of them to pass"],
           "Confirm that `./test_operators` reports 0 failures with every test uncommented.")

d.walkthrough("Walkthrough 4",
              ["`2 + half` works because `+` is a non-member and `Rational(int)` converts the `2`",
               "`(t += a) += b` works because `+=` returns `*this` by reference",
               "`cout << a << b` is `(cout << a) << b`, so `<<` returns the stream",
               "No `friend` needed: the operators use `numerator()` and `denominator()`",
               "Marking `Rational(int)` `explicit` would break `2 + half`"])

d.selftest(4, ["`Card` has private `rank_`, `suit_`, no accessors. How do you declare `operator==` so it can read them?",
               "With `+` written as a member, which compile: `half + 2`, `2 + half`?",
               "`Rational &operator+(...)` builds a local `r` and returns it. What's wrong?",
               "Why must `operator<<` return the stream for `cout << a << b` to work?"])

# ------------------------------------------------------------------ wrap-up
d.submission(2,
             """Lab2/
└── exercises/
    ├── ex1-debug/
    │     grades.cpp Makefile
    ├── ex2-classes/
    │     rational.h rational.cpp main.cpp
    │     Makefile
    ├── ex3-lifetime/
    │     tracer.h tracer.cpp lifetime.cpp
    │     predictions.txt counter.h
    │     counter_test.cpp Makefile
    └── ex4-operators/
          rational.h rational.cpp
          test_operators.cpp Makefile""",
             ["Your work is in `Lab2/exercises`, with subfolders named like the starter folders",
              "Run `make clean` in each; delete `.o` files, executables, `out.txt`; delete the `examples` folder",
              "Check: compiles with `-Wall -Wextra`; only the planted `-Wreorder` warning",
              "Zip the whole folder: `zip -r Lab2-netid.zip Lab2`",
              "Upload that one zip to the Lab 2 assignment on Canvas"])

d.takeaways(["Debug messages go to `cerr`. After a crash: run it in the debugger and read `bt`; for wrong output, break and step.",
             "Class in the `.h`, members in the `.cpp`, initializer lists, and `const` on every read-only member.",
             "Objects die at the end of their scope, in reverse order. Pass objects by `const&` to avoid copies.",
             "Compound operators are members returning `*this` by reference; `+`, `==`, `<<` are non-members."])

out = os.path.join(LAB2, "Lab2-Slides.pptx")
d.save(os.path.abspath(out))
print("wrote", os.path.abspath(out), len(d.prs.slides), "slides")

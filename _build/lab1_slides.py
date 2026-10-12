"""Builds Lab1/Lab1-Slides.pptx.  Run:  python lab1_slides.py"""
import os
from slidekit import Deck

HERE = os.path.dirname(os.path.abspath(__file__))
LAB1 = os.path.join(HERE, "..", "Lab1")

d = Deck("Lab 1: Toolchain and C++ Basics")

d.title("CSS SKL 342 · Lab 1", "Toolchain and C++ Basics",
        "Your Linux environment · building multi-file programs · numbers · references",
        notes="Students arrive with the Pre-Lab done: container cssskl342 running, VS Code attached, "
              "hello.cpp compiled. Part 0 makes sure they understand that setup; then three rounds of "
              "short lecture, hands-on exercise, and solution walkthrough.")

d.agenda([
    (0, "Your Linux environment", [("Hands-on", "1:15", "25 min", "Linux warm-up and practice"),
                                   ("Lecture", "1:40", "10 min", "One folder, two names"),
                                   ("Hands-on", "1:50", "25 min", "Files on both sides; walkthrough 2:10")]),
    (1, "How C++ programs are built", [("Lecture", "2:15", "20 min", "The build model"),
                                       ("Hands-on", "2:35", "35 min", "Fix a broken build"),
                                       ("Solutions", "3:10", "10 min", "Walkthrough + self-test")]),
    (2, "Types, conversions, limits", [("Lecture", "3:20", "15 min", "Numbers in C++"),
                                       ("Hands-on", "3:35", "30 min", "Rounding and limits"),
                                       ("Solutions", "4:05", "5 min", "Walkthrough + self-test")]),
    (3, "References", [("Lecture", "4:20", "15 min", "Value, &, const &"),
                       ("Hands-on", "4:35", "25 min", "Reference functions"),
                       ("Solutions", "5:00", "5 min", "Walkthrough; catch-up 5:05")]),
], notes="Break 4:10-4:20. 5:05-5:15 is catch-up and wrap-up: finish exercises, build the submission zip, takeaways. "
         "Each exercise ends with a self-check: students confirm for themselves that their code runs correctly. "
         "One submission at the end (Exercises 1-3; nothing for Part 0).")

# ------------------------------------------------------------------ Part 0
d.divider(0, "Your Linux environment",
          ["Explain the difference between the image and your container",
           "Say where every file lives: in Linux, on your computer, or both",
           "Use the everyday Linux commands: `pwd`, `ls`, `cd`, `mkdir`, `cp`, `mv`, `rm`, ...",
           "Move between VS Code and File Explorer (Finder) on the same files",
           "Read and write file names, relative paths, and full paths"],
          why='CSS 342 grades your code with g++ on Linux; the container gives everyone that same setup',
          notes="Your CSS 342 programs are compiled and graded with g++ on Linux, and a program that builds and runs on your laptop's compiler can fail or behave differently there. A container gives everyone the same Linux, the same compiler, and the same tools (`make`, `gdb`, `valgrind`) on any computer. The one thing to get straight is where each file lives: on your computer, inside the container, or both.")

d.bullets_code("Warm-up: Linux command essentials",
               ["Where am I? `pwd` · `ls` (`-l`, `-a`, `-R`) · `cd` (`..` up, `~` home)",
                "Files and folders: `mkdir` (`-p`) · `touch` · `cp` (`-r`) · `mv` (move or rename) · `rm` (`-r`; forever) · `rmdir` (empty folders only)",
                "Text: `cat` · `less` (`q` quits) · `echo` with `>` (write) and `>>` (add)",
                "Help: `ls --help` (no man pages in the image) · `clear`",
                "Keys: `Tab` finishes names · ↑ repeats · `Ctrl+C` stops a program",
                "Full reference: every lab page's left menu, Reference, Linux commands"],
               """cd ~/CSSSKL342
mkdir -p part0/warmup
cd part0/warmup
touch empty.txt
echo "first line" > notes.txt
echo "second line" >> notes.txt
cat notes.txt
cp notes.txt copy.txt
mkdir backup
mv copy.txt backup/
mv empty.txt blank.txt
ls -R              # checkpoint 1
rmdir backup       # Directory not empty
cd ..
rm -r warmup       # no Recycle Bin!""", kind="Hands-on", code_size=14, split=0.5,
               notes="15 minutes, guided, before Exercise 0; the Lab 1 page has the full sequence with two "
                     "checkpoints and expected output. The full reference is its own page, linked from every lab "
                     "page's left menu (reference/linux.html, built from assets/commands.js).")

d.bullets("Practice: Linux commands",
          ["Build a tree in `part0`: `practice/src/main.cpp`, `practice/src/util.h`, and `practice/docs/readme.txt` with two lines",
           "Reorganize: rename `util.h` to `convert.h`, copy `readme.txt` into `src` as `notes.txt`, move `readme.txt` up, "
           "delete the empty `docs` with `rmdir` (then see why `rmdir src` refuses)",
           "Relative paths: from inside `src`, use `..` to print, copy, and list; then go back and `rm -r practice`",
           "Each step has a self-check with exact `ls -R` output on the lab page; model answers are hidden until you try"],
          kind="Hands-on", callout=("10 minutes, no step-by-step commands",
                                    "Use the warm-up and the Linux command reference (left menu, Reference)."),
          notes="Model answers and expected output: Lab 1 page and the private solutions, Lab1/part0-answers.txt.")

d.image("One folder, two names", os.path.join(LAB1, "images", "docker-model.png"),
        caption="Your setup from the Pre-Lab: hello.cpp is ONE file, with a Linux name and a Windows/Mac name.",
        notes="Walk the picture: the image (template) -> docker run -> container. The green folders are the same "
              "folder (the -v option). notes.txt lives only in the container. The VS Code window is on the "
              "student's computer, but attached to a VS Code Server in Linux: files, terminal, g++ all run there.")

d.bullets("What runs where",
          ["Image vs. container: the image `cssimages/linuxlab` is a read-only template; your container "
           "`cssskl342` is a running Linux machine made from it, once, by `docker run`",
           "One folder, two names: `/home/cssuwbstudent/CSSSKL342` in Linux is `C:\\Users\\you\\CSSSKL342` "
           "(Mac: `/Users/you/CSSSKL342`); everything else in Linux lives only in the container",
           "The VS Code window is on your computer, but its files, terminal, and `g++` are in Linux: "
           "check the bottom-left label, Container ... (cssskl342)",
           "Linux rules apply inside: programs compiled there run only in Linux, `rm` deletes for good "
           "(no Recycle Bin), and file names are case-sensitive"],
          callout=("Keep all your course work in CSSSKL342",
                   "It is on your own disk: backed up, and safe even if the container is deleted."))

d.exercise(0, "Files on both sides", "20 min", "~/CSSSKL342/part0/",
           ["VS Code → computer: in the `part0` folder from the warm-up, create `from-vscode.txt` in VS Code; add a line in Notepad (TextEdit)",
            "Computer → VS Code: make folder `made-on-my-computer` in File Explorer; write, compile, run `sum.cpp` in VS Code",
            "Rename in File Explorer, then move with `mv` in the terminal",
            "Delete `sum` in File Explorer, then `rm` a file in Linux: check the Recycle Bin",
            "Make `~/outside.txt` in the terminal; look for it in File Explorer, then remove it"],
           "In `part0`, `ls -R` shows only `made-on-my-computer`, containing only `sum.cpp`. Nothing to submit.",
           notes="If a file doesn't appear on the other side: Refresh in VS Code's Explorer, F5 in File Explorer. "
                 "Answers: the private solutions, Lab1/part0-answers.txt.")

d.bullets_code("File names and paths",
               ["File name: `sum.cpp` (`.cpp` is the extension)",
                "Full path: from the root `/` down: same meaning anywhere",
                "Current folder: where the terminal is; `pwd` prints it, `cd` changes it",
                "Relative path: starts from the current folder, so no leading `/`",
                "`~` home, `.` this folder (`./hello`), `..` one level up",
                "Linux uses `/` and is case-sensitive; quote names with spaces"],
               """cd ~/CSSSKL342/part0
pwd
# /home/cssuwbstudent/CSSSKL342/part0

# full path of sum.cpp:
#   /home/cssuwbstudent/CSSSKL342/part0/
#       made-on-my-computer/sum.cpp

# all three list that same file:
ls made-on-my-computer/sum.cpp         # relative
ls ~/CSSSKL342/part0/made-on-my-computer/sum.cpp
cd made-on-my-computer
ls ../made-on-my-computer/sum.cpp      # via ..

ls "my notes.txt"    # quotes: one name""", code_size=13, split=0.44,
               notes="'No such file or directory' is almost always the wrong current folder: pwd, then ls. "
                     "The same idea applies to #include \"convert.h\" in Part 1.")

d.bullets("Done early? Challenges while others finish",
          ["Case-sensitivity trap: `#include \"Stack.h\"` finds `stack.h` in the shared folder, but not in `/tmp` "
           "(or on the Linux grader)",
           "Line endings (Windows): `cat -A` shows `^M$` on a Notepad file; switch VS Code's CRLF to LF",
           "`file hello`: an ELF program, for GNU/Linux only",
           "`docker stop` / `docker start cssskl342`, then Reload Window",
           "A throwaway `docker run --rm -it cssimages/linuxlab bash`: where did your file go?",
           "Terminal only: `mkdir -p`, `cp`, `ls -R`, `rm -r`; and `Shift+Alt+F` formats your code"],
          kind="Hands-on",
          notes="Optional, not submitted. Full list and verified outputs on the Lab 1 page and in part0-answers.txt.")

d.walkthrough("Walkthrough 0",
              ["`sum.cpp` is `/home/cssuwbstudent/CSSSKL342/part0/made-on-my-computer/sum.cpp` in Linux "
               "and `C:\\Users\\you\\CSSSKL342\\part0\\...\\sum.cpp` on Windows: one file",
               "`rm` never uses the Recycle Bin, even in the shared folder; deleting in File Explorer does",
               "`~/outside.txt` lived only in the container: invisible to Windows, gone if the container is removed",
               "Linux's `g++` built `sum`: a Linux program, stored on your disk, runnable only in Linux"],
              notes="Redo steps 3-5 live with both windows side by side. If time allows, the case-sensitivity trap.")

d.selftest(0, ["Your container is deleted and re-created. Which of your files survive?",
               "You edit `main.cpp` in Notepad, then compile in VS Code's terminal. Does `g++` see the edits?",
               "`#include \"Node.h\"` with a file named `node.h` compiles in your shared folder. What happens on the Linux grader?",
               "You run `rm *.cpp` in the wrong folder. Can you get the files back from the Recycle Bin?"])

# ------------------------------------------------------------------ Part 1
d.divider(1, "How C++ programs are built",
          ["Split a program into `.h` and `.cpp` files correctly",
           "Tell a compiler error from a linker error, and know where to look",
           "Build with `make`, and check code with `cppcheck`"],
          why='In C++ you drive the build yourself; knowing the stages makes build errors easy to read',
          notes='In Java, `javac` finds your other classes for you. In C++, you tell the compiler which files to compile and the linker which pieces to join, and every multi-file CSS 342 assignment depends on getting this right. Most confusing build errors (`undefined reference`, `multiple definition`, `redefinition`) make sense once you know which stage is complaining.')

d.bullets_code("Three stages: preprocess, compile, link",
               ["The preprocessor pastes each `#include` in as text",
                "The compiler turns each `.cpp` into an object file `.o`, one at a time, without seeing the others",
                "The linker joins the `.o` files and matches every call to exactly one definition",
                "Java has no separate link step and no headers"],
               """main.cpp    + convert.h ──compile──▶ main.o    ┐
convert.cpp + convert.h ──compile──▶ convert.o ├─link─▶ temps
report.cpp  + convert.h ──compile──▶ report.o  ┘

g++ -std=c++17 -Wall -Wextra -g -c main.cpp
g++ -std=c++17 -Wall -Wextra -g -c convert.cpp
g++ -std=c++17 -Wall -Wextra -g -c report.cpp
g++ -o temps main.o convert.o report.o""", code_size=14, split=0.4,
               notes="Draw the pipeline on the board. Emphasize: each .cpp is compiled ALONE. "
                     "The only thing main.cpp knows about convert.cpp is what convert.h tells it.")

d.bullets_code("Declarations in headers, definitions in .cpp files",
               ["Declaration: \"this function exists, with this signature\"; definition: the body, written once",
                "The compiler needs only the declaration; the linker needs the definition",
                "An include guard stops a header being pasted twice into one `.cpp`: the second time, "
                "`#ifndef` is false and the whole file is skipped",
                "`#pragma once` does the same job in one line, with no macro name to invent; not in the "
                "standard, but g++, clang, and Visual C++ support it"],
               """// convert.h: include guard
#ifndef CONVERT_H
#define CONVERT_H
double celsiusToFahrenheit(double celsius);
#endif

// report.h: the same job, one line
#pragma once
void printRow(double celsius);

// convert.cpp
#include "convert.h"
double celsiusToFahrenheit(double c) {
    return c * 9.0 / 5.0 + 32.0;
}""", code_size=14,
               notes="Exercise 1 uses both: report.h already has #pragma once; convert.h has no protection yet "
                     "(students add a guard). The guard name must be unique per header. Guards are per translation "
                     "unit: they don't stop two different .cpp files from each getting a copy of a body.")

d.bullets_code("Global (free) functions",
               ["In C++ a function does not have to belong to a class",
                "`celsiusToFahrenheit` is declared in `convert.h`, defined in `convert.cpp`, and called by name "
                "from any file that includes the header",
                "No object and no class name in front; `main` is a global function too",
                "Java has nothing like this: the nearest equivalent is a `static` method such as `Math.sqrt`"],
               """// convert.h -- no class anywhere
double celsiusToFahrenheit(double celsius);

// main.cpp
#include "convert.h"

double f = celsiusToFahrenheit(100.0);
// not obj.celsiusToFahrenheit(...)
// not Convert::celsiusToFahrenheit(...)""",
               notes="Classes come in Lab 2. Until then, everything students write is global functions.")

d.bullets_code("#include <> vs \"\", and namespaces",
               ["`<...>`: a standard-library or system header; the compiler searches only the system include directories",
                "`\"...\"`: your own header; the compiler searches the including file's folder first, then the system directories",
                "The standard library is in the namespace `std`: `std::cout`, `std::string`",
                "`using namespace std;` lets a `.cpp` write just `cout`; never put it in a header",
                "Like Java: a namespace is a package; `using namespace std;` is `import java.util.*;`"],
               """#include <iostream>      // standard library
#include "convert.h"     // your header

using namespace std;     // .cpp files only

int main() {
    std::cout << "full name" << std::endl;
    cout << "short name" << endl;
}""",
               notes="Exercise 1's main.cpp has these comments and mixes std::cout with cout. "
                     "Many CSS 342 instructors prefer the explicit std:: form; both are correct.")

d.compare("Compiler error or linker error?",
          "Compiler error",
          ["Has a file name and line number: `main.cpp:12:5: error:`",
           "Comes from compiling one `.cpp`",
           "Typical causes: syntax, missing `#include`, wrong types, a header pasted twice",
           "Fix it at that line, or in a header that line uses"],
          "Linker error",
          ["No line number; mentions `.o` files",
           "`undefined reference to ...`: declared, but never defined (or misspelled)",
           "`multiple definition of ...`: defined in more than one `.o`, often a function body in a header",
           "Ends with `ld returned 1 exit status`"],
          notes="Have students read real messages. The first error is usually the real one; later ones cascade.")

d.bullets_code("make rebuilds only what changed",
               ["A rule: target, its dependencies, and the command to build it",
                "`make` compares file timestamps and reruns only stale rules",
                "Command lines must start with a TAB",
                "Always compile with `-Wall -Wextra`, and treat warnings as bugs",
                "`cppcheck --enable=all *.cpp` finds bugs the compiler accepts"],
               """CXX      = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -g

temps: main.o convert.o report.o
	$(CXX) $(CXXFLAGS) -o temps main.o convert.o report.o

main.o: main.cpp convert.h report.h
	$(CXX) $(CXXFLAGS) -c main.cpp

clean:
	rm -f *.o temps""".replace("\t", "    "),
               notes="CSS 342 instructors ask students to run cppcheck before asking for help (Lagesse syllabus).")

d.exercise(1, "Fix a broken multi-file build", "35 min", "Lab1/exercises/ex1-build/",
           ["Compile each `.cpp` alone with `g++ -std=c++17 -Wall -Wextra -c`; fix compiler errors and the warning",
            "Link the three `.o` files; fix linker errors",
            "Finish the `Makefile` (`convert.o`, `report.o`, `clean`); run `./temps`, type temperatures in F, `-999` quits",
            "`touch report.cpp`, run `make` again, and note what it rebuilds",
            "Run `cppcheck --enable=all *.cpp`"],
           "Confirm that `make` builds with no warnings and the program prints the expected output.",
           notes="Planted: missing include guard in convert.h (compile: redefinition), function body in header "
                 "(link: multiple definition), misspelled definition fahrenheitToCelcius (link: undefined reference), "
                 "sign-compare warning in main.cpp. report.h already has #pragma once and does not help: "
                 "convert.h is the file pasted twice.")

d.walkthrough("Walkthrough 1",
              ["Error 1, compiler: `redefinition of 'double clampToAbsoluteZero(double)'`. `main.cpp` includes `convert.h` twice (once through `report.h`). Fix: an include guard (or `#pragma once`) in `convert.h`",
               "Error 2, linker: `multiple definition of clampToAbsoluteZero`. Body in the header, so every `.cpp` gets a copy. Fix: move it to `convert.cpp` (or `inline`)",
               "Error 3, linker: `undefined reference to fahrenheitToCelsius(double)`. Defined as `fahrenheitToCelcius`",
               "Warning: `int i` compared with `unsigned int rows`. Make both `int`",
               "Fixed output: `0 C = 32 F` ... `100 C = 212 F`; -300 C clamps to `-459.67 F`; `-999` ends the input loop"],
              notes="Build the original live. After touch report.cpp, make reruns only report.o and the link.")

d.selftest(1, ["`g++ -c main.cpp` succeeds although `celsiusToFahrenheit()` is defined nowhere. Why is that not an error yet?",
               "`main.cpp:20:9: error: 'printRow' was not declared in this scope`. Compiler or linker? Likely cause?",
               "You edit only `convert.h` and run `make`. Which files are recompiled?",
               "`int helper() { return 1; }` sits in a guarded header included by two `.cpp` files. What happens? Two fixes?"])

# ------------------------------------------------------------------ Part 2
d.divider(2, "Types, conversions, and limits",
          ["Find the range of any numeric type with `numeric_limits`",
           "Predict integer division, overflow, and unsigned wraparound",
           "Convert safely with `static_cast`, at the right moment"],
          why='Types catch bugs early, but C++ sizes vary, overflow is silent, and conversions can lose data',
          notes='A type tells the compiler how many bytes a value takes and which operations make sense on it, so mistakes like multiplying a string are caught before the program ever runs. C++ types sit close to the hardware: their sizes can differ between machines, and an `int` that overflows silently wraps around instead of throwing. Real programs also mix types all the time (an average is a `double` computed from `int` totals; an index is compared with a size), so you need to know when C++ converts for you, when a conversion loses information, and how to convert on purpose with a cast.')

d.bullets_code("Sizes are not fixed in C++",
               ["`int` is usually 32 bits; `long` is 64 bits with g++ on Linux but 32 bits with Visual C++",
                "Ask the compiler: `numeric_limits<T>` in `<limits>`",
                "Unsigned types wrap around; `sizeof` and `.size()` return them",
                "Signed overflow is undefined behavior: anything can happen"],
               """#include <limits>

numeric_limits<int>::max()          // 2147483647
numeric_limits<int>::min()          // -2147483648

numeric_limits<double>::lowest()        // most negative
numeric_limits<double>::min()           // smallest POSITIVE!
numeric_limits<double>::epsilon()       // gap after 1.0

unsigned int u = 0;
u = u - 1;      // 4294967295""", code_size=14,
               notes="Run limits live on the lab image to show the real values.")

d.bullets_code("Reading std::numeric_limits<int>::min()",
               ["`std::` the standard library's namespace",
                "`numeric_limits` a template: a recipe that describes ANY numeric type, once told which one",
                "`<int>` fills in that type; angle brackets hold a TYPE, not a value (like Java's `ArrayList<Integer>`)",
                "`::` \"the thing on the right belongs to the thing on the left\"; compare `.`, which reaches into an object",
                "`min()` a function that belongs to `numeric_limits<int>`; Java: `Integer.MIN_VALUE`"],
               """std::numeric_limits<int>::min()

std::            in the standard library,
numeric_limits   the numeric limits
<int>            of the type int:
::min()          call its min()

std::numeric_limits<double>::max()
                 same recipe, for double

std::min(3, 7)   a DIFFERENT function
                 named min: no clash""", code_size=14, split=0.5,
               notes="Strictly, numeric_limits<int> is a type (a class), not a namespace; Lab 2 explains classes, "
                     "Lab 4 templates. The comment at the top of limits.cpp says the same.")

d.bullets_code("Arithmetic happens in the operands' type",
               ["The type of the result is decided before it is stored",
                "`int * int` overflows even if you store it in a `long long`",
                "`int / int` truncates toward zero, even if you store it in a `double`",
                "Cast an operand before the operation, not the result after",
                "Prefer `static_cast<double>(x)` to C-style `(double)x`"],
               """int big = 2000000000;
long long p = big * 2;   // overflow!
long long q =
    static_cast<long long>(big) * 2;    // ok

double h = 7 / 2;        // 3.0
double k = static_cast<double>(7) / 2;  // 3.5
double z = static_cast<double>(7 / 2);  // 3.0

double x = 0.1 + 0.2;
x == 0.3                 // false!
fabs(x - 0.3) < 1e-9        // true""",
               notes="The binary-search midpoint (low + high) / 2 overflow shows up in the self-test.")

d.compare("Coming from Java",
          "Java",
          ["Every type has a fixed size (`int` is always 32 bits)",
           "Integer overflow is defined: it wraps",
           "No unsigned integer types",
           "`(double) x` is the only cast syntax"],
          "C++",
          ["Sizes vary by platform; check with `numeric_limits`",
           "Signed overflow is undefined behavior",
           "Unsigned types wrap, and mixing them with signed values causes bugs",
           "Use `static_cast<T>(x)`; it is safer and easy to search for"])

d.exercise(2, "Rounding and numeric limits", "30 min", "Lab1/exercises/ex2-types/",
           ["Implement `int myRound(double)` in a new `rounding.cpp`: halves round away from zero, no `round`",
            "Add at least six test cases to `test_rounding.cpp`",
            "Write a `Makefile` that builds `test_rounding` and `limits`",
            "Read the comment at the top of `limits.cpp`, complete its TODOs, and run it"],
           "Confirm that `./test_rounding` reports 0 failures.")

d.walkthrough("Walkthrough 2",
              ["Casting to `int` truncates toward zero, so shift by 0.5 away from zero first",
               "`big * 2` overflows in `int` before it is stored; cast one operand to `long long`",
               "`-7 / 2` is `-3`: integer division truncates toward zero",
               "Bonus: is there a `double` where `myRound` and `round` disagree?"],
              code="""int myRound(double value) {
    if (value >= 0) {
        return static_cast<int>(value + 0.5);
    }
    return static_cast<int>(value - 0.5);
}""",
              notes="Bonus answer: 0.49999999999999994 + 0.5 rounds to 1.0 in double, so myRound gives 1; "
                    "round gives 0. Also: values beyond INT_MAX make the cast undefined.")

d.selftest(2, ["`int a = 5, b = 2; double r = a / b;` What is `r`? How do you get 2.5?",
               "When does `int mid = (low + high) / 2;` go wrong? What is the safer form?",
               "With an empty `string s`, how many times does `for (int i = 0; i < s.size() - 1; i++)` run?",
               "After `double x = 0.1 + 0.2;`, how should you test whether `x` is 0.3?"])

# ------------------------------------------------------------------ Part 3
d.divider(3, "References and parameter passing",
          ["Explain what a reference variable is: another name for an existing variable",
           "Choose between pass by value, `&`, and `const&`",
           "Return more than one result through reference parameters",
           "Return a reference safely, and spot a dangling one"],
          why='Every call works on your variable or on a copy; C++ lets you choose, for correctness and speed',
          notes="Every function call has to settle one question: does the function work on the caller's variable, or on a copy of it? Java decides for you (primitives are copied, objects are shared); C++ lets you choose for every parameter of every type. The choice affects correctness (can the function change my variable?) and speed (copying a large object on every call is costly), and `const &` gives you the speed without the risk.")

d.bullets_code("Reference variables: another name",
               ["`int &r = i;` makes `r` another name for `i`: no new `int` is created",
                "Changing `r` changes `i`; `&i` and `&r` are the same address",
                "`int x = i;` is different: a new `int` holding a copy",
                "A reference must be initialized when declared, and can never be re-pointed later"],
               """int i = 1;
int &r = i;     // r IS i
int x = r;      // x is a separate copy

r = 2;          // i = 2, r = 2, x = 1

&i == &r        // true: one variable
&i == &x        // false

int &xr;        // error: 'xr' declared as
                // reference but not initialized""",
               notes="From the original ReferenceDemo.cpp. Exercise 3 Part A has students run exactly this and print "
                     "the addresses. & in a declaration means reference; &x in an expression means address-of.")

d.bullets_code("Three ways to pass a parameter",
               ["By value: the function gets a copy, for every type, including objects",
                "By reference `&`: another name for the caller's variable",
                "By const reference `const&`: no copy, no changes",
                "In Java, a method can change an object you pass; in C++ an object parameter is a full copy unless you write `&`"],
               """void byValue(int n)       { n++; }  // caller unchanged
void byRef(int &n)        { n++; }  // caller changed

void show(const string &s);         // no copy, read-only

int x = 10;
byValue(x);    // x is 10
byRef(x);      // x is 11
byRef(5);      // error: 5 is not a variable""")

d.compare("Which one should I use?",
          "Rule of thumb for CSS 342",
          ["Built-ins (`int`, `double`, `char`, `bool`): by value",
           "Objects (`string`, your classes): by `const&`",
           "Plain `&` only when the function must change the argument",
           "Plain `&` also lets a function \"return\" several results"],
          "Examples from Exercise 3",
          ["`int countVowels(const string &word);`",
           "`void swapValues(int &a, int &b);`",
           "`void divide(int dividend, int divisor, int &quotient, int &remainder);`",
           "`void addOneByValue(int n);`"])

d.bullets_code("Returning a reference",
               ["A function returning `int&` can appear on the left of `=`",
                "This is how `operator[]` and `operator=` work (later labs)",
                "Never return a reference to a local variable: it is destroyed when the function returns",
                "g++ `-Wall` warns: reference to local variable returned"],
               """int &larger(int &a, int &b) {
    if (a >= b) return a;
    return b;
}
int p = 4, q = 9;
larger(p, q) = 0;     // sets q:  p = 4, q = 0
larger(p, q)++;       // now p:   p = 5, q = 0

int &badReference() {
    int local = 42;
    return local;     // dangling!
}""")

d.exercise(3, "References", "25 min", "Lab1/exercises/ex3-references/",
           ["Part A (given): run it; compare the values and addresses of `i`, `r`, `x`; uncomment `int &xr;` and read the error",
            "Part B: implement `addOneByReference`, `swapValues`, `divide`, `countVowels`; uncomment the matching lines",
            "Part C: implement `larger`, which returns a reference; uncomment its lines",
            "Compile with `g++ -std=c++17 -Wall -Wextra` and read the warning for `badReference`"],
           "Output ends with `17 / 5 = 3 remainder 2`, `5` vowels, `p = 4, q = 0`, `p = 5, q = 0`; only the `badReference` warning.",
           notes="Full expected output and answers: the private solutions, Lab1/ex3-references/answers.txt.")

d.walkthrough("Walkthrough 3",
              ["Part A: `r` and `i` share one address, so `r = 2` changes `i`; `x` is a copy and stays 1",
               "`addOneByReference(r)` changes `i`, because `r` IS `i`",
               "`const string&` avoids the copy, forbids changes, and accepts the literal `\"Data Structures\"`; plain `string&` does not",
               "`larger` returns `int&`, so the call IS `p` or `q`; returning `int` gives `lvalue required` errors",
               "Java cannot write `swapValues` for two `int`s: it always passes by value"])

d.selftest(3, ["Given `void g(int &n);`, which compile: `g(x)`, `g(5)`, `g(x + 1)`?",
               "`int a = 1, b = 7; int &r = a; r = b; r = r + 1;` What are `a` and `b`?",
               "What is wrong with `const string &longer(string a, string b)` returning `a` or `b`?",
               "Declare `printAll`, which prints a string without changing it, and `toUpper`, which changes it in place"])

# ------------------------------------------------------------------ wrap-up
d.submission(1,
             """Lab1/
└── exercises/
    ├── ex1-build/
    │     main.cpp convert.h convert.cpp
    │     report.h report.cpp
    │     Makefile
    ├── ex2-types/
    │     rounding.h rounding.cpp
    │     test_rounding.cpp limits.cpp
    │     Makefile
    └── ex3-references/
          references.cpp

(Part 0: nothing to submit;
 part0/ stays out of the zip)""",
             ["Your work is in `Lab1/exercises`, with subfolders named like the starter folders",
              "Run `make clean`; delete other `.o` files and executables; delete the `examples` folder",
              "Check: compiles with `-Wall -Wextra`; the only warning is the planted `badReference` one (Exercise 3)",
              "Zip the whole folder: `zip -r Lab1-netid.zip Lab1`",
              "Upload that one zip to the Lab 1 assignment on Canvas"])

d.takeaways(["`CSSSKL342` is one folder with two names. Keep your work in it; Linux names are case-sensitive and `rm` is forever.",
             "Headers declare, `.cpp` files define, the linker matches them up. Guard every header.",
             "Type sizes vary and arithmetic happens in the operands' type. Cast before the operation.",
             "A reference is another name for a variable. Pass objects by `const&`; use `&` only to change the caller's variable."])

out = os.path.join(LAB1, "Lab1-Slides.pptx")
d.save(os.path.abspath(out))
print("wrote", os.path.abspath(out), len(d.prs.slides), "slides")

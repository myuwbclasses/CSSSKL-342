"""Builds Lab5/Lab5-Slides.pptx.  Run:  python lab5_slides.py"""
import os
from slidekit import Deck

HERE = os.path.dirname(os.path.abspath(__file__))

d = Deck("Lab 5: Iterators and the Standard Library")

d.title("CSS SKL 342 · Lab 5", "Iterators and the Standard Library",
        "vector, string, and files · iterators · list and map · algorithms and lambdas",
        notes="Remind students: many CSS 342 assignments forbid the standard container that does the assignment's job. "
              "Know the library anyway: it's how you test your own containers, and what CSS 343 builds on.")

d.agenda([
    (1, "vector, string, and files", [("Lecture", "1:15", "20 min", "vector, string, and files"),
                                      ("Hands-on", "1:35", "35 min", "Vectors, words, files"),
                                      ("Solutions", "2:10", "10 min", "Walkthrough + self-test")]),
    (2, "Iterators", [("Lecture", "2:20", "15 min", "Using and writing"),
                      ("Hands-on", "2:35", "30 min", "Iterators"),
                      ("Solutions", "3:05", "10 min", "Walkthrough + self-test")]),
    (3, "list and map", [("Lecture", "3:25", "15 min", "More containers"),
                         ("Hands-on", "3:40", "25 min", "List, word count"),
                         ("Solutions", "4:05", "5 min", "Walkthrough + self-test")]),
    (4, "Algorithms and lambdas", [("Lecture", "4:10", "15 min", "Passing behavior"),
                                   ("Hands-on", "4:25", "30 min", "Students"),
                                   ("Solutions", "4:55", "10 min", "Walkthrough; catch-up 5:05")]),
], notes="Break 3:15-3:25. 5:05-5:15 is catch-up and wrap-up. The lecture examples are in Lab5/examples/ "
         "(they come with the starter zip).")

# ------------------------------------------------------------------ Part 1
d.divider(1, "vector, string, and files",
          ["Use `vector` and `string` instead of raw arrays and C strings",
           "Take a file name from the command line, open it, and read it with the right loop",
           "Take a line apart with `istringstream`, and spot Windows line endings"],
          why="The library's growable array and string, done right, and input from files named on the command line",
          notes="You've built growable arrays by hand; now use the standard library's. vector and string manage their "
                "own memory, copy correctly, and know their size. Most programs also read their input from files and "
                "command-line arguments rather than the keyboard, and CSS 342 assignments are often run that way. "
                "Knowing how these classes behave (when a vector reallocates, which index operations are unchecked) "
                "keeps you from bringing back the bugs they were made to prevent.")

d.bullets_code("vector: the array you built, done right",
               ["Knows its `size()`; grows with `push_back`; frees itself; copies deeply",
                "When `size() == capacity()`, `push_back` reallocates (usually doubling): Lab 3's `grow()`",
                "Reallocation invalidates pointers, references, and iterators into it",
                "`v[i]` doesn't check; `v.at(i)` throws `out_of_range`",
                "`size()` is unsigned: loop with range-for; pass by `const&`"],
               """vector<int> v = {8, 2, 14, 6, 10};
v.push_back(13);   // size 6, capacity 10

for (int n : v) {
    cout << n << " ";
}

v.at(100);         // throws out_of_range
v[100];            // undefined behavior

vector<vector<int>> table(
    3, vector<int>(4, 0));        // 3 x 4 zeros""")

d.bullets_code("string",
               ["Owns its characters and knows its `size()`: no `'\\0'` to manage",
                "`+` and `+=` join; `==` and `<` compare the CONTENTS (unlike `==` on Java strings)",
                "`substr(pos, len)`; `find` returns a position or `string::npos`",
                "`to_string(42)`; `stoi(\"42\")` throws `invalid_argument` on `\"abc\"`"],
               """string fruit = "pear";
string other = "pe";
other += "ar";
cout << (fruit == other);           // 1: same characters
cout << fruit.substr(1, 2);         // ea
cout << fruit.find("ar");           // 2
if (fruit.find("z") == string::npos) {
    cout << "no z in " << fruit;
}
string label = "item " + to_string(42);
int n = stoi("17") + 1;             // 18""",
               caption="Example 1.1.string_basics: also stoi(\"abc\") throwing invalid_argument.")

d.bullets_code("Files named on the command line",
               ["`main(int argc, char *argv[])`: `argv[0]` is the program; check `argc` first",
                "`ifstream in(argv[1]);` then `if (!in)`: did it open?",
                "On an error: a message to `cerr`, and `return 1;`",
                "Loop on the read itself: `while (in >> x)`, `while (getline(in, line))`",
                "`while (!in.eof())` runs once too often: `eof()` turns true only AFTER a read fails"],
               """int main(int argc, char *argv[]) {
    if (argc != 2) {
        cerr << "usage: " << argv[0] << " <file>" << endl;
        return 1;
    }
    ifstream in(argv[1]);
    if (!in) {
        cerr << "cannot open " << argv[1] << endl;
        return 1;
    }
    int value;
    int count = 0;
    while (in >> value) {      // RIGHT: the read is the test
        count++;
    }
    ...
}""",
               caption="Examples 1.2.argc_argv and 1.3.read_loop: the same 3-number file counts 3, then 4 with eof().",
               code_size=13)

d.bullets_code("Taking a line apart",
               ["`getline` reads a whole line; `istringstream` turns it into a stream",
                "`>>` then reads each field in its own type, skipping any whitespace",
                "A failed `>>` means a bad line: report it and keep going",
                "Windows files end lines in `\\r\\n`: `getline` keeps the `\\r`; `od -c` shows it"],
               """string line;
while (getline(cin, line)) {
    istringstream fields(line);
    string name;
    int age;
    double height;
    if (fields >> name >> age >> height) {
        cout << name << " is " << age << endl;
    } else {
        cerr << "bad line: \\"" << line << "\\"" << endl;
    }
}""",
               caption="Example 1.4.parse_line: \"Grace sixty 1.60\" is reported; the other lines print.")

d.exercise(1, "Vectors, words, and files", "35 min", "Lab5/exercises/ex1-vector/",
           ["`vectors.cpp` TODOs 1-6: average, print, size vs. capacity, sort, `at` vs. `[]`, a 2D table",
            "`words.cpp` TODO 1: check `argc` and the open file; errors to `cerr`, `return 1`",
            "`split`, `join`, `reversed`, and the `getline` loop",
            "`./words data/lines.txt`, `./words`, `./words nosuch.txt`; `echo $?` after each",
            "`./words data/lines_crlf.txt` and `od -c data/lines_crlf.txt | head -3`"],
           "Confirm that `./vectors` catches `out_of_range`, that `./words data/lines.txt` prints one line per input line, "
           "and that a missing argument or file gives a message and exit code 1.")

d.walkthrough("Walkthrough 1",
              ["Capacity 5, then 10 for the next five pushes: Lab 3's `grow()`",
               "`v.at(100)`: `vector::_M_range_check: __n (which is 100) >= this->size() (which is 10)`",
               "`./words` and `./words nosuch.txt`: a message on `cerr`, exit code 1",
               "`while (!in.eof())`: a 5th line, `5 (0 chars): 0 words:`",
               "`lines_crlf.txt`: every line one char longer; `od -c` shows `\\r \\n`"])

d.selftest(1, ["What do `vector<int> a(3);` and `vector<int> b{3};` contain?",
               "`int *p = &v[0]; v.push_back(7); cout << *p;` What can go wrong?",
               "What does `argc` equal for `./words data/a.txt data/b.txt`, and what is `argv[2]`?",
               "A file contains `10 20 abc 30`. What does `while (in >> x)` read?",
               "`line == \"END\"` matches on Windows but never on Linux, same file. Why?"])

# ------------------------------------------------------------------ Part 2
d.divider(2, "Iterators",
          ["Loop over any container with iterators",
           "Erase elements safely while iterating",
           "Write an iterator for your own linked container"],
          why="One loop, and the same algorithms, for every container: an array, a chain of nodes, or a tree",
          notes="Containers store their elements in very different ways (an array, a chain of nodes, a tree), yet you "
                "want to visit them all with the same loop. An iterator gives every container one way to say \"the "
                "current element\" and \"the next one\", so the same code and the same standard algorithms work on all "
                "of them. Range-based for loops are iterators underneath, and the containers you write for CSS 342 "
                "often need one.")

d.bullets_code("Using iterators",
               ["`*it` is the element; `++it` moves on",
                "`begin()` is the first element; `end()` is ONE PAST the last: never dereference it",
                "The same loop works on a vector, a list, a string, a map",
                "`auto it = v.begin();`: the compiler fills in `vector<int>::iterator`; still one fixed type, so it must be initialized",
                "Range-for is shorthand for it: `begin()`, `!=`, `++`, `*`",
                "`erase` returns the next valid iterator: `++it` only when you didn't erase",
                "`const_iterator` is read-only"],
               """vector<int> v = {3, 1, 4};
list<int> l = {1, 5, 9};
string s = "abc";

for (auto it = v.begin(); it != v.end(); ++it) {
    cout << *it << " ";              // 3 1 4
}
for (auto it = l.begin(); it != l.end(); ++it) {
    *it = *it * 10;                  // write through it
}
for (int n : l) {                    // range-for
    cout << n << " ";                // 10 50 90
}
for (auto it = s.rbegin(); it != s.rend(); ++it) {
    cout << *it;                     // cba
}""",
               caption="Example 2.1.same_loop_any_container.",
               code_size=13)

d.bullets_code("++ before and after: what each returns",
               ["An iterator for your own container: a small class holding a `Node *`",
                "It needs `*`, pre- and post-`++`, `==`, and `!=`; the container needs `begin()` and `end()`",
                "Pre (`++x`): move, return `*this` by reference",
                "Post (`x++`): the unused `int` marks it; save, move, return the OLD copy",
                "An iterator's `++` is written the same way"],
               """class Counter {
public:
    explicit Counter(int start) : n_(start) {}
    int value() const { return n_; }
    Counter &operator++() {     // ++c
        n_++;
        return *this;
    }
    Counter operator++(int) {   // c++
        Counter old = *this;
        n_++;
        return old;
    }
private:
    int n_;
};

Counter c(5);
Counter a = ++c;    // a 6, c 6
Counter b = c++;    // b 6, c 7""",
               caption="Example 2.2.pre_post_increment.",
               code_size=13)

d.exercise(2, "Iterators", "30 min", "Lab5/exercises/ex2-iterators/",
           ["`iterate.cpp` TODOs 1-5: an iterator loop, writing through `*it`, reverse, erase, `const_iterator`",
            "For TODO 4, also try the wrong loop (always `++it`) and compare",
            "`make list_test`: it doesn't link; read which functions are undefined",
            "Write `Iterator`'s pre- and post-increment, `==`, and `!=`",
            "`./list_test` and `make check`"],
           "Confirm that `./iterate` prints what you expect, and that `./list_test` matches its comments with a clean `make check`.")

d.walkthrough("Walkthrough 2",
              ["Right erase loop: `6 2 4`. Always `++it`: `6 2 18 4`: the element after each erase is skipped",
               "If the last element is erased, `++it` steps past `end()`: undefined behavior",
               "`for (int n : numbers)` expands into `begin()`, `end()`, `!=`, `++`, and `*`",
               "Assigning through a `const_iterator`: \"assignment of read-only location\"",
               "`find` and `count` work on `SimpleList`: algorithms only need iterators"])

d.selftest(2, ["Why do generic loops test `it != c.end()` rather than `it < c.end()`?",
               "A loop calls `v.push_back(1)` while iterating over `v`. What's wrong?",
               "Write the declaration of post-increment for an `Iterator` class",
               "What does `*v.end()` do?"])

# ------------------------------------------------------------------ Part 3
d.divider(3, "list and map",
          ["Use `list` and its member algorithms",
           "Count and look up with `map`, without accidental inserts",
           "Choose the right container for a job"],
          why="No one container is best at everything: choose the right one, and know its traps",
          notes="No one container is best at everything: a vector is fast to index but slow to insert into the middle, "
                "a linked list is the opposite, and looking items up by a key calls for something else again. The "
                "standard library has a container for each of these jobs, already written and tested. Choosing the "
                "right one, and knowing its traps (like map's [] quietly adding keys), is a skill you'll use in every "
                "larger program.")

d.bullets_code("map: look up by key",
               ["`list`: doubly linked; fast insert/erase anywhere; no `[]`; its own `sort()` and `remove_if()`",
                "`map<Key, Value>`: pairs kept sorted by key (a balanced BST, CSS 343)",
                "Each element is a `pair`: `.first` the key, `.second` the value",
                "`m[key]` ADDS a missing key (value 0); `m.find(key)` only looks",
                "`insert` doesn't overwrite an existing key"],
               """map<string, int> ext;
ext["Zoe"] = 4410;
ext["Amir"] = 4102;
ext.insert({"Mei", 4307});
ext.insert({"Mei", 9999});     // exists: no change

auto found = ext.find("Ravi"); // just looks
if (found == ext.end()) {
    cout << "Ravi not found";  // size still 3
}
cout << ext["Ravi"];           // 0: ADDS Ravi
                               // size now 4
for (const auto &entry : ext) {
    cout << entry.first << ": " << entry.second;
}                              // Amir, Mei, Ravi, Zoe""",
               caption="Example 3.1.map_lookup: phone extensions.",
               code_size=13)

d.compare("Choosing a container",
          "Default to...",
          ["`vector`: compact, fast, indexable",
           "`string` for text",
           "`map` to look things up by key, in sorted order",
           "`unordered_map` for faster lookup when order doesn't matter"],
          "...and reach for",
          ["`list` for many inserts/erases in the middle, with no indexing",
           "`set` for sorted keys with no values",
           "`stack` / `queue` when only those operations are allowed",
           "Your own class when the CSS 342 assignment says so: most do"])

d.exercise(3, "list and word count", "25 min", "Lab5/exercises/ex3-containers/",
           ["`lists.cpp` TODOs 1-7",
            "TODO 5: try `sort(numbers.begin(), numbers.end())` on the list, read the error, remove it",
            "`wordcount.cpp` TODOs 1-5",
            "Run `./wordcount data/sample.txt`"],
           "Confirm that `./lists` ends with `2 4 5 6 8 10`, and that the word counts look right.")

d.walkthrough("Walkthrough 3",
              ["`sort(begin, end)` on a list: \"no match for 'operator-'\": it needs random-access iterators",
               "So `list` has its own `sort()`, which relinks nodes",
               "`counts[w]++` works for a new word: `[]` inserts 0, then `++`",
               "Words print alphabetically: a map is sorted by key",
               "27 different words, before and after `find`: no accidental inserts"])

d.selftest(3, ["`map<string, int> m; if (m[\"x\"] == 0) {}` What is `m.size()` afterward?",
               "What type is each element of a `map<string, int>`? Can you change the key?",
               "`m.insert({\"a\", 5})` when `\"a\"` maps to 1. What is `m[\"a\"]` afterward?",
               "Why does `list` have a `remove_if` member when the general `remove_if` exists?"])

# ------------------------------------------------------------------ Part 4
d.divider(4, "Algorithms and lambdas",
          ["Customize `sort`, `find_if`, `count_if`, and `accumulate`",
           "Pass behavior with function pointers and lambdas",
           "Remove elements with the erase-remove idiom"],
          why="The loops are already written: pass in the rule (by name, or as a lambda right at the call)",
          notes="Sorting, searching, counting, and removing are written once in the standard library and work on any "
                "container through iterators, so you rarely need to write those loops yourself. What changes from one "
                "use to the next is the rule: sort students by name or by grade, count only the passing scores. C++ "
                "lets you pass that rule in as a function, and a lambda lets you write it right where you call the "
                "algorithm.")

d.bullets_code("Function pointers and lambdas",
               ["A comparator returns true when `a` comes BEFORE `b`; use `<`, never `<=`",
                "A function's name converts to a pointer to it",
                "A lambda is an unnamed function written in place",
                "`[minLength]` copies a local in; `[&x]` refers to it",
                "Like Java's `(a, b) -> ...`, but you choose how locals are captured"],
               """bool shorterFirst(const string &a, const string &b) {
    return a.size() < b.size();
}

sort(words.begin(), words.end(), shorterFirst);
sort(words.begin(), words.end(),
     [](const string &a, const string &b) { return a > b; });

size_t minLength = 4;
auto longOnes = count_if(words.begin(), words.end(),
    [minLength](const string &w) { return w.size() >= minLength; });

int x = 1;
auto byCopy = [x]() { return x; };
auto byRef = [&x]() { return x; };
x = 5;
cout << byCopy() << " " << byRef();   // 1 5""",
               caption="Example 4.1.lambdas: words sorted shortest first, then Z to A.",
               code_size=12)

d.bullets_code("Algorithm traps",
               ["`find_if` returns `end()` when nothing matches: check before using it",
                "`accumulate`'s result has the type of its start value: `0` truncates doubles",
                "`remove_if` doesn't shrink the vector: it moves the kept elements forward",
                "Then `erase` from the returned iterator to `end()`: the erase-remove idiom"],
               """vector<int> v = {1, 2, 3, 4, 5, 6};
auto newEnd = remove_if(v.begin(), v.end(),
                        [](int n) { return n % 2 == 0; });
// v: 1 3 5 4 5 6   (size 6: leftovers at the end)
v.erase(newEnd, v.end());
// v: 1 3 5         (size 3)

vector<double> g = {3.6, 2.9};
accumulate(g.begin(), g.end(), 0);     // 5
accumulate(g.begin(), g.end(), 0.0);   // 6.5""",
               caption="Example 4.2.erase_remove prints the vector after remove_if alone, and after erase.")

d.exercise(4, "Students", "30 min", "Lab5/exercises/ex4-algorithms/",
           ["Write `byId` and `sortBy` (TODOs 1-2); sort by name and by id (TODO 3)",
            "Sort by GPA, highest first, with a lambda (TODO 4)",
            "`find_if`, `count_if`, `accumulate` (TODOs 5-7): try starting at `0` and at `0.0`",
            "A capturing lambda (TODO 8), then erase-remove (TODO 9)"],
           "Confirm that `./students` runs to the end and finishes with the four remaining students.")

d.walkthrough("Walkthrough 4",
              ["Same `sort`, two ways to pass the comparison: a function pointer and a lambda",
               "Captures: `[minId]` copies the local; `[&total]` refers to it",
               "Erase-remove drawn on the vector: Kai, Mina, Lee, Ari remain",
               "`accumulate(..., 0)` gave 5 for 3.6 + 2.9: Lab 1's operand-type rule again",
               "Five labs: build, types, classes, pointers, memory, templates, copying, exceptions, and the library"])

d.selftest(4, ["Write a lambda that returns `true` for even `int`s",
               "`int x = 1; auto c = [x]() { return x; }; auto r = [&x]() { return x; }; x = 5;` What do `c()` and `r()` return?",
               "How do you sort a `vector<int>` descending without writing a lambda?",
               "After `remove(v.begin(), v.end(), 3);` alone, has `v.size()` changed?"])

# ------------------------------------------------------------------ wrap-up
d.submission(5,
             """Lab5/
└── exercises/
    ├── ex1-vector/
    │     vectors.cpp words.cpp
    │     Makefile
    │     data/ lines.txt lines_crlf.txt
    ├── ex2-iterators/
    │     iterate.cpp SimpleList.h
    │     list_test.cpp Makefile
    ├── ex3-containers/
    │     lists.cpp wordcount.cpp
    │     Makefile  data/
    └── ex4-algorithms/
          students.cpp Makefile""",
             ["Your work is in `Lab5/exercises`, with subfolders named like the starter folders",
              "Run `make clean` in each; delete executables; delete the `examples` folder",
              "Check: no warnings; `make check` clean for `list_test`",
              "Zip the whole folder: `zip -r Lab5-netid.zip Lab5`",
              "Upload that one zip to the Lab 5 assignment on Canvas"])

d.takeaways(["`vector` and `string` by default. Pass by `const&`; growing invalidates pointers.",
             "Files: check `argc`, check the open, loop on the read (never `eof()`), report on `cerr`, `return 1`.",
             "Iterators make every container look alike. `list` for linked behavior; `map` for sorted lookup.",
             "Pass behavior with function pointers or lambdas. Comparators use `<`. Erase-remove."],
            next_lab="That's all five labs. Good luck with your CSS 342 assignments!")

out = os.path.join(HERE, "..", "Lab5", "Lab5-Slides.pptx")
d.save(os.path.abspath(out))
print("wrote", os.path.abspath(out), len(d.prs.slides), "slides")

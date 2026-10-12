1.1.all_in_one_file -- same program, different organization

temps.cpp is Exercise 1's fixed program with everything in one file: the
conversion functions, printRow, and main. No headers, no Makefile:

$ g++ -std=c++17 -Wall -Wextra temps.cpp -o temps
$ ./temps

Its output is IDENTICAL to the five-file version from Exercise 1 (checked with
diff in the course image, feeding both 212, 32, -40, -999):

0 C = 32 F
25 C = 77 F
50 C = 122 F
75 C = 167 F
100 C = 212 F
98.6 F = 37 C
-300 C is below absolute zero: -459.67 F
Enter a temperature in F (-999 to quit): 212 F = 100 C
Enter a temperature in F (-999 to quit): 32 F = 0 C
Enter a temperature in F (-999 to quit): -40 F = -40 C
Enter a temperature in F (-999 to quit):
Bye!

So why split it up? How code is organized and whether the program is correct
are separate questions: the computer runs both versions the same way. The
organization is for PEOPLE. In the split version:
  - each file has one job, so you know where to look;
  - a header shows what a module offers without its details;
  - make recompiles only the file you changed;
  - other programs can reuse convert.h/.cpp;
  - two people can work on different files at once.
With 50 lines it hardly matters. With the thousands of lines of a real project
-- or a CSS 342 assignment you keep extending for weeks -- it decides whether
the code can still be read, fixed, and changed.

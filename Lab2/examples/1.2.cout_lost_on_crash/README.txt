1.2.cout_lost_on_crash -- cout can wait; cerr doesn't

crash.cpp prints a progress message with cout, WITHOUT a newline, then crashes
(integer division by zero). Output below is from the course image
(cssimages/linuxlab), run in VS Code's terminal.

$ g++ -std=c++17 -Wall -Wextra crash.cpp -o crash
$ ./crash
Floating point exception (core dumped)

The message is gone. cout keeps text in a buffer and writes it out later (on a
terminal: when a line ends); the crash killed the program first.

Fix A: cout << "step 1: about to divide" << endl;
$ ./crash
step 1: about to divide
Floating point exception (core dumped)

Fix B: cerr << "step 1: about to divide";        (still no newline)
$ ./crash
step 1: about to divideFloating point exception (core dumped)

cerr is written immediately, so even without a newline the message is there.

Same idea, worse: with "\n" instead of endl, the line DOES appear on a terminal,
but run ./crash > out.txt and out.txt is empty -- output going to a file waits
until much more of it has built up. That is how a grader runs your program.

Lesson: debug messages go to cerr.

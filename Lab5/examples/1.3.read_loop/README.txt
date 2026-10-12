1.3.read_loop -- opening a file, and the right and wrong read loops

nums.txt holds three numbers on two lines (od -c shows its bytes):
    0000000   1   0       2   0  \n   3   0  \n

Build and run (in the container):
    g++ -std=c++17 -Wall -Wextra read_loop.cpp -o read_loop
    ./read_loop nums.txt
    ./read_loop nosuch.txt

Output (g++ 11, cssimages/linuxlab):
    $ ./read_loop nums.txt
    while (in >> value): 3 values
    while (!in.eof()):   4 values
    $ ./read_loop nosuch.txt
    cannot open nosuch.txt
    $ echo $?
    1

- ifstream in(argv[1]); opens the file; if (!in) means it didn't open
  (wrong name, wrong folder). Check it, report it on cerr, return 1.
- RIGHT: while (in >> value). The read is the test: the loop runs once per
  value that was actually read, and stops when a read fails, at the end of
  the file or at bad data.
- WRONG: while (!in.eof()). After 30 is read, the '\n' after it is still
  unread, so eof() is still false. The loop runs a 4th time, the read FAILS
  (now eof() turns true), and the failed read is counted anyway. eof() only
  says what already happened; it can't predict that the next read will fail.
- The same goes for lines: use while (getline(in, line)).

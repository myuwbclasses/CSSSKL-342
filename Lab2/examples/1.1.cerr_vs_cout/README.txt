1.1.cerr_vs_cout -- cout vs. cerr

streams.cpp writes two result lines with cout and one debug line with cerr.
On the screen they look the same; redirecting shows they are two separate streams.
Output below is from the course image (cssimages/linuxlab).

$ g++ -std=c++17 -Wall -Wextra streams.cpp -o streams

$ ./streams
result: 42
debug: computing...
result: 99

$ ./streams > out.txt          # > redirects only cout
debug: computing...
$ cat out.txt
result: 42
result: 99

$ ./streams 2> err.txt         # 2> redirects only cerr
result: 42
result: 99
$ cat err.txt
debug: computing...

Why it matters: a grader runs ./prog > out.txt and compares out.txt with the
expected output. Debug messages sent to cerr stay out of that file, so they
can't make a correct program fail.

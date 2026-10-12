1.4.parse_line -- getline for whole lines, then istringstream to split each one

people.txt:
    Ada 36 1.65
    Linus   54   1.80
    Grace sixty 1.60
    Alan 41 1.75

Build and run (in the container):
    g++ -std=c++17 -Wall -Wextra parse_line.cpp -o parse_line
    ./parse_line < people.txt

Output (g++ 11, cssimages/linuxlab, in a terminal):
    Ada is 36, 1.65 m
    Linus is 54, 1.8 m
    bad line: "Grace sixty 1.60"
    Alan is 41, 1.75 m

- while (getline(cin, line)) reads one whole line per pass.
- istringstream fields(line); makes a stream that reads from the
  string, so >> works on it exactly as on cin or a file: it skips any
  amount of whitespace (Linus's extra spaces need no special code) and
  converts each field to its variable's type: string, int, double.
- if (fields >> name >> age >> height) is true only if all three reads
  worked. "sixty" isn't an int, so Grace's line is reported on cerr,
  and the loop simply goes on with the next line: one bad line doesn't
  break the rest of the input.
- Try ./parse_line < people.txt > out.txt: the three good lines go to
  out.txt, and only the "bad line" message appears on the screen.

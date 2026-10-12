1.2.argc_argv -- command-line arguments

Build and run (in the container):
    g++ -std=c++17 -Wall -Wextra args.cpp -o args
    ./args
    ./args Ada

Output (g++ 11, cssimages/linuxlab):
    $ ./args
    argc = 1
    argv[0] = ./args
    usage: ./args <name>
    $ echo $?
    1
    $ ./args Ada
    argc = 2
    argv[0] = ./args
    argv[1] = Ada
    hello, Ada
    $ echo $?
    0

- int main(int argc, char *argv[]): argc is the number of words on the
  command line, INCLUDING the program's own name; argv[0] is that name, and
  argv[1] ... argv[argc - 1] are the arguments, as C strings.
- Check argc before using argv[1]: with no argument, argv[1] isn't yours.
- On a usage error, write the message to cerr (so ./args > out.txt
  still shows it on the screen) and return nonzero from main. echo $? shows
  the exit code of the last command; scripts and graders check it.

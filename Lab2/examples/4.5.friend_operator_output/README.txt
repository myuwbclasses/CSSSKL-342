4.5.friend_operator_output -- operator<< with and without friend

Two tiny classes, one driver:
  Point   has public accessors x() and y(), so its operator<< uses those and
          needs no friend.
  Secret  has no accessor for code_, so the class declares its operator<< a
          FRIEND, which lets that one function read the private code_.
Both operator<< functions are non-member (global) functions.

Output from the course image (cssimages/linuxlab):

$ g++ -std=c++17 -Wall -Wextra friend_output.cpp -o friend_output
$ ./friend_output
(3, 4)
Secret #42
(3, 4) Secret #42

What the friend line does, and doesn't do:
  - friend ostream &operator<<(ostream &out, const Secret &s);  inside the class
    says "this global function may use my private members". That's all.
  - It does NOT make operator<< a member. The definition below the class is an
    ordinary global function: no "friend" and no "Secret::" in front.
  - It's the class that grants friendship. A function can't make itself a friend.

Try these, one at a time, then put the line back:

1. Delete the friend line from Secret:
   error: 'int Secret::code_' is private within this context
   (operator<< is now an ordinary outsider, and code_ is private.)

2. Write "friend" on the definition too  (friend ostream &operator<<(...) {):
   error: 'friend' used outside of class
   ("friend" belongs only on the declaration inside the class.)

3. Write "Secret::" on the definition  (ostream &Secret::operator<<(...) {):
   error: 'std::ostream& Secret::operator<<(std::ostream&, const Secret&)' must have exactly one argument
   (That would make it a MEMBER, whose left operand is a Secret -- but the left
   operand of cout << s is the stream. Which is exactly why operator<< is a
   non-member.)

When to use friend: only when the function truly needs private data. If the
class already has accessors (like Point), a plain non-member is simpler.

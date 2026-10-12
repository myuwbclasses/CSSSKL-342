4.4.why_nonmember -- why + is usually a non-member

MemberMoney and Money are identical except that MemberMoney writes + as a
MEMBER function and Money writes it as a NON-MEMBER (global) function. Both have
a constructor that takes one int, so the compiler can turn 2 into a Money.

Output from the course image (cssimages/linuxlab):

$ g++ -std=c++17 -Wall -Wextra why_nonmember.cpp -o why_nonmember
$ ./why_nonmember
member:     m + 2 = 502
non-member: n + 2 = 502
non-member: 2 + n = 502

Now uncomment the TRY THIS line (MemberMoney m2 = 2 + m;) and build again:

why_nonmember.cpp:53:24: error: no match for 'operator+' (operand types are 'int' and 'MemberMoney')

(g++ then prints many "note: candidate" lines about unrelated operator+
functions in the standard library; the first line is the one that matters.)

Why:
  - With a MEMBER +, m + 2 means m.operator+(2). The 2 is an ARGUMENT, and the
    compiler converts arguments: 2 becomes MemberMoney(2). Fine.
  - 2 + m would mean 2.operator+(m). But 2 is an int, and an int has no member
    functions. The compiler never converts the object a member function is
    called ON, so there is nothing to call: error.
  - With a NON-MEMBER +, n + 2 is operator+(n, 2) and 2 + n is operator+(2, n).
    Both operands are ordinary arguments, so 2 converts either way.

Rule: write + - * / == != < (anything that should work with the operands in
either order) as non-members. Write += -= = [] as members: their left operand
must be an existing object of your class anyway.

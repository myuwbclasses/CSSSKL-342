4.2.return_this -- why += returns *this by reference

Money::operator+= adds to the object it is called on and returns *this, "the
current object", by reference. Output from the course image (cssimages/linuxlab):

$ g++ -std=c++17 -Wall -Wextra return_this.cpp -o return_this
$ ./return_this
total = 123

(total += a) += b  is  total.operator+=(a).operator+=(b). The first call returns
total itself, so the second call also adds to total: 100 + 20 + 3 = 123.

Change the return type from Money & to Money (by value) and run it again:
total = 120
Now the first call returns a COPY of total; the second += adds 3 to that copy,
which is then thrown away.

Read *this as one phrase for now: "the object this member function was called
on". (Why it's written with a * comes later, with pointers.) The same pattern
makes  a = b = c  work for assignment.

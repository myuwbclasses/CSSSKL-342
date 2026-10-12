# Makefile for Exercise 1. -g puts line numbers and variable names into the
# program, so gdb and the VS Code debugger can show them.
# Each command line must start with a TAB.

CXX      = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -g

grades: grades.cpp
	$(CXX) $(CXXFLAGS) -o grades grades.cpp

clean:
	rm -f grades out.txt

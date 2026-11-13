# Makefile for Exercise 2 -- GIVEN: builds the rounding tests and the limits program.
# Compare it with your Exercise 1 Makefile: the same kinds of rules.
# Each command line must start with a TAB.

CXX      = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -g

all: test_rounding limits

test_rounding: test_rounding.o rounding.o
	$(CXX) $(CXXFLAGS) -o test_rounding test_rounding.o rounding.o

test_rounding.o: test_rounding.cpp rounding.h
	$(CXX) $(CXXFLAGS) -c test_rounding.cpp

rounding.o: rounding.cpp rounding.h
	$(CXX) $(CXXFLAGS) -c rounding.cpp

limits: limits.cpp
	$(CXX) $(CXXFLAGS) -o limits limits.cpp

clean:
	rm -f *.o test_rounding limits

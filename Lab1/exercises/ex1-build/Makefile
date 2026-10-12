# Makefile for Exercise 1 -- PARTIAL. Finish it (see the handout).
# IMPORTANT: each command line under a target must start with a TAB, not spaces.

CXX      = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -g

# Link step: combine the object files into the executable.
temps: main.o convert.o report.o
	$(CXX) $(CXXFLAGS) -o temps main.o convert.o report.o

# Compile step: one rule per .cpp file. main.o is done for you.
main.o: main.cpp convert.h report.h
	$(CXX) $(CXXFLAGS) -c main.cpp

# TODO: add a rule for convert.o
# TODO: add a rule for report.o
# TODO: add a "clean" target that removes the .o files and temps

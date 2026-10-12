CXX      = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -g

all: iterate list_test

iterate: iterate.cpp
	$(CXX) $(CXXFLAGS) -o iterate iterate.cpp

list_test: list_test.cpp SimpleList.h
	$(CXX) $(CXXFLAGS) -o list_test list_test.cpp

check: list_test
	valgrind --leak-check=full ./list_test

clean:
	rm -f iterate list_test

CXX      = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -g

stack_test: stack_test.cpp LinkedStack.h
	$(CXX) $(CXXFLAGS) -o stack_test stack_test.cpp

check: stack_test
	valgrind --leak-check=full ./stack_test

clean:
	rm -f stack_test

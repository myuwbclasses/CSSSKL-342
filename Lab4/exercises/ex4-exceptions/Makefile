CXX      = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -g

all: exceptions_test raii

exceptions_test: exceptions_test.o rational.o
	$(CXX) $(CXXFLAGS) -o exceptions_test exceptions_test.o rational.o

exceptions_test.o: exceptions_test.cpp ArrayStack.h PrecondViolatedExcept.h rational.h
	$(CXX) $(CXXFLAGS) -c exceptions_test.cpp

rational.o: rational.cpp rational.h
	$(CXX) $(CXXFLAGS) -c rational.cpp

raii: raii.cpp
	$(CXX) $(CXXFLAGS) -o raii raii.cpp

check: raii
	valgrind --leak-check=full ./raii

clean:
	rm -f *.o exceptions_test raii

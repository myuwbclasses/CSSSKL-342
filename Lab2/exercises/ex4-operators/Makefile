CXX      = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -g

test_operators: test_operators.o rational.o
	$(CXX) $(CXXFLAGS) -o test_operators test_operators.o rational.o

test_operators.o: test_operators.cpp rational.h
	$(CXX) $(CXXFLAGS) -c test_operators.cpp

rational.o: rational.cpp rational.h
	$(CXX) $(CXXFLAGS) -c rational.cpp

clean:
	rm -f *.o test_operators

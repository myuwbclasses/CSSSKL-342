CXX      = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -g

chain_test: chain_test.o nodes.o
	$(CXX) $(CXXFLAGS) -o chain_test chain_test.o nodes.o

chain_test.o: chain_test.cpp nodes.h
	$(CXX) $(CXXFLAGS) -c chain_test.cpp

nodes.o: nodes.cpp nodes.h
	$(CXX) $(CXXFLAGS) -c nodes.cpp

# Run the tests under valgrind.
check: chain_test
	valgrind --leak-check=full --error-exitcode=1 ./chain_test

clean:
	rm -f *.o chain_test

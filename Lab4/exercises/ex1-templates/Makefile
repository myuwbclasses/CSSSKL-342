CXX      = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -g

# entry.cpp is compiled only while it exists: Part B, TODO 1 deletes it.
templates_test: templates_test.cpp sorting.h entry.h $(wildcard entry.cpp)
	$(CXX) $(CXXFLAGS) -o templates_test templates_test.cpp $(wildcard entry.cpp)

check: templates_test
	valgrind --leak-check=full ./templates_test

clean:
	rm -f templates_test

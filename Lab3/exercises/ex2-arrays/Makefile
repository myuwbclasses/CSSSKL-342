CXX      = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -g

arrays: arrays.cpp
	$(CXX) $(CXXFLAGS) -o arrays arrays.cpp

check: arrays
	valgrind --leak-check=full ./arrays

clean:
	rm -f arrays

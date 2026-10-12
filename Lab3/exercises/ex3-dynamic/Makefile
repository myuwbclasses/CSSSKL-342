CXX      = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -g

all: growing leaky

growing: growing.cpp
	$(CXX) $(CXXFLAGS) -o growing growing.cpp

leaky: leaky.cpp
	$(CXX) $(CXXFLAGS) -o leaky leaky.cpp

check: growing leaky
	valgrind --leak-check=full ./growing
	valgrind --leak-check=full ./leaky

clean:
	rm -f growing leaky

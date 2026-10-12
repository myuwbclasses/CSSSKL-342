CXX      = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -g

all: lifetime counter_test

lifetime: lifetime.cpp tracer.cpp tracer.h
	$(CXX) $(CXXFLAGS) -o lifetime lifetime.cpp tracer.cpp

counter_test: counter_test.cpp counter.h
	$(CXX) $(CXXFLAGS) -o counter_test counter_test.cpp

clean:
	rm -f lifetime counter_test

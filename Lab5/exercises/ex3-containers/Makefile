CXX      = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -g

all: lists wordcount

lists: lists.cpp
	$(CXX) $(CXXFLAGS) -o lists lists.cpp

wordcount: wordcount.cpp
	$(CXX) $(CXXFLAGS) -o wordcount wordcount.cpp

clean:
	rm -f lists wordcount

CXX      = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -g

all: vectors words

vectors: vectors.cpp
	$(CXX) $(CXXFLAGS) -o vectors vectors.cpp

words: words.cpp
	$(CXX) $(CXXFLAGS) -o words words.cpp

clean:
	rm -f vectors words

CXX      = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -g

rational_app: main.o rational.o
	$(CXX) $(CXXFLAGS) -o rational_app main.o rational.o

main.o: main.cpp rational.h
	$(CXX) $(CXXFLAGS) -c main.cpp

rational.o: rational.cpp rational.h
	$(CXX) $(CXXFLAGS) -c rational.cpp

clean:
	rm -f *.o rational_app

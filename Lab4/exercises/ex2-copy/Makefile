CXX      = g++
CXXFLAGS = -std=c++17 -Wall -Wextra -g

copy_test: copy_test.o intarray.o
	$(CXX) $(CXXFLAGS) -o copy_test copy_test.o intarray.o

copy_test.o: copy_test.cpp intarray.h
	$(CXX) $(CXXFLAGS) -c copy_test.cpp

intarray.o: intarray.cpp intarray.h
	$(CXX) $(CXXFLAGS) -c intarray.cpp

check: copy_test
	valgrind --leak-check=full ./copy_test

clean:
	rm -f *.o copy_test

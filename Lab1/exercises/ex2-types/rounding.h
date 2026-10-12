// rounding.h -- declaration of myRound.
#ifndef ROUNDING_H
#define ROUNDING_H

// Rounds value to the nearest int, with halves rounded away from zero:
//    2.5 -> 3,   2.4 -> 2,   -2.4 -> -2,   -2.5 -> -3
// Do NOT call std::round (or lround, floor, ceil) in your implementation.
int myRound(double value);

#endif

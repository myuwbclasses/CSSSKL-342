/*
 *  Square.cpp
 *  Class-example
 *
 */

#include "Square.h"

void Square::setSize(int newSize)
{
   theSize = newSize;
}


int Square::getSize(void) const
{
   return theSize;
}

Square& Square::operator = (const Square& other)
{
	theSize = other.getSize();
	return *this;
}
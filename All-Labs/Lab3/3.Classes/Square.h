/*
 *  Square.h
 *  Class-example
 *
 */

#ifndef SQUARE_H
#define SQUARE_H

class Square {
public:
   void setSize(int newSize);
   int getSize(void) const;
   Square& operator = (const Square&);

private:
   int theSize;
   
};

#endif

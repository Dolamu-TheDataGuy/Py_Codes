#include <stdio.h>

int area_of_a_circle (int radius) {
  float pi = 3.142;
  int area = pi * (radius * radius);
  return area;
}

int main () {
  int r1 = 5;
  int r2 = 10;
  int area1 = area_of_a_circle(r1);
  int area2 = area_of_a_circle(r2);
  printf("The area of the circle with radius of %d is %d\n",r1, area1);
  printf("The area of the circle with radius of %d is %d\n",r2, area2);
  return 0;
}
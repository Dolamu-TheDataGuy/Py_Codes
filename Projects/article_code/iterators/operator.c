#include <stdio.h>

int main(void)
{
    int choice = 5;

    int row = --choice/3;

    int column = choice%3;

    printf("The value is %d\n", row);
    printf("The value is %d\n", column);


}


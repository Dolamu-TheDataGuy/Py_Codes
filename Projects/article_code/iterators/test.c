#include <stdio.h>

int main(void)
{
    int numbers[10];
    int count = 10;
    long sum = 0;
    float average = 0.0;

    printf("\nEnter the 10 numbers:\n");

    for(int i = 0; i< count; i++)
    {
        printf("%2d> ", i+1);
        scanf("%d", &numbers[i]);
        sum += numbers[i];
    }

    average = (float)sum/count;

    int number[3][4] = {
                            {10, 20, 30, 40},
                            {20, 15, 25, 39},
                            {30, 36, 42, 48},

                        };


    /*2 layers, 3 rows, 4 columns*/
    int numb[2][3][4] = {
                                {
                                    {10, 20, 30, 40},
                                    {15, 25, 35, 45},
                                    {23, 45, 56, 32}

                                },
                                {
                                  
                                    {10, 20, 30, 40},
                                    {15, 25, 35, 45},
                                    {23, 48, 56, 36}  
                                }
        
                            };

    printf("\nAverage of the ten numbers entered is: %f\n", average);
    printf("The size of an integer on my computer is %ld bytes", sizeof(int));
}


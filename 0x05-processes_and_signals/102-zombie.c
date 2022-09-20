#include <stdio.h>

int main()
{
    int zid; /*zombieID*/
    int loopi = 1;
    while (loopi < 6)
    {
        printf("Zombie process created, PID: %d\n", zid);
        loopi++;
        sleep(1);
    }
}

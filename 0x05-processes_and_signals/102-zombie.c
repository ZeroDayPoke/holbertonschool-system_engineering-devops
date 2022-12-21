#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - Function that runs an infinite loop
 * Return: Always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - zombie factory
 * Return: Always 0
 */
int main(void)
{
	pid_t pidZ;
	int i;

	for (i = 0; i < 5; i++)
	{
		pidZ = fork();
		if (pidZ == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}
	infinite_while();
	return (0);
}

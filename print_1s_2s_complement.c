#include<stdio.h>
#include<stdlib.h>
int main()
{
	int n;
	scanf("%d",&n);
	printf("1's complement = %d\n",~n);
	printf("2's complement = %d\n",~n+1);
}

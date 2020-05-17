#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int sockMerchant(int n, int ar_count, int* ar) {
    int i,j,count=0,result=0,p,count1=0;
for(i=0;i<n;i++)
{
    count=0;
    count1=0;
     for(p=0;p<i;p++)
        {
            if(*(ar+p)==*(ar+i))
            {
            count1=count1+1;
            }
        }
        if(count1>0)
        continue;
    for(j=i;j<n;j++)
    {
    if(*(ar+i)==*(ar+(j+1)))
       count=count+1;
    } 
    if(count%2==0)
        result=result+(count)/2;
    else if(count==1)
            result=result+(count);
            else
        result=result+(count+1)/2;
}
return result;
}

int main()
{
 	int n;
	scanf("%d",&n);
	int i=0;
	int array[100000];
	int ar_count = n;
	for(i=0;i<n;i++)
	{
		scanf("%d",&array[i]);
	}
	int result = sockMerchant(n, ar_count, array);
	printf("%d\n",result);
}

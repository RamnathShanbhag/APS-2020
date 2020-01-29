#include<stdio.h>
#include<stdlib.h>
int rod_cutting(int n);
int max(int a,int b,int c);
int main()
{
	int n;
	int size;
	printf("Enter the integer\n");
	scanf("%d",&n);
	size=rod_cutting(n);
	printf("%d\n",size);
}
int max(int a,int b,int c)
{
	int maximum;
	maximum=a;
	if(a>=b && a>=c)
	{
		maximum=a;
	}
	else if(b>=a && b>=c)
	{
		maximum=b;
	}
	else if(c>=a && c>=b)
	{
		maximum=c;
	}
	//printf("max= %d\n",maximum);
	return maximum;
}
int rod_cutting(int n)
{
	int arr[n+1];
	arr[0]=0;
	arr[1]=0;
	int i,j;
	for(i=2;i<=n;i++)
	{
		arr[i]=0;
		for(j=1;j<=(i/2);j++)
		{
			arr[i]=max(arr[i],j*(i-j),j*(arr[i-j]));
		}
	}
	for(i=0;i<n+1;i++)
	{
		printf("%d\n",arr[i]);
	}
	return arr[n];
}


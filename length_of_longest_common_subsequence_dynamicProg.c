#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int longest_common_subseq(char [],char []);
int maximum(int a,int b);
int main()
{
	char s1[100];
	char s2[100];
	printf("Enter two strings\n");
	scanf("%s%s",s1,s2);
	int n;
	n=longest_common_subseq(s1,s2);
	printf("The length of longest possible common subsequence string is %d\n",n);
}
int maximum(int a,int b)
{
	if(a>b)
	{
		return a;
	}
	else 
		return b;
}
int longest_common_subseq(char s1[100],char s2[100])
{
	int l1=strlen(s1);
	int l2=strlen(s2);
	int a[l1+1][l2+1];
	int i,j,max;
	for(i=0;i<l1+1;i++)
	{
		for(j=0;j<l2+1;j++)
		{
			if(i==0)
			{
				a[i][j]=0;
			}
			else if(j==0)
			{
				a[i][j]=0;
			}
			else
			{
				if(s1[i-1]==s2[j-1])
				{
					a[i][j]=a[i-1][j-1]+1;
				}
				else
				{
					max=maximum(a[i][j-1],a[i-1][j]);
					a[i][j]=max;
				}
			}
		}
	}
	for(i=0;i<l1+1;i++)
	{
		for(j=0;j<l2+1;j++)
		{
			printf("%d\t",a[i][j]);
		}
		printf("\n");	
	}
	return a[l1][l2];
}


			
	


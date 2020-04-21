#include<iostream>
using namespace std;

int subarray(int array[100000],int n)
{
	int x=0;
	for (int i = 0; i < n; i++)
	{
		x=max(x,array[i]);
	}
	int ans=0;
	for(int i=0;i<n;i++)
	{
		if(array[i]!=x)
		{
			continue;
		}
		int j=i;
		while(array[j]==x)
		{
			j++;
		}
		ans=max(ans,j-1);
	}
	return(ans);
}
int main()
{
	int n,array[100000];
	cout<<"Enter the array size\n";
	cin>>n;
	cout<<"Enter the array elements\n";
	for(int i=0;i<n;i++)
	{
		cin>>array[i];
	}
	int res=subarray(array,n);
	cout<<res<<"\n";
}

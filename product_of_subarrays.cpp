#include<iostream>
using namespace std;
int subarrayProduct(int array[100000],int n)
{
	int prod=1;
	for(int i=0;i<n;i++)
	{
		for(int j=i;j<n;j++)
		{
			prod*=array[j];
		}
	}
	cout<<prod<<"\n";
	return(prod);
}
int main()
{
	int n,array[100000];
	cout<<"Enter the array size\n";
	cin>>n;
	for(int i=0;i<n;i++)
	{
		cin>>array[i];
	}
	int product=subarrayProduct(array,n);
	cout<<"The product of all subarrays is\t"<<product<<"\n";
}


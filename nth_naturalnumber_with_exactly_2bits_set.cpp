#include<iostream>
using namespace std;
long long int findNumber(long long int n)
{
	long long int bit=1,num=0;
	while(bit*(bit+1)/2<n)
	{
		num+=bit;
		bit++;
	}
	int bitR=n-num-1;
	return((1<<bit)+(1<<bitR));
}
int main()
{
	long long int n;
	cin>>n;
	long long int res=findNumber(n);
	cout<<res<<"\n";
}

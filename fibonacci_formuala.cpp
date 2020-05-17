#include<iostream>
#include<math.h>
using namespace std;

long int fibonacci(long int n)
{
	double phi = (1 + sqrt(5)) / 2; 
  	return round(pow(phi, n) / sqrt(5));	
}
int main()
{
	long int n;
	cin>>n;
	long int res=fibonacci(n);
	cout<<res<<"\n";	
}


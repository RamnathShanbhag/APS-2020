#include<iostream>
using namespace std;
void update(int BIT[],int n,int index,int val)
{
	for(;index<=n;index+=(index&-index))
	{
		BIT[index]+=val;
	}
}
int query(int BIT[],int x)
{
	int sum=0;
	for(;x>0;x=x-(x&-x))
	{
		sum+=BIT[x];
	}
	return sum;
}
int Inverse(int arr[], int n) 
{ 
    int inverse = 0; 
    int ele = 0; 
    for (int i=0; i<n; i++) 
        if (ele < arr[i]) 
            ele = arr[i];
    int BIT[ele+1]; 
    for (int i=1; i<=ele; i++) 
        BIT[i] = 0;  
    for (int i=1; i<=ele; i++) 
        BIT[i] = 0;  
    for (int i=n-1; i>=0; i--) 
    {  
        inverse += query(BIT,arr[i]-1);  
        update(BIT,ele, arr[i], 1); 
    }   
    return inverse; 
} 
int main()
{
	int t;
	int n;
	int res;
	int a[1000];
	cin>>t;
	for(int i=0;i<t;i++)
	{	
		cin>>n;
		for(int j=0;j<n;j++)
		{
			cin>>a[j];
		}
		res=Inverse(a,n);
		cout<<res<<endl;
		if(res>n)
		{
			cout<<"YES"<<endl;
		}
		else
		{
			cout<<"NO"<<endl;
		}
	}
}

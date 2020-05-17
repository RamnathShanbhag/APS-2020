#include<stdio.h>
#include<stdlib.h>
int arr[100000];
void reverseArray(int arr[], int start, int end) 
{ 
   int temp; 
   if (start >= end) 
     return; 
   temp = arr[start];    
   arr[start] = arr[end]; 
   arr[end] = temp; 
   reverseArray(arr, start+1, end-1);    
}      
  
void printArray(int arr[], int size) 
{ 
  int i; 
  for (i=0; i < size; i++) 
    printf("%d ", arr[i]); 
  printf("\n"); 
}  
  
int main()  
{ 
    int n;
    printf("Enter the size\n");
    scanf("%d",&n);
    int i=0;
    printf("Enter the array elements\n");
    for(i=0;i<n;i++)
    {
	scanf("%d",&arr[i]);
    }
    reverseArray(arr, 0, n); 
    printf("Reversed array is \n"); 
    printArray(arr, n);     
    return 0; 
} 

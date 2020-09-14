#include<iostream>
using namespace std;

void sortit(int arr[], int n)
{
    for(int i=0; i<n; i++)
    {
        arr[i] = i+1;
    }
}
int main()
{
    int arr[] = {10, 7, 9, 2, 8, 3, 5, 4, 6, 1};
    int n = sizeof(arr) / sizeof(int);
    sortit(arr, n);

    for(int i=0; i<n; i++)
        cout<<arr[i]<<" ";
    cout<<endl;
    return 0;
}
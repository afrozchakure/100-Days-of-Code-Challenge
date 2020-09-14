#include<iostream>
using namespace std;

void InsertionSort(int arr[], int n)
{
    int key;
    for(int i=1; i<n; i++)
    {
        key = arr[i];
        int j = i-1;
        while(j >=0 && arr[j] > key)
        {
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = key;
    }
}
int main()
{
    int arr[] = {12, 11, 13, 5, 2};
    int n = sizeof(arr) / sizeof(int);
    InsertionSort(arr, n);
    for(int i=0; i<n; i++)
        cout<<arr[i]<<" ";
    return 0;
}

// Time Complexity - O(n**2)
// Space Complexity - O(1)

// Worst Case (n**2) - if array sorted in descending order
// Best Case (n) - If array already sorted

// Used when number of elements is less
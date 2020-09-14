// Selection Sort  

// Select the minimum element from unsorted part 
// and place it at the beginning

#include<iostream>
using namespace std;

void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}
void selectionSort(int arr[], int n)
{
    int min_idx;
    for(int i=0; i<n-1; i++)
    {
        min_idx = i;
        for(int j=i+1; j<n; j++)
        {
            if(arr[min_idx] > arr[i])
                arr[min_idx] = arr[i];
        }
        if(min_idx != i)
            swap(arr[min_idx], arr[i]);
    }
}
int main()
{
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr) / sizeof(int);
    selectionSort(arr, n);
    for(int i=0; i<n; i++)
        cout<<arr[i]<<" ";
    cout<<endl;
    return 0;
}

// Time Complexity - O(n**2)
// Space Complexity - O(1)

// Can be useful when memory write is costly
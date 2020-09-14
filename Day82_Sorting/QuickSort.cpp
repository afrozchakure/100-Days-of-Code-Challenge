// QuickSort 
// Follows Devide and Conquer
// Pick first element as pivot and assign high and low
// We partition the array around the picked pivot

// Idea is to put all the elements smaller than pivot before it
// and all elements larger than pivot after the pivot

#include<iostream>
using namespace std;
void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}
int partition(int arr[], int low, int high)
{
    int pivot = arr[low];  // pivot
    int i=low, j = high;
    while(i <= j)
    {
        do{i++;} while(arr[i] <= pivot);
        do{j--;} while(arr[j] > pivot);
        if(i < j) swap(&arr[i], &arr[j]);
    }
    swap(&arr[low], &arr[j]);
    return j;
}
void QuickSort(int arr[], int low, int high)
{
    if(low < high)
    {
        int j = partition(arr, low, high);
        QuickSort(arr, low, j-1);
        QuickSort(arr, j+1, high);
    }
}
int main()
{
    int arr[] = {10, 7, 88, 9, 5, 1};
    int n = sizeof(arr) / sizeof(int);
    QuickSort(arr, 0, n);
    for(int i=0; i<n; i++)
        cout<<arr[i]<<" ";
    cout<<endl;
    return 0;
}

// Time Complexity - O(n**2)
// Space Complexity - O(1)

// Best Case -> O(nlogn) - When we pick the middle element as the pivot
// Worst Case O(n**2) -> When the array is already sorted
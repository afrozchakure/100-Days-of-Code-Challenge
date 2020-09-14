#include<iostream>
#include<bits/stdc++.h>
using namespace std;
void printArr(int arr[], int n)
{
    for(int i=0; i<n; i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}
bool compare(int a, int b)
{
    // If both are even, return the one with smallest value
    if(a % 2==0 && b % 2 == 0)
        return a < b;
    // If both are ood, return the one which is bigger
    if(a % 2 != 0 && b % 2 != 0)
    {
        return b < a;
    }
    // If one is odd and other is even, odd should come to left side
    if(a % 2 != 0)
    {
        return true;
    }
    // if one is even and other odd
    else{
        return false;
    }
}
int main()
{
    int arr[] = {1, 2, 3, 5, 4, 7, 10};
    int n = sizeof(arr)/ sizeof(int);
    
    // Sorting the array using comparator
    sort(arr, arr+n, compare);
    printArr(arr, n);
    int M = 4;
    int remain = n - M;
    // Sorting the First 4 elements in Ascending order
    sort(arr, arr + 4);
    printArr(arr, n);
    // Sorting the next elements in Descending order
    sort(arr+4, arr+n, greater<int>());
    printArr(arr, n);
    return 0;
}

// Time Complexity - O(nlogn)
// Space Complexity - O(1)

// first part contains odd numbers in descending
// second par contains even numbers in ascending

// Conditions :
// 1. When both the elements are even: In this case, the smaller element must appear in the left of the larger element in the sorted array.
// 2. When both the elements are odd: The larger element must appear on left of the smaller element.
// 3. One is odd and the other is even: The element which is odd must appear on the left of the even element.


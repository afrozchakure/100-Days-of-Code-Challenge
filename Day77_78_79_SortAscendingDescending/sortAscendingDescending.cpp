#include<iostream>
using namespace std;
#include<bits/stdc++.h>

int main()
{
    int N = 9;
    int array[] = {5, 4, 6, 2, 1, 3, 8, 9, -1};
    
    int M = 4;
    int arr1[N];
    int arr2[N-M];

    // Storing in arr1
    for(int i=0; i<M; i++)
    {
        arr1[i] = array[i];
        // cout<<array[i]<<" ";  // Printing out value in array[i]
    }

    // Storing in arr2
    for(int i=M; i<N; i++)
    {
        arr2[i-M] = array[i];
    }

    // Sort arr1 and arr2 in ascending order
    sort(arr1, arr1 + M);
    sort(arr2, arr2 + N-M);

    // Setting in the array
    int len2 = N-M-1;
    for(int i=0; i<N; i++)
    {
        if(i < M)
        {
            array[i] = arr1[i];
            // cout<<array[i]<<" ";
        }
        else
        {
            array[i] = arr2[len2];    
            // cout<<array[i]<<" ";
            len2--;   
        }   
    }
    // cout<<endl;

    // Print the array
    for(int i=0; i<N; i++)
    {
        cout<<array[i]<<" ";
    }
    return 0;
}
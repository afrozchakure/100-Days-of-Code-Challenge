#include<iostream>
#include<bits/stdc++.h>
using namespace std;

// Creating a variable of template class 
template <class T>

void print(T arr[], int num)
{
    for(int i=0; i<num; i++)
        cout<<arr[i]<<" ";
    cout<<endl;
}
int main()
{
    int num = 5;
    int arr[num] = {5, 2, 6, 1, 0};
    string str_arr[num] = {"def", "abc", "World", "Afroz", "Hello"};
    float float_arr[num] = {5.0, 3.0, 1.0, 7.0, 9.0};
    sort(arr, arr+num);
    sort(str_arr, str_arr + num);
    sort(float_arr, float_arr + num);
    print(arr, num);
    print(str_arr, num);
    print(float_arr, num);
    return 0;
}

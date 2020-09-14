#include<iostream>
#include<map>
#include<unordered_map>
#include<vector>
#include<unordered_map>
using namespace std;

int main()
{
    int n;
    cin>>n;
    vector<int> A(n+5,0);  // Increase Array size to prevent segmentatin fault
    long long S = 0;  // To calculate the total sum of array

    // Inserting the elements in vector and calculating sum of elements
    for(int i=0; i<n;i++)  cin>> A[i], S+= A[i];

    // Check if sum is odd
    if(S & 1)  // Means if the number is odd
    {
        cout << "NO";  // The answer won't exist
        return 0;
    }

    unordered_map<long long,int> first, second;  // Creating two maps

    first[A[0]] = 1;  // assign first element of A as 1

    for(int i=1; i<n; i++) second[A[i]]++;  // assigning other elements

    long long sdash = 0;

    for(int i=0; i < n; i++)
    {
        sdash += A[i];  // First i numbers (Calculating sdash) 
        if(sdash == S/2){
            cout << "YES\n";
            return 0;
    }
        if(sdash < S/2)
        {
            long long x = S / 2 - sdash; 
            // delete element from second half, and insert into first half
            if(second[x] > 0)
            {
                cout<< "YES\n";
                return 0;
            }
        }
        else{
            long long y = sdash - S / 2; 
            // delete element from the first half, and insert into second half
            if(first[y] > 0)
            {
                cout<< "YES\n";
                return 0;
            }
        }
        first[A[i+1]]++;  // Incrementing the value of first index
        second[A[i+1]]--;  // Decrementing the value of second index
    }
    cout << "NO\n";
}

#include <iostream>
#include<bits/stdc++.h>  // Add this library to use sort
using namespace std;

bool KeyPair(int sum_pairs, int N, int A[]){
    int l = 0;
    int r = N-1;
    while(l < r){
        if(A[l] + A[r] == sum_pairs)
            return 1;
        else if(A[l] + A[r] < sum_pairs)
            l++;
        else if(A[l] + A[r] > sum_pairs)
            r--;
	    }
	return 0;
}

int main() {
	//code
	int T;
	cin>>T;
	for(int i=0; i<T; i++){
	    int N, sum_pairs;
	    cin>>N>>sum_pairs;
	    int A[N];
	    for(int j=0; j<N; j++)
	    {
	        cin>>A[j];
	    }
	    sort(A, A+N);
	    int a = KeyPair(sum_pairs, N, A);
	    if(a)
	        cout<<"Yes"<<endl;
	    else
	        cout<<"No"<<endl;
	    
	}
	return 0;
}

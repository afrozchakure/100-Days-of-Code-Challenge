#include <iostream>
using namespace std;

int main() {
	//code
	int t;
	cin>>t;
	for(int i=0; i<t; i++){
	    int n;
	    cin>>n;
	    for(int j=13; j > -1; j--)
	    {
	    cout<< ((n>>j) & 1);
	    }
	    cout<<endl;
	}
	return 0;
}

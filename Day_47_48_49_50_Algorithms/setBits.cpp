#include <iostream>
using namespace std;

string setBit(int n){
    // All bits are not set
    if(n == 0){
        return "NO";
    }
    // Loop till n becomes 0
    while(n > 0){
        if((n & 1)== 0){
            return "NO";
        }
        n = n>>1;  // Performing right shift by 1 bit
    }
    // All bits are set
    return "YES";
}
int main() {
	//code
	int t;
	cin>>t;
	for(int i=0; i<t; i++){
	    int n;
	    cin>>n;
	    cout<<setBit(n)<<endl;
	    
	}
	return 0;
}

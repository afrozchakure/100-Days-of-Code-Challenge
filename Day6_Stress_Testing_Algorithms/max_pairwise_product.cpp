#include <cstdlib>  // part of standard library, helps us generate random numbers
#include <iostream>
using namespace std;
#include <vector>

long long MaxPairwiseProduct(const vector<int>& numbers) {
    long long product = 0;
    int n = numbers.size();
    for(int i = 0; i < n; ++i){
        for(int j = i+1; j < n; ++j){
            if ((long long)numbers[i] * numbers[j] > product) {
                product = max(product, (long long)numbers[i] * numbers[j]);
            }
        }
    }
    return product;
}

long long MaxPairwiseProductFast(const vector<int>& numbers){
    int n = numbers.size();
    int max_index1 = -1;
    for(int i = 0; i < n; ++i)
        if((max_index1 == -1) || (numbers[i] > numbers[max_index1]))
            max_index1 = i;
    int max_index2 = -1;
    for(int j = 0; j < n; ++j)
        if((j != max_index1) && ((max_index2 == -1) || (numbers[j] > numbers[max_index2])))
            max_index2 = j;

    // cout<<max_index1 << " "<< max_index2 <<"\n";
    return ((long long) ((long long)numbers[max_index1] * (long long)numbers[max_index2]));
}

int main(){
    // Stress Testing
/*    while(true) {
        int n = rand() % 1000 + 2;  // Generating nos. of nos. (minimum 2) (Gives random nos b/w 2 and 101)
        cout << n << "\n";
        vector<int> a;
        for (int i = 0; i < n; ++i){
            a.push_back(rand() % 100000);  // rand() generates a number b/w 0 to 99999
        }
        for(int i = 0; i < n; ++i){
            cout<< a[i] << " ";
        }
        cout << "\n";
        long long res1 = MaxPairwiseProduct(a);
        long long res2 = MaxPairwiseProductFast(a);
        if(res1 != res2){
            cout<<"Wrong Answer: " << res1 <<" "<< res2 << "\n";
            break;
        }
        else{
            cout<<"OK\n";
        }

    }
*/
    // Taking the input from user
    int n;
    cin >> n;
    vector<int> numbers(n);
    for(int i = 0; i < n; ++i) {
        cin >> numbers[i];
    }

    long long result = MaxPairwiseProductFast(numbers);
    cout << result << "\n";
    return 0;
}
#include<iostream>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
using namespace std;

bool Descending(int a, int b)  // function to sort in decreasing order
{
    return a > b;
}

void vectorDemo()
{
    vector<int> A = {11, 2, 3, 14};

    cout<< A[1]<<endl;

    // You can perform the below operations only when array is sorted which takes O(NlogN) time
    sort(A.begin(), A.end());  // O(nlogn)

    // 2, 3, 11, 14
    
    // binary Search - O(logN)
    bool present = binary_search(A.begin(), A.end(), 3); 
    present = binary_search(A.begin(), A.end(), 4); // false

    A.push_back(100);
    present = binary_search(A.begin(), A.end(), 100);  // true

    // 2, 3, 11, 14, 100
    A.push_back(100);
    A.push_back(100);
    A.push_back(100);
    A.push_back(100);
    A.push_back(123);
    // 2,3, 11, 14, 100, 100, 100, 100, 100, 123

    // We can perform lower_bound and upper_bound so that we can get the element
    // Strictly greater or Strictly greater and equal in an array
    vector<int>:: iterator it = lower_bound(A.begin(), A.end(), 100); // >= returns 1st number greater than equal to
    vector<int>:: iterator it2 = upper_bound(A.begin(), A.end(), 100); // > first number strictly greater than 100

    // Another way to use iterators 
    // auto tells c++ that it is an iterator of x
    // upper_bound and lower_bound works in O(logn) time if array is sorted
    auto it_1 = lower_bound(A.begin(), A.end(), 100);
    auto it_2 = upper_bound(A.begin(), A.end(), 100);
    // it = 100 , it2 = 123

    cout<< *it << " " << *it2 << endl;
    cout<< it2 - it << endl;  // 4 (difference in position) - iterators and vectors are random, perform in constant time O(1) time
    
    sort(A.begin(), A.end(), Descending);  // f is comparator function

    vector<int>:: iterator it3;

    // Printing the Vector A elements
    for(it3 = A.begin(); it3 != A.end(); it3++)
    {
        cout<< *it3 << " ";
    }
    cout<<endl;

    // Printing the vector A elements
    for(int x: A)
    {
        cout << x << " ";
    }
    cout<<endl;
    // When you want to update the value of element in vector 
    for(int &x: A)  // reference
    {
        x++;
        cout << x << " ";
    }
    cout << endl;
}

// Function for Set
void setDemo()
{
    set<int> S;

    // Set inserts the element in ascending order
    S.insert(1);
    S.insert(2);
    S.insert(-1);
    S.insert(-10);

    // Each operation in set is O(logN) time
    for(int x: S)
        cout << x << " ";
    cout<<endl;

    // -10 -1 1 2 

    // Checking if -1 is present in Set of not
    auto it = S.find(-1);  // If present it points to -1 here 

    // not present it return S.end()
    if(it == S.end())
    {
        cout << "not present\n";
    }
    else {
        cout << "present\n";
        cout << *it <<endl;  // prints the value of it
    }

    // Find 1st element of set greater than 0
    // In Set the class itself has the lower_bound function 
    // unlike *Vector* where the lower_bound() function is different
    
    auto it2 = S.lower_bound(-1);  // iterator to 1st element >= to -1
    auto it3 = S.upper_bound(0); // If I'm interested in strictly greater to 0
    cout << *it2 << " " << *it3 << endl;

    // Case where upperbound doesn't exist in our Set 
    auto it5 = S.upper_bound(3); // It'll return S.end()
    if(it5 == S.end())  // S.end() == 4
    {
        cout << "oops! sorry can't find something like that\n";
    }

    // it2 = -1, it3 = 1

    // Inserting number and Erasing number in set takes O(logN) time
    S.erase(1);  // Done in O(logN) time

/*-------------------------------------------------*/
    // Set vs Vector 
    /* 
    Set doesn't disturb the ordering of the elements
    In Vector all elements are inserted at the end and disturb ordering
    */
/*-------------------------------------------------*/


}

void mapDemo()
{
    map<int, int> A;
    A[1] = 100;
    A[2] = -1;
    A[3] = 200;
    A[100000232] = 1;

    map<char, int> cnt;
    string x= "afroz chakure";

    // How many times a character appears in my name
    for(char c: x){
        cnt[c]++;
    }

    cout<< cnt['a'] << " " << cnt['z'] << endl;

    /*-----------------------------------*/
    // O(logn) -- Takes O(n) time for building the map
    // You can find and delete a key in map or not in just log(N) time 
    // A.find(key) and A.erase(key)
    /*-----------------------------------*/
}

void PowerofStl()
{
    // [x, y]
    /*
    add [2, 3]
    add [10, 20]
    add [30, 400]
    add [401, 450]
    give me the interval that contains 401 */

    set<pair<int, int>> S;

    // what is a pair ? 
    // {x, y} --> {1, 3}, {-1, -12} is a pair
    // pairs of set<pair<int, char>> S;
    // {x, y} --> {1, 'c'}, {2, 'd'}
    
    S.insert({401, 450});
    S.insert({10, 20});
    S.insert({2, 3});
    S.insert({30, 400});

    // Order of elements in set
    // {2, 3}, 
    // {10, 20}, 
    // {30, 400}, 
    // {401, 450}

    // Pair {a, b} is smaller than pair {c, d}
    // iff (a < b) or (a == b and c < d)

    /* {a, b} is smaller than {c, d} iff 
    (a < c) or (a == c and b < d) */

    // find {31, ?}
    // Do upper_bound for {31, ?} --> will give set {401, 450}
    // Do upper_bound for {12, ?} --> {30, 400}
    // Case: Do upper_bound for {10, 0} --> {10, 20} (Since x-corr same and we'll compare y-corrdinates)
    // So for our algorithm to find correct upper_bound 
    // The 2nd element in pair should be bigger than all 2nd elements in all pairs 
    // Solution : use {10, INT_MAX}

    int point = 401;

    auto it = S.upper_bound({point, INT16_MAX});  // for point = 401, it should return S.end() 
    if( it == S.begin())
    {   
        cout << "the given point is not lying in any interval..\n";
        return;
    }
    it--; 
    pair<int, int> current = *it;

    // Values in pair X = {a, b} acessed using X.first and X.second
    // Means point lies within current.first and current.second
    if(current.first <= point && point <= current.second)
    {
        cout << "yes its present" << current.first << " " << current.second<<endl;
    }
    else 
    {
        cout << "the given point is not lying in any interval\n";
    }

}
int main()
{
    // C++ STL

    // Vector
    vectorDemo();

    // Set 
    setDemo();

    // Map
    mapDemo();

    // Solving using Sets
    PowerofStl();
    return 0;
}
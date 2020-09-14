#include<iostream>
#include<map>
#include<unordered_map>
using namespace std;
int main()
{
    map<char, int> Map;  // Ordered_map
    unordered_map<char, int> Uset;  // Unordered_map

    string s = "Afroz Chakure";

    // ordered_map v/s unordered_map
    // add(key, value) --> logN, O(1)
    // erase(key) --> logN, O(1)

    // How many times a character occurs in String s
    for(char c: s) Map[c]++; // O(NlogN) where N = |s|, N is equal to size of string s
    for(char c: s) Uset[c]++;  // O(N) 
    // Unordered Maps can set and get the value in O(1) time 
    // that is, O(N) for N values

    return 0;
}
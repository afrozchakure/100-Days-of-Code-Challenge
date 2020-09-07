class Solution {
public:
    bool isPalindrome(string s) {
        for(int i=0, j=s.size() - 1; i<j; i++, j--)  // Move two pointers from each end until they collide
        {
            while(isalnum(s[i]) == false && i<j) i++;  // If s[i] is not alphanumeric do i++
            while(isalnum(s[j]) == false && i<j) j--;  // If s[j] is not alphanumeric do j--
            if(toupper(s[i]) != toupper(s[j])) return false;
        }
        return true;
    }
};

// Time Complexity - O(n)
// Space Complexity - O(1)

class Solution {
public:
    vector<int> decompressRLElist(vector<int>& nums) {
        vector<int> s;
        for(int i=0; i<nums.size(); i+=2)
        {
            for(int j=0; j<nums[i]; j++)
            {
                s.push_back(nums[i+1]);
            }
        }
        return s;
    }
};

// Time Complexity - O(n**2)
// Space Complexity - O(n)

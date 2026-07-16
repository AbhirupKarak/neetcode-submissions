class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int,int> m;
        for(int i : nums){
            m[i]++;
        }
        for(auto i : m){
            if(i.second > 1){
                return true;
            }
        }
        return false;
    }
};
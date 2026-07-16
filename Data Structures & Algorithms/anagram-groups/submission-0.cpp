class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;
        vector<vector<string>> res;
        for(string s : strs){
            string x = s;
            sort(x.begin(), x.end());
            map[x].push_back(s);
        }

        for(auto i : map){
            res.push_back(i.second);
        }
        return res;
    }
};
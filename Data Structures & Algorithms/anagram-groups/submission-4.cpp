class Solution {
private: 
    string build_key(const string &str) {
        vector<int> count(26, 0); 
        for (const auto& c : str) {
            char index = c - 'a';
            count[index]++;
        } 

        string key = to_string(count[0]);
        for (int i = 1; i < count.size(); i++) {
            key += "," + to_string(count[i]);
        }
        return key;
    }   
    
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;
        // key: counts of the characters of a single string in the bucket
        // val: the vector of strings that hash into that bucket

        for (string str : strs) {
            string key = build_key(str);

            if (map.contains(key)) {
                map[key].push_back(str);
            } else {
                map[key] = {str};
            }
        } 

        vector<vector<string>> result = {};
        transform(map.begin(), map.end(), back_inserter(result), [](const auto &pair) { return pair.second; }); 
        return result;
    }
};

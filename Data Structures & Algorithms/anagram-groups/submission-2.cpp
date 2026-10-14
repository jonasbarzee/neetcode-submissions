class Solution {
private: 
    vector<int> build_key(const string &str) {
        vector<int> count(26, 0);

        for (const auto& c : str) {
            char index = c - 'a';
            count[index]++;
        }

        // cout << "[";
        // for (const auto& elem : count) {
        //     cout << elem << ", ";
        // }
        // cout << "]" << endl;;

        return count;
    }  

    void print_map(const unordered_map<int, vector<string>> &map) {
        auto iter = map.begin();
        cout << "{" << endl;
        while (iter != NULL) {
            cout << iter->first <<  " : ";

            auto vec_iter = iter->second.begin();
            while (vec_iter != iter->second.end()) { 
                cout << *vec_iter << " ";
                vec_iter++;
            }
            cout << endl;
            
            iter++;
        }
        cout << "}"; 
        return;
    }

public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<vector<int>, vector<string>> map;
        // key: counts of the characters of a single string in the bucket
        // val: the vector of strings that hash into that bucket

        for (string str : strs) {
            vector<int> key = build_key(str);

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

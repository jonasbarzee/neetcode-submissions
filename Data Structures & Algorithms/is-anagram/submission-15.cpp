class Solution {
private:

    void print_map(std::unordered_map<char, int> *map) {
        std::unordered_map<char, int>::iterator iter = map->begin();
        int i = 0;
        while (i < map->size()) {
            std::cout << "{" << iter->first << " : " << iter->second << "}";
            iter++;
            i++;
        } 
        std::cout << std::endl;
        return;
    }

public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> map;

        if (s.size() != t.size()) {
            return false;
        }

        for (char c : s) {
            std::unordered_map<char, int>::iterator prev = map.find(c);
            if (prev != map.end()) {
                char key = prev->first;
                int val = prev->second;
                // std::cout << "inserting " << c << " : " << val << "+1" << std::endl;
                map[key] = val + 1;
            } else { 
                // std::cout << "inserting " << c << " : 1" << std::endl;
                map.insert({c, 1});
            }  
            // print_map(&map);
        }

        
        for (char c : t) {
            std::unordered_map<char, int>::iterator prev = map.find(c);
            if (prev != map.end() && prev->second != 0) {
                char key = prev->first;
                int val = prev->second;
                map[key] = val - 1;
            } else {
                return false; 
            } 
            // print_map(&map);
        }
        return true; 
    }
};

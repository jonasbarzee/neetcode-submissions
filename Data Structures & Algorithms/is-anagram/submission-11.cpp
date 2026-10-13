class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        for (char c : s) {
            int ptr = 0;
            while (ptr < t.size()) {
                if (c == t[ptr]) {
                    t.erase(ptr, 1);
                    break;
                }
                ptr++;
            }
        }
        if (!t.size()) {
            return true;
        }
        return false;
        
    }
};

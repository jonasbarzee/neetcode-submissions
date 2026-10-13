class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_multimap<int, int> num_to_idx;

        for (int i = 0; i < nums.size(); i++) {
            auto prev = num_to_idx.find(target - nums[i]);
            if (prev != num_to_idx.end()) {
                return {prev->second, i}; 
            } else {
                num_to_idx.insert({nums[i], i});
            }
        } 
        return {};
    }
};

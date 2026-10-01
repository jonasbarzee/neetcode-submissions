class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int saved_size = nums.size();
        for (int i = 0; i < saved_size; i++) {
            nums.push_back(nums[i]);
        }
        return nums;
    }
};
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int result = 0;
        int count = 0;

        for (int num : nums) {
            if (count == 0) {
                result = num;
                count++;
                continue;
            } 
            result == num ? count++ : count--;
        }    
        return result;
    }
};
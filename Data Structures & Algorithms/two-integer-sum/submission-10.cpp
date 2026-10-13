class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_multimap<int, int> diff_to_idx;
        std::vector<int> result;

        for (int i = 0; i < nums.size(); i++) {
            int difference = target - nums[i];
            diff_to_idx.insert({difference, i});
        }

         auto iter = diff_to_idx.begin();
         while (iter != nullptr) {
             std::cout << iter->first << " " << iter->second << " | ";
             iter++;
         }
         std::cout << std::endl;

        for (int i = 0; i < nums.size(); i++) {
            auto exists = diff_to_idx.find(nums[i]);
            if (exists == diff_to_idx.end()) { continue; }

            // std::cout << exists->second << std::endl;
            // std::cout << i << std::endl;
            int smaller = std::min(exists->second, i);
            int bigger = std::max(exists->second, i);

            if (smaller == bigger) { continue; }
            
            result.push_back(smaller);
            result.push_back(bigger); 
            return result;
        }
        
    }
};

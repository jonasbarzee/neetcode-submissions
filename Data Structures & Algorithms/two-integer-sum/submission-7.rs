impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut num_to_idx = HashMap::with_capacity(nums.len());

        for (i, &num) in nums.iter().enumerate() {
            let diff = target - num;

            if let Some(&match_idx) = num_to_idx.get(&diff) {
                return vec![match_idx, i as i32]
            }
            num_to_idx.insert(num, i as i32);
        }
        vec![] 
    }
}

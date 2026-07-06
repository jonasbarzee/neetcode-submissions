impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut val_to_idx: HashMap<&i32, i32> = HashMap::new();

        for (index, value) in nums.iter().enumerate() {
            val_to_idx.insert(value, index as i32);
        }

        for (index, value) in nums.iter().enumerate() {
            let difference = target - value;

            if val_to_idx.contains_key(&difference) && index as i32 != val_to_idx[&difference] {
                let diff_idx = val_to_idx[&difference];
                return vec![min(index as i32, diff_idx), max(index as i32, diff_idx)]
            }
        } 
        vec![]
    }
}

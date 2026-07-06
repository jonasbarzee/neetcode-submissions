impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut diff_to_index: HashMap<i32, i32> = HashMap::new();
        for (index, number) in nums.iter().enumerate() {
            let diff = target - number;
            if diff_to_index.contains_key(&number) {
                let diff_index = diff_to_index[&number];
                return vec![min(index as i32, diff_index), max(index as i32, diff_index)]
            } else {
                diff_to_index.insert(diff, index as i32);
            }
            let diff_index = diff_to_index.get(&diff).unwrap();
            // println!("index: {} number: {} diff: {} diff_index: {:?} diff_to_index: {:?}", index, number, diff, diff_index, diff_to_index)
        }
        vec![]

    }
}

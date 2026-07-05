impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        let mut set: HashSet<i32> = HashSet::new();

        for number in nums {
            if !set.insert(number) {
                return true;
            }
        }  
        false

    }
}

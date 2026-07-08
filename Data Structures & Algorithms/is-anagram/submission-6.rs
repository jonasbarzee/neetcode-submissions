impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut left: HashMap<char, u32> = HashMap::new();
        let mut right: HashMap<char, u32> = HashMap::new();

        for c in s.chars() {
            if left.contains_key(&c) {
                left.insert(c, left[&c] + 1);
            } else {
                left.insert(c, 1);
            }
        }

        for c in t.chars() {
            if right.contains_key(&c) { 
                right.insert(c, right[&c] + 1); 
            } else { 
                right.insert(c, 1);  
            }
        }

        left == right

    }
}

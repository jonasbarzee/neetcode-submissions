impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut left: HashMap<char, u32> = HashMap::new();
        let mut right: HashMap<char, u32> = HashMap::new(); 

        for c in s.chars() {
            *left.entry(c).or_insert(0) += 1;
        }

        for c in t.chars() { 
            *right.entry(c).or_insert(0) += 1;
        }

        left == right

    
    }
}

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {  
        if s.len() != t.len() {
            return false 
        }

        let mut left: Vec<char> = s.chars().collect();
        let mut right: Vec<char> = t.chars().collect();

        left.sort();
        right.sort();

        left == right
    }
}

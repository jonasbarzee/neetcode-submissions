impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {  
        let mut left: Vec<char> = vec![];
        for character in s.chars() {
            left.push(character);

        }
        let mut right: Vec<char> = vec![];
        for character in t.chars() {
            right.push(character);

        }

        left.sort();
        right.sort();


        println!("left {:?} right {:?}", left, right);

        left == right
    }
}

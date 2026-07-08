impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let left: HashMap<char, u32> = s.chars().fold(HashMap::new(), |mut map, c| {
            *map.entry(c).or_insert(0) += 1;
            map
        });
        let right: HashMap<char, u32> = t.chars().fold(HashMap::new(), |mut map, c| {
            *map.entry(c).or_insert(0) += 1;
            map
        });

        left == right


    }
}

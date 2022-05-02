struct Solution;

impl Solution {
    pub fn letter_combinations(digits: String) -> Vec<String> {
        let map = std::collections::HashMap::from([
            ('2', vec!['a', 'b', 'c']),
            ('3', vec!['d', 'e', 'f']),
            ('4', vec!['g', 'h', 'i']),
            ('5', vec!['j', 'k', 'l']),
            ('6', vec!['m', 'n', 'o']),
            ('7', vec!['p', 'q', 'r', 's']),
            ('8', vec!['t', 'u', 'v']),
            ('9', vec!['w', 'x', 'y', 'z']),
        ]);

        let product2 = |i1, i2| {
            let mut result = vec![];
            for c1 in map.get(i1).unwrap() {
                for c2 in map.get(i2).unwrap() {
                    result.push(c1.to_string() + &c2.to_string());
                }
            }
            result
        };

        let product3 = |i1, i2, i3| {
            let mut result = vec![];
            for c1 in map.get(i1).unwrap() {
                for c2 in map.get(i2).unwrap() {
                    for c3 in map.get(i3).unwrap() {
                        result.push(c1.to_string() + &c2.to_string() + &c3.to_string());
                    }
                }
            }
            result
        };

        let product4 = |i1, i2, i3, i4| {
            let mut result = vec![];
            for c1 in map.get(i1).unwrap() {
                for c2 in map.get(i2).unwrap() {
                    for c3 in map.get(i3).unwrap() {
                        for c4 in map.get(i4).unwrap() {
                            result.push(
                                c1.to_string()
                                    + &c2.to_string()
                                    + &c3.to_string()
                                    + &c4.to_string(),
                            );
                        }
                    }
                }
            }
            result
        };

        let mut iter = digits.chars();
        match digits.len() {
            1 => {
                let mut result = vec![];
                map.get(&iter.next().unwrap())
                    .unwrap()
                    .iter()
                    .for_each(|c| {
                        result.push(c.to_string());
                    });
                result
            }
            2 => product2(&iter.next().unwrap(), &iter.next().unwrap()),
            3 => product3(
                &iter.next().unwrap(),
                &iter.next().unwrap(),
                &iter.next().unwrap(),
            ),
            4 => product4(
                &iter.next().unwrap(),
                &iter.next().unwrap(),
                &iter.next().unwrap(),
                &iter.next().unwrap(),
            ),
            _ => vec![],
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(
            Solution::letter_combinations("23".to_string()),
            vec!["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        );
    }

    #[test]
    fn test_2() {
        assert_eq!(
            Solution::letter_combinations("2".to_string()),
            vec!["a", "b", "c"]
        );
    }

    #[test]
    fn test_3() {
        assert_eq!(
            Solution::letter_combinations("".to_string()),
            Vec::<String>::new()
        );
    }
}

use std::collections::VecDeque;

fn part1(input: &str) {
    fn check_vowels(word: &str) -> bool {
        let mut count = 0;
        for c in word.chars() {
            if c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' {
                count += 1;
            }
        }
        count >= 3
    }

    fn check_twice(word: &str) -> bool {
        let mut last_char = '@';
        for c in word.chars() {
            if c == last_char {
                return true;
            }
            last_char = c;
        }
        false
    }

    fn check_exclude(word: &str) -> bool {
        let bad_strings = ["ab", "cd", "pq", "xy"];
        for bad in bad_strings {
            if word.contains(bad) {
                return false;
            }
        }
        true
    }

    fn check_all_rules(word: &str) -> bool {
        check_vowels(word) && check_twice(word) && check_exclude(word)
    }

    println!(
        "Part 1: {}",
        input.lines().filter(|l| check_all_rules(l)).count()
    );
}

fn part2(input: &str) {
    fn check_xyx(word: &str) -> bool {
        let mut chars = VecDeque::from(['@', '!', '%']);
        for c in word.chars() {
            chars.push_front(c);
            chars.pop_back();

            if chars[0] == chars[2] {
                return true;
            }
        }
        false
    }

    fn twice_without_overlapping(word: &str) -> bool {
        let char_vec: Vec<char> = word.chars().collect();
        let iter = char_vec.windows(2);
        let pairs: Vec<(usize, &[char])> = iter.enumerate().collect();
        for (i, pair1) in &pairs {
            for (j, pair2) in pairs[i + 1..].iter() {
                if (pair1 == pair2) && (j - i > 1) {
                    return true;
                }
            }
        }

        false
    }

    fn check_all_rules(word: &str) -> bool {
        check_xyx(word) && twice_without_overlapping(word)
    }

    println!(
        "Part 2: {}",
        input.lines().filter(|l| check_all_rules(l)).count()
    );
}
fn main() {
    let input = include_str!("../input.txt");
    part1(input);
    part2(input);
}

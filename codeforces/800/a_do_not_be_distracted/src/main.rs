use std::{collections::HashSet, io::stdin};

fn solver(s: &str) {
    let mut used = HashSet::new();
    let mut result = "YES";
    for i in 0..s.len() - 1 {
        let curr_char = s.chars().nth(i).unwrap();
        let next_char = s.chars().nth(i + 1).unwrap();

        if curr_char != next_char {
            // println!("add char {}", curr_char);
            if used.contains(&curr_char) {
                result = "NO";
                break;
            } else {
                used.insert(curr_char);
            }
        } else {
            if used.contains(&curr_char) {
                result = "NO";
                break;
            } else {
                continue;
            }
        }
    }

    // check last char
    if used.contains(&s.chars().nth(s.len() - 1).unwrap()) {
        result = "NO";
    }

    println!("{}", result);
}
fn main() {
    let mut t = String::new();

    let reader = stdin();

    reader.read_line(&mut t).expect("er1"); // t
    let t: usize = t.trim().parse().expect("er2");
    for _ in 0..t {
        let mut n = String::new();
        reader.read_line(&mut n).expect("er3"); // n

        let mut line = String::new();
        reader.read_line(&mut line).expect("er5"); // string

        let s = line.trim();
        // println!("s = {}", s);
        solver(s);
    }
}

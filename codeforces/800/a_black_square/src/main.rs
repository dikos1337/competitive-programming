use std::io::{self, BufRead};

fn main() {
    let reader = io::stdin();
    let numbers: Vec<i32> = reader
        .lock()
        .lines()
        .next()
        .unwrap()
        .unwrap()
        .split(' ')
        .map(|s| s.trim())
        .filter(|s| !s.is_empty())
        .map(|s| s.parse().unwrap())
        .collect();

    let s = reader.lock().lines().next().unwrap().unwrap();

    let mut sum = 0;
    for c in s.chars() {
        sum += numbers.get((c.to_digit(10).unwrap() - 1) as usize).unwrap();
    }

    println!("{}", sum);
}

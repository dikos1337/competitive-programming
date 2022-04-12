use std::{
    cmp::Ordering,
    io::{stdin, BufRead},
};

fn main() {
    let reader = stdin();
    let n: usize = reader
        .lock()
        .lines()
        .next()
        .unwrap()
        .unwrap()
        .parse()
        .unwrap();

    let mut mishka_score: usize = 0;
    let mut chris_score: usize = 0;

    for _ in 0..n {
        let arr: Vec<usize> = reader
            .lock()
            .lines()
            .next()
            .unwrap()
            .unwrap()
            .split(" ")
            .map(|x| x.trim().parse().unwrap())
            .collect();

        let (m, c) = (arr[0], arr[1]);

        match m.cmp(&c) {
            Ordering::Equal => continue,
            Ordering::Greater => mishka_score += 1,
            Ordering::Less => chris_score += 1,
        }
    }

    match mishka_score.cmp(&chris_score) {
        Ordering::Equal => println!("Friendship is magic!^^"),
        Ordering::Greater => println!("Mishka"),
        Ordering::Less => println!("Chris"),
    }
}

use regex::Regex;

fn part1(input: &str) {
    let re = Regex::new(r"-?\d+").unwrap();

    let part1: i64 = re
        .captures_iter(input)
        .map(|cap| cap[0].parse::<i64>().unwrap())
        .into_iter()
        .sum();

    println!("Part 1: {}", part1);
}
fn main() {
    let input = include_str!("../input.txt");
    part1(input);
}

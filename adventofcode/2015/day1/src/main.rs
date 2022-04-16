fn part1(input: &str) {
    let floor = input.chars().fold(0, |acc, c| match c {
        '(' => acc + 1,
        ')' => acc - 1,
        _ => panic!(),
    });
    println!("Part 1: {}", floor);
}

fn part2(input: &str) {
    let mut floor: i64 = 0;
    for (i, ch) in input.chars().enumerate() {
        match ch {
            '(' => floor += 1,
            ')' => floor -= 1,
            _ => panic!(),
        }
        if floor == -1 {
            println!("Part 2: {}", i + 1);
            break;
        }
    }
}
fn main() {
    let input = include_str!("../input.txt");
    part1(input);
    part2(input);
}

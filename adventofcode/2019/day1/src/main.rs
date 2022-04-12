fn part1() {
    let input = include_str!("../input.txt");
    let nums = input
        .lines()
        .map(|l| l.parse::<i32>().unwrap())
        .collect::<Vec<_>>();

    let answer = nums.into_iter().map(|n| n / 3 - 2).sum::<i32>();
    println!("answer: {}", answer);
}

fn part2() {
    let input = include_str!("../input.txt");
    let nums = input
        .lines()
        .map(|l| l.parse::<i32>().unwrap())
        .collect::<Vec<_>>();

    let answer = nums
        .into_iter()
        .map(|n| {
            let mut sum = 0;
            let mut fuel = n / 3 - 2;
            while fuel > 0 {
                sum += fuel;
                fuel = fuel / 3 - 2;
            }
            sum
        })
        .sum::<i32>();
    println!("answer: {}", answer);
}

fn main() {
    // part1();
    part2();
}

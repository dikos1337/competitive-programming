fn part1(input: &str) {
    let mut counter = 0;
    for line in input.lines() {
        let mut nums = line
            .split_ascii_whitespace()
            .filter(|x| !x.is_empty())
            .map(|s| s.parse().unwrap())
            .collect::<Vec<i32>>();

        nums.sort_unstable();
        if nums[0] + nums[1] > nums[2] {
            counter += 1;
        }
    }
    println!("Part 1: {}", counter);
}

fn part2(input: &str) {
    let mut counter = 0;
    let mut group3 = Vec::new();
    for line in input.lines() {
        let nums = line
            .split_ascii_whitespace()
            .filter(|x| !x.is_empty())
            .map(|s| s.parse().unwrap())
            .collect::<Vec<i32>>();
        group3.push(nums);
        if group3.len() % 3 == 0 {
            for i in 0..3 {
                group3.sort_by(|a, b| a[i].cmp(&b[i]));
                if group3[0][i] + group3[1][i] > group3[2][i] {
                    counter += 1;
                }
            }
            group3.clear();
        }
    }
    println!("Part 2: {}", counter);
}

fn main() {
    let input = include_str!("../input.txt");
    part1(input);
    part2(input);
}

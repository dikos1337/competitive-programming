fn part1() {
    let input = include_str!("../input.txt");
    let mut nums = input
        .trim()
        .split(',')
        .map(|s| s.parse::<usize>().unwrap())
        .collect::<Vec<_>>();

    nums[1] = 12;
    nums[2] = 2;

    let mut i = 0;
    while nums[i] != 99 {
        let op = nums[i];
        match op {
            1 => {
                let a = nums[i + 1];
                let b = nums[i + 2];
                let c = nums[a] + nums[b];
                let idx = nums[i + 3];
                nums[idx] = c;
            }
            2 => {
                let a = nums[i + 1];
                let b = nums[i + 2];
                let c = nums[a] * nums[b];
                let idx = nums[i + 3];
                nums[idx] = c;
            }
            _ => panic!("Unknown opcode {}", op),
        }

        i += 4;
    }
    let answer = nums[0];
    println!("answer: {}", answer);
}

fn part2() {
    let input = include_str!("../input.txt");

    for noun in 0..100 {
        for verb in 0..100 {
            let mut nums = input
                .trim()
                .split(',')
                .map(|s| s.parse::<usize>().unwrap())
                .collect::<Vec<_>>();

            nums[1] = noun;
            nums[2] = verb;

            let mut i = 0;
            while nums[i] != 99 {
                let op = nums[i];
                match op {
                    1 => {
                        let a = nums[i + 1];
                        let b = nums[i + 2];
                        let c = nums[a] + nums[b];
                        let idx = nums[i + 3];
                        nums[idx] = c;
                    }
                    2 => {
                        let a = nums[i + 1];
                        let b = nums[i + 2];
                        let c = nums[a] * nums[b];
                        let idx = nums[i + 3];
                        nums[idx] = c;
                    }
                    _ => panic!("Unknown opcode {}", op),
                }

                i += 4;
            }
            if nums[0] == 19690720 {
                println!("answer: {}", 100 * noun + verb);
                return;
            }
        }
    }
}
fn main() {
    // part1();
    part2();
}

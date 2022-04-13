use itertools::Itertools;

mod intcode;
use intcode::IntCode;
fn main() {
    let input = include_str!("../input.txt");
    let memory = input
        .trim()
        .split(',')
        .map(|s| s.parse::<i64>().unwrap())
        .collect::<Vec<_>>();

    let mut max_output = 0;
    let perms = (0..=4).permutations(5);

    for perm in perms {
        let mut prev_output = 0;
        for i in perm {
            print!("i: {} \t", i);

            let mut computer = IntCode::from(memory.clone());
            computer.set_user_input(i);
            computer.set_user_input(prev_output);
            computer.run();
            match computer.output.pop() {
                Some(output) => {
                    prev_output = output as usize;
                    if output > max_output {
                        max_output = output;
                    }
                }
                None => {
                    println!("No output");
                }
            }
        }
    }
    println!("Part 1: {}", max_output);
}

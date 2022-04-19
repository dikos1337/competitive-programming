use itertools::Itertools;
use std::collections::{HashMap, HashSet};

fn main() {
    let mut distances = HashMap::new();

    let input = include_str!("../input.txt")
        .trim()
        .split('\n')
        .map(|line| {
            let split = line.split_ascii_whitespace().collect::<Vec<_>>();
            let (from, to, distance) = (split[0], split[2], split[4]);
            distances.insert(
                (from.to_string(), to.to_string()),
                distance.parse::<i32>().unwrap(),
            );
            distances.insert(
                (to.to_string(), from.to_string()),
                distance.parse::<i32>().unwrap(),
            );
            (from, to, distance.parse::<i32>().unwrap())
        })
        .collect::<Vec<_>>();

    let mut unique_cities = HashSet::new();

    for x in &input {
        unique_cities.insert(x.0);
        unique_cities.insert(x.1);
    }

    let num_cities = unique_cities.len();
    let mut min_distance = std::i32::MAX;
    let mut max_distance = std::i32::MIN;
    for city in unique_cities.into_iter().permutations(num_cities) {
        let mut curr_distance = Vec::new();
        for win2 in city.windows(2) {
            curr_distance.push(
                distances
                    .get(&(win2[0].to_string(), win2[1].to_string()))
                    .unwrap(),
            );
        }

        let sum = curr_distance.into_iter().sum::<i32>();
        if sum < min_distance {
            min_distance = sum;
        }
        if sum > max_distance {
            max_distance = sum;
        }
    }
    println!("Part 1: {}", min_distance);
    println!("Part 2: {}", max_distance);
}

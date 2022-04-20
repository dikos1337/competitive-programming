use itertools::Itertools;
use std::collections::{HashMap, HashSet};

fn part1(input: &str) {
    let mut persons: HashMap<&str, Person> = HashMap::new();
    let mut diffs = HashMap::new();
    parse_persons(input, &mut persons);
    let persons_clone = persons.clone();
    fill_diffs(&mut persons, persons_clone, &mut diffs);
    let max_diff_sum = calc_happiness(persons, diffs);
    println!("Part 1: {}", max_diff_sum);
}

fn part2(input: &str) {
    let mut persons: HashMap<&str, Person> = HashMap::new();
    let mut diffs = HashMap::new();
    parse_persons(input, &mut persons);
    let unique_names: HashSet<&str> = persons.keys().cloned().collect();

    for other in unique_names.iter() {
        persons.get_mut(other).unwrap().relations.insert("Me", 0);
    }
    let me = persons.entry("Me").or_insert(Person {
        relations: HashMap::new(),
    });
    for other in unique_names.iter() {
        me.relations.insert(*other, 0);
    }

    let persons_clone = persons.clone();
    fill_diffs(&mut persons, persons_clone, &mut diffs);
    let max_diff_sum = calc_happiness(persons, diffs);
    println!("Part 2: {}", max_diff_sum);
}
fn main() {
    let input = include_str!("../input.txt");
    part1(input);
    part2(input);
}

#[derive(Debug, Clone)]
struct Person<'a> {
    relations: HashMap<&'a str, i32>,
}

fn calc_happiness(persons: HashMap<&str, Person>, diffs: HashMap<(&str, &str), i32>) -> i32 {
    let unique_names: HashSet<&str> = persons.keys().cloned().collect();
    let names_len = unique_names.len();
    let perms = unique_names.iter().permutations(names_len);
    let mut max_diff_sum = i32::MIN;
    for p in perms {
        let mut diff_sum = Vec::new();
        let fisrt_name;
        let last_name;
        {
            let mut iter = p.iter();
            fisrt_name = *iter.next().unwrap();
            last_name = *iter.last().unwrap();
        }
        for w2 in p.windows(2) {
            let tuple = (*w2[0], *w2[1]);
            let diff = diffs.get(&tuple).unwrap();
            diff_sum.push(*diff);
        }
        diff_sum.push(*diffs.get(&(fisrt_name, last_name)).unwrap());

        let diff_sum_sum = diff_sum.iter().sum::<i32>();
        if diff_sum_sum > max_diff_sum {
            max_diff_sum = diff_sum_sum;
        }
        // println!("------")
    }
    max_diff_sum
}

fn fill_diffs<'a>(
    persons: &mut HashMap<&'a str, Person<'a>>,
    persons_clone: HashMap<&str, Person>,
    diffs: &mut HashMap<(&'a str, &'a str), i32>,
) {
    for (self_name, me) in persons.iter_mut() {
        for (other_name, happiness) in me.relations.iter() {
            let other_person_relation_with_me = *persons_clone
                .get(other_name)
                .unwrap()
                .relations
                .get(self_name)
                .unwrap();

            let diff = *happiness + other_person_relation_with_me;
            let tuple = (*other_name, *self_name);
            diffs.insert(tuple, diff);
        }
    }
}

fn parse_persons<'a>(input: &'a str, persons: &mut HashMap<&'a str, Person<'a>>) {
    let lines = input.lines();
    // fill persons
    for line in lines {
        let words = line.split_whitespace().collect::<Vec<_>>();
        let name = words[0];
        let sing = words[2];
        let happiness = words[3];
        let other_person = words[10].trim_matches('.');

        let person = persons.entry(name).or_insert(Person {
            relations: HashMap::new(),
        });

        person.relations.insert(
            other_person,
            match sing {
                "lose" => -happiness.parse::<i32>().unwrap(),
                "gain" => happiness.parse::<i32>().unwrap(),
                _ => panic!("Unknown sign"),
            },
        );
    }
}

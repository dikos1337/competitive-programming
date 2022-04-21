#[derive(Debug, Clone, Copy)]
struct Sue {
    id: u32,
    children: u32,
    cats: u32,
    samoyeds: u32,
    pomeranians: u32,
    akitas: u32,
    vizslas: u32,
    goldfish: u32,
    trees: u32,
    cars: u32,
    perfumes: u32,
}

impl Sue {
    fn new(s: &str) -> Sue {
        let mut sue = Sue {
            id: 999,
            children: 999,
            cats: 999,
            samoyeds: 999,
            pomeranians: 999,
            akitas: 999,
            vizslas: 999,
            goldfish: 999,
            trees: 999,
            cars: 999,
            perfumes: 999,
        };

        for line in s.lines() {
            let id = line
                .split(": ")
                .next()
                .unwrap()
                .replace("Sue ", "")
                .parse()
                .unwrap();
            sue.id = id;
            let (_, parts) = line.split_once(": ").unwrap();
            let parts: Vec<&str> = parts.split(", ").collect();
            for part in parts {
                let (key, value) = part.split_once(": ").unwrap();
                match key {
                    "children" => sue.children = value.parse().unwrap(),
                    "cats" => sue.cats = value.parse().unwrap(),
                    "samoyeds" => sue.samoyeds = value.parse().unwrap(),
                    "pomeranians" => sue.pomeranians = value.parse().unwrap(),
                    "akitas" => sue.akitas = value.parse().unwrap(),
                    "vizslas" => sue.vizslas = value.parse().unwrap(),
                    "goldfish" => sue.goldfish = value.parse().unwrap(),
                    "trees" => sue.trees = value.parse().unwrap(),
                    "cars" => sue.cars = value.parse().unwrap(),
                    "perfumes" => sue.perfumes = value.parse().unwrap(),
                    _ => (),
                }
            }
        }

        sue
    }
}

fn main() {
    let input = include_str!("../input.txt");
    let my_sue = Sue::new("Sue 0: children: 3, cats: 7, samoyeds: 2, pomeranians: 3, akitas: 0, vizslas: 0, goldfish: 5, trees: 3, cars: 2, perfumes: 1");
    let mut sues = Vec::new();
    for line in input.lines() {
        sues.push(Sue::new(line));
    }

    let attrs = vec![
        "children",
        "cats",
        "samoyeds",
        "pomeranians",
        "akitas",
        "vizslas",
        "goldfish",
        "trees",
        "cars",
        "perfumes",
    ];

    part1(&attrs, &sues, &my_sue);
    part2(&attrs, &sues, &my_sue);
}
fn part1(attrs: &[&str], sues: &[Sue], my_sue: &Sue) {
    let mut filtered_sues = sues.to_owned();
    for attr in attrs.iter() {
        filtered_sues = filtered_sues
            .iter()
            .filter(|sue| {
                return match *attr {
                    "cats" => match sue.cats {
                        999 => true,
                        0 => true,
                        _ => sue.cats == my_sue.cats,
                    },
                    "trees" => match sue.trees {
                        999 => true,
                        0 => true,
                        _ => sue.trees == my_sue.trees,
                    },
                    "pomeranians" => match sue.pomeranians {
                        999 => true,
                        0 => true,
                        _ => sue.pomeranians == my_sue.pomeranians,
                    },
                    "goldfish" => match sue.goldfish {
                        999 => true,
                        0 => true,
                        _ => sue.goldfish == my_sue.goldfish,
                    },
                    "children" => match sue.children {
                        999 => true,
                        0 => true,
                        _ => sue.children == my_sue.children,
                    },
                    "samoyeds" => match sue.samoyeds {
                        999 => true,
                        0 => true,
                        _ => sue.samoyeds == my_sue.samoyeds,
                    },
                    "cars" => match sue.cars {
                        999 => true,
                        0 => true,
                        _ => sue.cars == my_sue.cars,
                    },
                    "perfumes" => match sue.perfumes {
                        999 => true,
                        0 => true,
                        _ => sue.perfumes == my_sue.perfumes,
                    },
                    "akitas" => match sue.akitas {
                        999 => true,
                        0 => true,
                        _ => sue.akitas == my_sue.akitas,
                    },

                    "vizslas" => match sue.vizslas {
                        999 => true,
                        0 => true,
                        _ => sue.vizslas == my_sue.vizslas,
                    },
                    _ => panic!("unknown attr"),
                };
            })
            .cloned()
            .collect::<Vec<Sue>>();
    }
    match filtered_sues.len() {
        1 => {
            println!("Part 1: {}", filtered_sues[0].id);
        }
        _ => panic!("no sue found"),
    }
}

fn part2(attrs: &[&str], sues: &[Sue], my_sue: &Sue) {
    let mut filtered_sues = sues.to_owned();
    for attr in attrs.iter() {
        filtered_sues = filtered_sues
            .iter()
            .filter(|sue| {
                return match *attr {
                    "cats" => match sue.cats {
                        999 => true,
                        0 => true,
                        _ => sue.cats > my_sue.cats,
                    },
                    "trees" => match sue.trees {
                        999 => true,
                        0 => true,
                        _ => sue.trees > my_sue.trees,
                    },
                    "pomeranians" => match sue.pomeranians {
                        999 => true,
                        0 => true,
                        _ => sue.pomeranians < my_sue.pomeranians,
                    },
                    "goldfish" => match sue.goldfish {
                        999 => true,
                        0 => true,
                        _ => sue.goldfish < my_sue.goldfish,
                    },
                    "children" => match sue.children {
                        999 => true,
                        0 => true,
                        _ => sue.children == my_sue.children,
                    },
                    "samoyeds" => match sue.samoyeds {
                        999 => true,
                        0 => true,
                        _ => sue.samoyeds == my_sue.samoyeds,
                    },
                    "cars" => match sue.cars {
                        999 => true,
                        0 => true,
                        _ => sue.cars == my_sue.cars,
                    },
                    "perfumes" => match sue.perfumes {
                        999 => true,
                        0 => true,
                        _ => sue.perfumes == my_sue.perfumes,
                    },
                    "akitas" => match sue.akitas {
                        999 => true,
                        0 => true,
                        _ => sue.akitas == my_sue.akitas,
                    },

                    "vizslas" => match sue.vizslas {
                        999 => true,
                        0 => true,
                        _ => sue.vizslas == my_sue.vizslas,
                    },
                    _ => panic!("unknown attr"),
                };
            })
            .cloned()
            .collect::<Vec<Sue>>();
    }
    match filtered_sues.len() {
        1 => {
            println!("Part 2: {}", filtered_sues[0].id);
        }
        _ => {
            println!("Part 2: one of:");
            filtered_sues.iter().for_each(|sue| {
                println!("{}", sue.id);
            });
        }
    }
}

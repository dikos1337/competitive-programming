use std::collections::HashSet;

struct WirePosition {
    x: i32,
    y: i32,
    path: HashSet<(i32, i32, i32)>,
    steps: i32,
}

impl WirePosition {
    fn new(x: i32, y: i32) -> WirePosition {
        WirePosition {
            x: x,
            y: y,
            path: HashSet::new(),
            steps: 0,
        }
    }

    fn parse_path(&mut self, path: &str) {
        let direction = &path[0..1];
        let distance = &path[1..].parse().unwrap();
        match direction {
            "U" => {
                for i in 1..=*distance {
                    self.steps += 1;
                    self.path.insert((self.x, self.y + i, self.steps));
                }
                self.y += distance
            }
            "D" => {
                for i in 1..=*distance {
                    self.steps += 1;
                    self.path.insert((self.x, self.y - i, self.steps));
                }
                self.y -= distance
            }
            "L" => {
                for i in 1..=*distance {
                    self.steps += 1;
                    self.path.insert((self.x - i, self.y, self.steps));
                }
                self.x -= distance
            }
            "R" => {
                for i in 1..=*distance {
                    self.steps += 1;
                    self.path.insert((self.x + i, self.y, self.steps));
                }
                self.x += distance
            }
            _ => panic!("Unknown direction: {}", direction),
        }
    }

    fn get_intersections(&self, other: &WirePosition) -> HashSet<(i32, i32)> {
        let mut intersections = HashSet::new();
        let mut paths1 = HashSet::new();
        let mut paths2 = HashSet::new();

        for point in &self.path {
            paths1.insert((point.0, point.1));
        }
        for point in &other.path {
            paths2.insert((point.0, point.1));
        }
        for p1 in paths1 {
            if paths2.contains(&p1) {
                intersections.insert((p1.0, p1.1));
            }
        }

        intersections
    }

    fn get_steps(&self, point: &(i32, i32)) -> i32 {
        let mut steps = 0;
        for p in &self.path {
            if p.0 == point.0 && p.1 == point.1 {
                steps = p.2;
                break;
            }
        }
        steps
    }
}

fn lowest_manhattan_distance(intersections: &HashSet<(i32, i32)>) -> i32 {
    let mut lowest = std::i32::MAX;
    for point in intersections {
        let distance = point.0.abs() + point.1.abs();
        if distance < lowest {
            lowest = distance;
        }
    }
    lowest
}

fn main() {
    let input = include_str!("../input.txt");
    let mut lines = input.lines();
    let wire1_path = lines.next().unwrap().trim().split(',').collect::<Vec<_>>();
    let wire2_path = lines.next().unwrap().trim().split(',').collect::<Vec<_>>();

    let mut wire1 = WirePosition::new(0, 0);
    let mut wire2 = WirePosition::new(0, 0);
    wire1_path
        .into_iter()
        .for_each(|path| wire1.parse_path(path));

    wire2_path
        .into_iter()
        .for_each(|path| wire2.parse_path(path));

    let intersections = wire1.get_intersections(&wire2);
    let answer = lowest_manhattan_distance(&intersections);
    println!("Part 1 answer: {}", answer);

    let steps = intersections
        .into_iter()
        .map(|point| wire1.get_steps(&point) + wire2.get_steps(&point))
        .min()
        .unwrap();
    println!("Part 2 answer: {}", steps);
}

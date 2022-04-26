use std::collections::HashSet;

struct Position {
    x: i32,
    y: i32,
    degrees: i32,
    visited: HashSet<(i32, i32)>,
    first_visited_twice: Option<(i32, i32)>,
}

impl Position {
    fn new() -> Position {
        Position {
            x: 0,
            y: 0,
            degrees: 0,
            visited: HashSet::new(),
            first_visited_twice: None,
        }
    }

    fn parse(&mut self, s: &str) {
        match &s[..1] {
            "R" => self.degrees += 90,
            "L" => self.degrees -= 90,
            _ => panic!("Unknown direction: {}", &s[..1]),
        }
        let step: i32 = s[1..].parse().unwrap();

        let d = self.degrees % 360;
        self.visit(step, d);
    }

    fn visit(&mut self, step: i32, d: i32) {
        for _ in 0..step {
            match d {
                -270 => self.y += 1,
                -180 => self.x -= 1,
                -90 => self.y -= 1,
                0 => self.x += 1,
                90 => self.y += 1,
                180 => self.x -= 1,
                270 => self.y -= 1,
                _ => panic!("Unknown degrees: {}", self.degrees),
            }
            if self.visited.contains(&(self.x, self.y)) {
                if self.first_visited_twice.is_none() {
                    self.first_visited_twice = Some((self.x, self.y));
                }
            } else {
                self.visited.insert((self.x, self.y));
            }
        }
    }

    fn manhattan_distance(&self) -> i32 {
        self.x.abs() + self.y.abs()
    }

    fn manhattan_distance_visited(&self) -> i32 {
        self.first_visited_twice.unwrap().0.abs() + self.first_visited_twice.unwrap().1.abs()
    }
}

fn main() {
    let input = include_str!("../input.txt")
        .trim()
        .split(", ")
        .collect::<Vec<_>>();
    let mut pos = Position::new();

    for s in input {
        pos.parse(s);
    }

    println!("Part 1: {}", pos.manhattan_distance());
    println!("Part 2: {}", pos.manhattan_distance_visited());
}

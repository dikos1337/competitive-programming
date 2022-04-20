use std::{cmp::Ordering, str::Lines};

#[derive(Debug)]
struct Reindeer {
    name: String,
    speed: u32,
    duration: u32,
    rest: u32,
    distance: u32,
    _rest_time: u32,
    _duration_time: u32,
    score: u32,
}

impl Reindeer {
    fn new(name: String, speed: u32, duration: u32, rest: u32) -> Reindeer {
        Reindeer {
            name,
            speed,
            duration,
            rest,
            score: 0,
            distance: 0,
            _rest_time: 0,
            _duration_time: 0,
        }
    }

    fn step(&mut self) {
        match self._duration_time.cmp(&self.duration) {
            Ordering::Less => {
                self.distance += self.speed;
                self._duration_time += 1;
            }
            Ordering::Equal => {
                self._rest_time += 1;
            }
            Ordering::Greater => panic!("Duration time is greater than duration"),
        }
        match self._rest_time.cmp(&self.rest) {
            Ordering::Less => {}
            Ordering::Equal => {
                self._rest_time = 0;
                self._duration_time = 0;
            }
            Ordering::Greater => panic!("rest time is greater than rest time"),
        }
    }
}

fn parse_reindeers(input: Lines, reindeers: &mut Vec<Reindeer>) {
    for line in input {
        let line = line.split_ascii_whitespace().collect::<Vec<_>>();
        let name = line[0];
        let speed = line[3].parse::<u32>().unwrap();
        let duration = line[6].parse::<u32>().unwrap();
        let rest = line[13].parse::<u32>().unwrap();
        reindeers.push(Reindeer::new(name.to_string(), speed, duration, rest));
    }
}

fn main() {
    let input = include_str!("../input.txt");
    let mut reindeers = Vec::new();
    parse_reindeers(input.lines(), &mut reindeers);

    let mut max_distance = u32::MAX;
    for _ in 0..2503 {
        for reindeer in reindeers.iter_mut() {
            if reindeer.distance == max_distance {
                reindeer.score += 1;
            }
            reindeer.step();
        }
        max_distance = reindeers.iter().map(|r| r.distance).max().unwrap();
    }
    let winner_p1 = reindeers.iter().max_by_key(|r| r.distance).unwrap();
    println!("Part 1: {}", winner_p1.distance);
    let winner_p2 = reindeers.iter().max_by_key(|r| r.score).unwrap();
    println!("Part 2: {}", winner_p2.score);
}

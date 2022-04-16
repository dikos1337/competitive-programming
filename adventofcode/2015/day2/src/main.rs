struct Present {
    l: usize,
    w: usize,
    h: usize,
}

impl From<Vec<usize>> for Present {
    fn from(v: Vec<usize>) -> Self {
        Present {
            l: v[0],
            w: v[1],
            h: v[2],
        }
    }
}
impl Present {
    fn area(&self) -> usize {
        2 * self.l * self.w + 2 * self.w * self.h + 2 * self.h * self.l
    }

    fn extra_paper_area(&self) -> usize {
        let mut sides = vec![self.l, self.w, self.h];
        sides.sort_unstable();
        sides[0] * sides[1]
    }

    fn ribbon(&self) -> usize {
        let mut sides = vec![self.l, self.w, self.h];
        sides.sort_unstable();
        sides[0] + sides[0] + sides[1] + sides[1]
    }
    fn bow(&self) -> usize {
        self.l * self.w * self.h
    }
}

fn main() {
    let input = include_str!("../input.txt");
    let presents = input
        .trim()
        .split('\n')
        .map(|s| {
            s.split('x')
                .map(|s| s.parse::<usize>().unwrap())
                .collect::<Vec<usize>>()
        })
        .map(Present::from)
        .collect::<Vec<Present>>();

    let total_area = presents.iter().map(|p| p.area()).sum::<usize>();
    let total_extra_paper = presents.iter().map(|p| p.extra_paper_area()).sum::<usize>();
    let part1 = total_area + total_extra_paper;
    println!("Part 1: {}", part1);

    let total_ribbon = presents.iter().map(|p| p.ribbon()).sum::<usize>();
    let total_bow = presents.iter().map(|p| p.bow()).sum::<usize>();
    let part2 = total_ribbon + total_bow;
    println!("Part 2: {}", part2);
}

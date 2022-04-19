fn unescape(s: &str) -> String {
    let mut result = String::new();
    let mut i = 0;
    while i < s.len() {
        if s.chars().nth(i).unwrap() == '\\' {
            i += 1;
            match s.chars().nth(i).unwrap() {
                '\"' => result.push('\"'),
                '\\' => result.push('\\'),
                'x' => {
                    i += 1;
                    let mut hex = String::new();
                    hex.push(s.chars().nth(i).unwrap());
                    i += 1;
                    hex.push(s.chars().nth(i).unwrap());
                    result.push(u8::from_str_radix(&hex, 16).unwrap() as char);
                }
                _ => {
                    result.push('\\');
                    result.push(s.chars().nth(i).unwrap());
                }
            }
        } else {
            result.push(s.chars().nth(i).unwrap());
        }
        i += 1;
    }
    result
}

fn escape(s: &str) -> String {
    let mut result = String::new();
    for c in s.chars() {
        match c {
            '\"' => result.push_str("\\\""),
            '\\' => result.push_str("\\\\"),
            _ => result.push(c),
        }
    }
    result
}

#[cfg(test)]
mod tests {
    use super::*;

    fn solve_p1(line: &str) -> String {
        let s = unescape(&mut line.to_string());
        s
    }

    #[test]
    fn p1_test1() {
        let input = r#""#;
        let out = solve_p1(input);
        assert_eq!(out.chars().count(), 0);
    }

    #[test]
    fn p1_test2() {
        let input = r#"abc"#;
        let out = solve_p1(input);
        assert_eq!(out.chars().count(), 3);
    }

    #[test]
    fn p1_test3() {
        let input = r#"aaa\"aaa"#;
        let out = solve_p1(input);
        assert_eq!(out.chars().count(), 7);
    }

    #[test]
    fn p1_test4() {
        let input = r#"\x27"#;
        let out = solve_p1(input);
        assert_eq!(out.chars().count(), 1);
    }

    #[test]
    fn p1_test5() {
        let input = r#"bvm\x28aa\\\\\"pywuhaniox\\z\\hbp\xd7mold"#;
        let out = solve_p1(input);
        assert_eq!(out.chars().count(), 30);
    }

    #[test]
    fn p1_test6() {
        let input = r#"u\x43ntr\\\\byyfjr\"iveujvnwsqbnpuvrta"#;
        let out = solve_p1(input);
        assert_eq!(out.chars().count(), 32);
    }

    #[test]
    fn p1_test7() {
        let input = r#"zdvrvn\xd0mtfvpylbn\\\\sxcznrzugwznl"#;
        let out = solve_p1(input);
        assert_eq!(out.chars().count(), 31);
    }

    #[test]
    fn p1_test8() {
        let input = r#"kllvhdp\"prjikzrrc\"adgpegc\\\"gk"#;
        let out = solve_p1(input);
        assert_eq!(out.chars().count(), 29);
    }

    #[test]
    fn p2_test1() {
        let input = r#""""#;
        let out = escape(&input.to_string());
        println!("{}", out);
        assert_eq!(out.chars().count() + 2, 6);
    }

    #[test]
    fn p2_test2() {
        let input = r#""\x27""#;
        let out = escape(&input.to_string());
        println!("{}", out);
        assert_eq!(out.chars().count() + 2, 11);
    }

    #[test]
    fn p2_test3() {
        let input = r#""aaa\"aaa""#;
        let out = escape(&input.to_string());
        println!("{}", out);
        assert_eq!(out.chars().count() + 2, 16);
    }
}

fn main() {
    let input = include_str!("../input.txt");
    let mut part1 = 0;
    let mut part2 = 0;
    for line in input.lines() {
        let line_len = line.len();
        let p1 = unescape(line);
        let p1_len = p1.chars().count() - 2;
        part1 += line_len - p1_len;

        let p2 = escape(line);
        let p2_len = p2.chars().count() + 2;
        part2 += p2_len - line_len;
    }
    println!("Part 1: {}", part1);
    println!("Part 2: {}", part2);
}

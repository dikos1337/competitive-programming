fn is_valid_password_part1(password: &str) -> bool {
    let mut has_double = false;
    let mut last_digit = None;
    let digits = password.chars().collect::<Vec<char>>();
    for digit in digits {
        if digit < last_digit.unwrap_or('0') {
            return false;
        }
        if digit == last_digit.unwrap_or('0') {
            has_double = true;
        }
        last_digit = Some(digit);
    }
    has_double
}

fn is_valid_password_part2(password: &str) -> bool {
    let mut has_double = std::collections::HashMap::new();
    let mut in_larger_group = std::collections::HashMap::new();
    let mut last_digit = None;
    let mut last_last_digit = None;

    let digits = password.chars().collect::<Vec<char>>();
    for digit in digits {
        if digit < last_digit.unwrap_or('0') {
            return false;
        }
        if digit == last_digit.unwrap_or('0') {
            has_double.insert(digit, true);
        }
        if digit == last_digit.unwrap_or('0') && digit == last_last_digit.unwrap_or('0') {
            in_larger_group.insert(digit, true);
        }

        match last_digit {
            Some(ld) => {
                last_last_digit = Some(ld);
                last_digit = Some(digit);
            }
            None => {
                last_digit = Some(digit);
            }
        }
    }
    match has_double.len() {
        1.. => match in_larger_group.len() {
            0 => true,
            _ => has_double.iter().any(|(k, v)| {
                if *v {
                    !in_larger_group.contains_key(k)
                } else {
                    true
                }
            }),
        },
        _ => false,
    }
}

fn main() {
    let mut input = "178416-676461"
        .split("-")
        .map(|x| x.parse::<u32>().unwrap());
    let low = input.next().unwrap();
    let high = input.next().unwrap();

    let cnt = (low..=high)
        .filter(|&x| is_valid_password_part1(x.to_string().as_str()))
        .count();
    println!("Part 1: {}", cnt);
    let cnt = (low..=high)
        .filter(|&x| is_valid_password_part2(x.to_string().as_str()))
        .count();
    println!("Part 2: {}", cnt);
}

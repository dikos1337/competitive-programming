fn count_chars_in_row(s: String) -> Vec<(i32, char)> {
    let mut count = 0;
    let mut prev = '@';
    let mut pairs = Vec::new();
    for c in s.chars() {
        if c == prev {
            count += 1;
        } else {
            if prev != '@' {
                pairs.push((count, prev));
            }
            count = 1;
        }

        prev = c;
    }
    pairs.push((count, prev));
    pairs
}

fn main() {
    let mut shared_input = String::from("3113322113");

    println!("{}", shared_input);

    for (i, _) in (0..50).enumerate() {
        let pairs = count_chars_in_row(shared_input);
        shared_input = pairs
            .iter()
            .map(|(c, c2)| format!("{}{}", c, c2))
            .collect::<Vec<String>>()
            .join("");

        if i == 39 {
            println!("Part 1: {}", shared_input.chars().count());
        }
    }
    println!("Part 2: {}", shared_input.chars().count());
}

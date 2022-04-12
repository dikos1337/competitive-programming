use std::io::stdin;
use std::iter::Iterator;

fn main() {
    let mut guest_name = String::new();
    let mut owner_name = String::new();
    let mut chars = String::new();

    stdin().read_line(&mut guest_name).unwrap();
    stdin().read_line(&mut owner_name).unwrap();
    stdin().read_line(&mut chars).unwrap();

    guest_name = guest_name.trim().to_string() + owner_name.trim();

    let mut names: Vec<char> = guest_name.chars().collect();
    names.sort_by(|a, b| a.cmp(b));

    let mut chars: Vec<char> = chars.trim().chars().collect();
    chars.sort_by(|a, b| a.cmp(b));

    if names == chars {
        println!("YES");
    } else {
        println!("NO")
    }
}

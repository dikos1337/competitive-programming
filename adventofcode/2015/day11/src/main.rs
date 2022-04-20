use std::cmp::Ordering;

fn valid_password(b: &[u8]) -> bool {
    fn contain_iol(b: &[u8]) -> bool {
        b.iter().any(|&c| c == b'i' || c == b'o' || c == b'l')
    }

    fn straight_of_three(b: &[u8]) -> bool {
        let mut last = b[0];
        let mut cnt = 1;
        for &c in b.iter().skip(1) {
            match c.cmp(&(last + 1)) {
                Ordering::Equal => cnt += 1,
                Ordering::Less => cnt = 1,
                Ordering::Greater => cnt = 1,
            }
            if cnt == 3 {
                return true;
            }
            last = c;
        }
        false
    }

    fn two_pairs(b: &[u8]) -> bool {
        let mut skip_next = false; // non-overlapping
        let mut cnt = 0;
        for w2 in b.windows(2) {
            if skip_next {
                skip_next = false;
                continue;
            }
            if w2[0] == w2[1] {
                cnt += 1;
                skip_next = true;
            }
        }
        cnt >= 2
    }

    !contain_iol(b) && straight_of_three(b) && two_pairs(b)
}

fn update_last_char(input: &mut [u8], size: usize, offset: &mut usize) {
    match input[size - *offset] {
        b'z' => {
            input[size - *offset] = b'a';
            *offset += 1;
            update_last_char(input, size, offset);
        }
        _ => {
            input[size - *offset] += 1;
            *offset = 1
        }
    }
}

fn main() {
    let mut input = "hxbxwxba".as_bytes().to_vec();
    let size = input.len();
    let mut offset = 1;
    loop {
        if valid_password(&input) {
            let answer = String::from_utf8(input.clone()).unwrap();
            println!("Part 1: {:?}", answer);
            break;
        }
        update_last_char(&mut input, size, &mut offset)
    }
    loop {
        update_last_char(&mut input, size, &mut offset);
        if valid_password(&input) {
            let answer = String::from_utf8(input.clone()).unwrap();
            println!("Part 2: {:?}", answer);
            break;
        }
    }
}

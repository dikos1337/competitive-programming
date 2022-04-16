fn main() {
    let input = String::from("yzbqklnj");

    let mut i = 0;
    loop {
        let hash = md5::compute(format!("{}{}", input, i).as_bytes());
        if format!("{:x}", hash).starts_with("00000") {
            println!("{} {:?}", i, hash);
            break;
        }
        i += 1;
    }
    println!("Part 1: {}", i);
    loop {
        let hash = md5::compute(format!("{}{}", input, i).as_bytes());
        if format!("{:x}", hash).starts_with("000000") {
            println!("{} {:?}", i, hash);
            break;
        }
        i += 1;
    }
    println!("Part 2: {}", i);
}

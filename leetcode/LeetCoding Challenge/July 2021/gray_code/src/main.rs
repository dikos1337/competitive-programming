use std::collections::HashMap;
use std::hash::Hash;

fn memoize<A, R, F>(cache: &mut HashMap<A, R>, func: F, arg: A) -> R
where
    A: Eq + Hash + Clone,
    R: Clone,
    F: Fn(&mut HashMap<A, R>, A) -> R,
{
    match cache.get(&arg).map(|x| x.clone()) {
        Some(result) => result,
        None => {
            let result = func(cache, arg.clone());
            cache.insert(arg, result.clone());
            result
        }
    }
}

struct Solution {}

impl Solution {
    fn gray(cache: &mut HashMap<(i32, i32), i32>, args: (i32, i32, &mut Vec<i32>)) -> i32 {
        if args.1 == 0 {
            args.2[0] = 0;
        } else {
            let t = 1 << (args.1 - 1);
            println!("t = {:?}", t);
            for i in 0..t {
                args.2[t + i] = args.2[t - i - 1] + (1 << (args.1 - 1));
            }
        }
        if args.1 != args.0 {
            match cache.get(&(args.0, args.1)).map(|entry| entry.clone()) {
                Some(result) => result,
                None => {
                    let result = Solution::gray(cache, (args.0, args.1 + 1, args.2));
                    cache.insert((args.0, args.1 + 1), result.clone());
                    result
                }
            };

            // Solution::gray(cache, (args.0, args.1 + 1, args.2));
        }

        return 0;
    }

    pub fn gray_code(n: i32) -> Vec<i32> {
        if n == 1 {
            return vec![0, 1];
        }

        let mut v: Vec<i32> = vec![0; ((2 as i32).pow(n as u32) + 1) as usize];

        let mut cache: HashMap<(i32, i32), i32> = HashMap::new();

        // cache.insert((1, 1), 1);
        // println!("n:{} , v:{:?}", n, v);
        Solution::gray(&mut cache, (n, 1, &mut v));

        // memoize(&mut cache, Solution::gray, (n, 1));

        // for i in 0..(v.len() - 1) {
        //     if v[i + 1..].contains(&v[i]) {
        //         println!("contains {}", &v[i]);
        //     }
        // }

        let mut counter: HashMap<&i32, usize> = HashMap::new();

        for el in v.iter() {
            counter.insert(el, v.iter().filter(|&x| x == el).count());
        }
        // println!("h {:#?}", counter);

        for val in counter.values() {
            if *val >= 2 as usize {
                return v[..(v.len() - 1) as usize]
                    .iter()
                    .enumerate()
                    .filter(|x| v.contains(x.1))
                    .map(|f| *f.1)
                    .collect();
            }
        }

        // let z: Vec<i32> = v[..(v.len() - 1) as usize]
        //     .iter()
        //     .enumerate()
        //     .filter(|x| v.contains(x.1))
        //     .map(|f| *f.1)
        //     .collect();

        // println!("n:{} , v:{:?}", n, v);
        // println!("z: {:?}", z);
        return v;
    }
}

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_case1() {
        assert_eq!(Solution::gray_code(1), vec![0, 1]);
    }
    #[test]
    fn test_case2() {
        assert_eq!(Solution::gray_code(2), vec![0, 1, 3, 2]);
    }
    #[test]
    fn test_case3() {
        assert_eq!(Solution::gray_code(3), vec![0, 1, 3, 2, 6, 7, 5, 4]);
    }
    #[test]
    fn test_case4() {
        assert_eq!(
            Solution::gray_code(13),
            vec![
                0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8, 24, 25, 27, 26, 30, 31, 29,
                28, 20, 21, 23, 22, 18, 19, 17, 16
            ]
        );
    }
}

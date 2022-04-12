struct Solution {}

impl Solution {
    pub fn matrix_reshape(m: Vec<Vec<i32>>, r: i32, c: i32) -> Vec<Vec<i32>> {
        if (r <= 1) & (c <= 1) {
            return m;
        }
        let len_y = m.len();
        let n = m[0].len();
        if (len_y * n) as i32 != (r * c) {
            return m;
        }

        let mut one_d: Vec<i32> = vec![0; (r * c) as usize];

        for i in 0..(len_y * n) {
            one_d[i] = m[i / n][i % n];
        }

        let mut new_m: Vec<Vec<i32>> = vec![vec![0; c as usize]; r as usize];

        for i in 0..(r * c) as usize {
            new_m[i / c as usize][i % c as usize] = one_d[i]
        }

        new_m
    }
}

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_case1() {
        assert_eq!(
            Solution::matrix_reshape(vec![vec![1, 2], vec![3, 4]], 1, 4),
            vec![vec![1, 2, 3, 4]]
        );
    }

    #[test]
    fn test_case2() {
        assert_eq!(
            Solution::matrix_reshape(vec![vec![1, 2], vec![3, 4]], 2, 4),
            vec![vec![1, 2], vec![3, 4]]
        );
    }
}

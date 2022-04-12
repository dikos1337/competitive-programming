struct Solution {}

impl Solution {
    pub fn kth_smallest(matrix: Vec<Vec<i32>>, k: i32) -> i32 {
        let len_y = matrix.len();
        let n = matrix[0].len();

        let mut one_d: Vec<i32> = vec![0; (len_y * n) as usize];
        for i in 0..(len_y * n) {
            one_d[i] = matrix[i / n][i % n];
        }

        one_d.sort();
        return one_d[(k - 1) as usize];
    }
}

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_case1() {
        assert_eq!(
            Solution::kth_smallest(vec![vec![1, 5, 9], vec![10, 11, 13], vec![12, 13, 15]], 8),
            13
        );
    }

    #[test]
    fn test_case2() {
        assert_eq!(Solution::kth_smallest(vec![vec![-5]], 1), -5);
    }
}

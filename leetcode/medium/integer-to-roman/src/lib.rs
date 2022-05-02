struct Solution;

impl Solution {
    pub fn int_to_roman(num: i32) -> String {
        let map = vec![
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ];

        let mut remainder = num;
        let mut result = Vec::new();

        for (num, literal) in map {
            while num <= remainder {
                result.push(literal);
                remainder -= num;
            }
        }

        result.join("")
    }
}

#[cfg(test)]
mod tests {
    use crate::*;

    #[test]
    fn test_1() {
        assert_eq!(Solution::int_to_roman(3), "III");
    }

    #[test]
    fn test_2() {
        assert_eq!(Solution::int_to_roman(27), "XXVII");
    }

    #[test]
    fn test_3() {
        assert_eq!(Solution::int_to_roman(58), "LVIII");
    }

    #[test]
    fn test_4() {
        assert_eq!(Solution::int_to_roman(1994), "MCMXCIV");
    }

    #[test]
    fn test_5() {
        assert_eq!(Solution::int_to_roman(3999), "MMMCMXCIX");
    }

    #[test]
    fn test_6() {
        assert_eq!(Solution::int_to_roman(10), "X");
    }

    #[test]
    fn test_7() {
        assert_eq!(Solution::int_to_roman(60), "LX");
    }

    #[test]
    fn test_8() {
        assert_eq!(Solution::int_to_roman(600), "DC");
    }
}

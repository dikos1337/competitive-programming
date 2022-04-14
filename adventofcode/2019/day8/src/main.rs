const WIDTH: usize = 25;
const HEIGHT: usize = 6;

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum PixelColor {
    Black,
    White,
    Transparent,
}

impl From<u32> for PixelColor {
    fn from(num: u32) -> PixelColor {
        match num {
            0 => PixelColor::Black,
            1 => PixelColor::White,
            2 => PixelColor::Transparent,
            _ => panic!("Invalid pixel color"),
        }
    }
}

fn part1(input: &str) -> Vec<Vec<u32>> {
    let num_layers = input.len() / (WIDTH * HEIGHT);
    let mut image = vec![vec![0; WIDTH * HEIGHT]; num_layers];

    for (i, c) in input.chars().enumerate() {
        let layer = i / (WIDTH * HEIGHT);
        let pixel = i % (WIDTH * HEIGHT);
        image[layer][pixel] = c.to_digit(10).unwrap();
    }

    let fewest_0_layer = image
        .iter()
        .min_by_key(|layer| layer.iter().filter(|&&p| p == 0).count())
        .unwrap();

    let num1_cnt = fewest_0_layer.iter().filter(|&&p| p == 1).count();
    let num2_cnt = fewest_0_layer.iter().filter(|&&p| p == 2).count();
    println!("Part 1: {}", num1_cnt * num2_cnt);
    image
}

fn part2(image: &Vec<Vec<u32>>) {
    let mut image_out = vec![vec![PixelColor::Transparent; WIDTH]; HEIGHT];

    for y in 0..HEIGHT {
        for x in 0..WIDTH {
            let mut color = PixelColor::Transparent;
            for layer in image {
                let pixel = layer[y * WIDTH + x];
                if PixelColor::Transparent != pixel.into() {
                    color = pixel.into();
                    break;
                }
            }
            image_out[y][x] = color;
        }
    }

    println!("Part 2:");
    for row in image_out {
        for pixel in row {
            print!(
                "{}",
                match pixel {
                    PixelColor::Black => "#",
                    PixelColor::White => "█",
                    PixelColor::Transparent => " ",
                }
            );
        }
        println!();
    }
}
fn main() {
    let input = include_str!("../input.txt").trim();
    let image = part1(input);
    part2(&image);
}

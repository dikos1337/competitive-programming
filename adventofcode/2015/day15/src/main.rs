use itertools::Itertools;

#[derive(Debug)]
struct Ingredient {
    capacity: i32,
    durability: i32,
    flavor: i32,
    texture: i32,
    calories: i32,
}

#[derive(Debug)]
struct Cookie {
    ingredients: Vec<Ingredient>,
    capacities: Vec<i32>,
    durability: Vec<i32>,
    flavors: Vec<i32>,
    textures: Vec<i32>,
    calories: Vec<i32>,
}

fn main() {
    let input = include_str!("../input.txt");
    let mut ingredients: Vec<Ingredient> = Vec::new();
    fill_ingredients(input, &mut ingredients);

    let mut cookie = Cookie {
        capacities: Vec::new(),
        durability: Vec::new(),
        flavors: Vec::new(),
        textures: Vec::new(),
        calories: Vec::new(),
        ingredients,
    };

    let mut max_score = 0;
    let mut max_score_p2 = 0;

    let iter = (1..99).permutations(cookie.ingredients.len());
    for teaspoons in iter {
        let sum: i32 = teaspoons.iter().sum();
        if sum != 100 {
            continue;
        }
        for (i, ing) in cookie.ingredients.iter().enumerate() {
            cookie.capacities.push(ing.capacity * teaspoons[i]);
            cookie.durability.push(ing.durability * teaspoons[i]);
            cookie.flavors.push(ing.flavor * teaspoons[i]);
            cookie.textures.push(ing.texture * teaspoons[i]);
            cookie.calories.push(ing.calories * teaspoons[i]);
            let score = cookie.calculate_score();
            let score_p2 = cookie.calculate_score_with_calories();
            if score > max_score {
                max_score = score;
            }
            if score_p2 > max_score_p2 {
                max_score_p2 = score_p2;
            }
        }
        cookie.clear();
    }
    println!("Part 1: {}", max_score);
    println!("Part 2: {}", max_score_p2);
}

fn fill_ingredients(input: &str, ingredients: &mut Vec<Ingredient>) {
    for line in input.lines() {
        let parts = line.split_whitespace().collect::<Vec<&str>>();
        let capacity = parts[2].trim_end_matches(',').parse::<i32>().unwrap();
        let durability = parts[4].trim_end_matches(',').parse::<i32>().unwrap();
        let flavor = parts[6].trim_end_matches(',').parse::<i32>().unwrap();
        let texture = parts[8].trim_end_matches(',').parse::<i32>().unwrap();
        let calories = parts[10].trim_end_matches('.').parse::<i32>().unwrap();
        ingredients.push(Ingredient {
            capacity,
            durability,
            flavor,
            texture,
            calories,
        });
    }
}

impl Cookie {
    fn calculate_score(&self) -> i32 {
        let capacities_sum = self.capacities.iter().sum::<i32>();
        if capacities_sum < 0 {
            return 0;
        }
        let durability_sum = self.durability.iter().sum::<i32>();
        if durability_sum < 0 {
            return 0;
        }
        let flavors_sum = self.flavors.iter().sum::<i32>();
        if flavors_sum < 0 {
            return 0;
        }
        let textures_sum = self.textures.iter().sum::<i32>();
        if textures_sum < 0 {
            return 0;
        }
        capacities_sum * durability_sum * flavors_sum * textures_sum
    }

    fn calculate_score_with_calories(&self) -> i32 {
        let calories_sum = self.calories.iter().sum::<i32>();
        if calories_sum != 500 {
            return 0;
        }
        self.calculate_score()
    }

    fn clear(&mut self) {
        self.capacities.clear();
        self.durability.clear();
        self.flavors.clear();
        self.textures.clear();
        self.calories.clear();
    }
}

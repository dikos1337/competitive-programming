const fs = require('fs')
let input = fs.readFileSync('day7.txt', 'utf8')
  .replaceAll(" bags", "")
  .replaceAll(" bag", "");

let data = input.split("\n");
let rules = [];

function defineRule(el_splitted) {
  let rule = {
    name: el_splitted[0].trim(),
    contains: el_splitted[1].split(",").map((el) => {
      el = el.replace("no other.", "0 no other.").replace(".", "").trim();
      let [value, ...name] = el.split(" ");
      name = name.join(" ");
      value = parseInt(value, 10);
      return { name, value };
    }),
  };
  return rule;
}

// define rules
data.forEach((el) => {
  let el_splitted = el.split("contain");
  let rule = defineRule(el_splitted);
  rules.push(rule);
});


const target = "shiny gold";

function find_bags_that_contains_exact_bag(bag_name) {
  let funded_bags = [];
  for (rule of rules) {
    rule.contains.forEach((el) => {
      if (el.name === bag_name) {
        funded_bags.push(rule);
      }
    });
  }
  return funded_bags;
}

let bag_pull = find_bags_that_contains_exact_bag(target);

for (bag of bag_pull) {
  let new_bags = find_bags_that_contains_exact_bag(bag.name);
  bag_pull.push(...new_bags);
}

let unique_bags = new Set(bag_pull);
console.log(unique_bags);
console.log("ANSWER =", unique_bags.size);

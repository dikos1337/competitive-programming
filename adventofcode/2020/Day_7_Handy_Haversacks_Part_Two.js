let input2 = `shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.`
  .replaceAll(" bags", "")
  .replaceAll(" bag", "");

let input = `light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.`
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

function find_rule(target_name, rule_list) {
  for (rule of rule_list) {
    if (rule.name === target_name) {
      return rule;
    }
  }
  return null;
}

function rule_value_sum(rule) {
  let sum = 0;
  if (rule.contains) {
    rule.contains.forEach((el) => {
      sum += el.value;
    });
  }
  return sum;
}

let target_rule = find_rule(target, rules);
let rules_pull = [{ ...target_rule }];

for (rule of rules_pull) {
  if (rule.contains) {
    rule.contains.forEach((el) => {
      let new_rule = find_rule(el.name, rules);
      console.log(`sum ${el.name}`, rule_value_sum(rule));
      if (new_rule) {
        rules_pull.push({ ...new_rule, rule_value_sum: rule_value_sum(rule) });
      }
    });
  }
}
// let rules_pull_set = new Set(rules_pull);

console.log("filtered_rules_pull END \n");
let filtered_rules_pull = rules_pull.filter((el) => el.rule_value_sum != 0);
for (rule of filtered_rules_pull) {
  console.log(rule);
}

let multipliers = [];
for (rule of filtered_rules_pull) {
  multipliers.push(...rule.contains);
}

let rules_for_delete = new Set(
  rules_pull.filter((el) => el.rule_value_sum == 0).map((el) => el.name)
);

multipliers = multipliers.filter((el) => !rules_for_delete.has(el.name));
console.log("multipliers", multipliers);

let answer_sum = 0; //rule_value_sum(target_rule);
// multipliers.forEach((el) => {
//   for (rule of filtered_rules_pull) {
//     if (rule.name === el.name) {
//       answer_sum += el.value + el.value * rule.rule_value_sum;
//     }
//   }
// });

let target_rule_contains = filtered_rules_pull[0].contains;
// branch_accumulator += mult.value + mult.value * r.value;
// answer_sum += branch_accumulator;
// console.log("ANSWER =", mult.value, r.value);

function pass_rule(rule_name, accumulated) {
  // console.log("name", el.name);
  let branch_accumulator = 0;
  branch_accumulator += accumulated; // CARE с этой штукой 126 во 2 варианте без 32 в 1 варинте. это ключ
  console.log("rule_name =", rule_name);
  let rule = find_rule(rule_name, filtered_rules_pull);
  let mult = find_rule(rule_name, multipliers);

  console.log("rule", rule);
  console.log("mult", mult);
  let rule_exists = rule ? true : false;
  if (rule_exists) {
    var next_rules_exists = rule ? true : false;
  } else {
    var next_rules_exists = false;
  }
  if (mult) {
    console.log("rule.rule_value_sum", rule.rule_value_sum, "accumulated=", accumulated);
    branch_accumulator = rule.rule_value_sum * mult.value;
    console.log(`accumulated`, accumulated, rule.rule_value_sum * accumulated);
  }
  if (next_rules_exists) {
    rule.contains.forEach((el) => {
      branch_accumulator += pass_rule(el.name, branch_accumulator);
    });
  }
  return branch_accumulator;
}

for (el of target_rule_contains) {
  // while (next_rule_exist) {}
  answer_sum += pass_rule(el.name, el.value);
}

console.log("target_rule_contains", target_rule_contains);
console.log("ANSWER =", answer_sum);

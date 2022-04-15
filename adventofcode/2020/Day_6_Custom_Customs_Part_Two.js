const fs = require('fs')

const sum = (accumulator, currentValue) => accumulator + currentValue;

class DefaultDict {
  constructor(defaultInit) {
    return new Proxy(
      {},
      {
        get: (target, name) =>
          name in target
            ? target[name]
            : (target[name] =
              typeof defaultInit === "function"
                ? new defaultInit().valueOf()
                : defaultInit),
      }
    );
  }
}

let input_data = fs.readFileSync('day6.txt', 'utf8')
  .split("\r\n\r\n")
  .map((el) => el.split("\r\n"))
  .map((el) => {
    if (el.length > 1) {
      let defaultDict = new DefaultDict(0);
      counter = 0;
      all_el_str = "";
      el.forEach((item) => (all_el_str += item));
      for (let i = 0; i < all_el_str.length; i++) {
        defaultDict[all_el_str[i]] += 1; // count chars
      }
      for (char in defaultDict) {
        if (defaultDict[char] == el.length) {
          counter += 1;
        }
      }
      return counter;
    } else {
      return el[0].length;
    }
  });

let answer = input_data.reduce(sum);
console.log(answer);

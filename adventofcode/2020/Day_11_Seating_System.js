let input = `L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL`
  .split("\n")
  .map((el) => Array.from(el));

const field_x_size = input[0].length;
const field_y_size = input.length;

function checkMiddle(inpMrx, current_seat, rule) {
  let allowed = ["L", "."];
  let check_result = {};
  check_result["left"] = allowed.includes(
    inpMrx[current_seat.y][current_seat.x - 1]
  )
    ? true
    : false;
  check_result["right"] = allowed.includes(
    inpMrx[current_seat.y][current_seat.x + 1]
  )
    ? true
    : false;
  check_result["top"] = allowed.includes(
    inpMrx[current_seat.y - 1][current_seat.x]
  )
    ? true
    : false;
  check_result["bottom"] = allowed.includes(
    inpMrx[current_seat.y + 1][current_seat.x]
  )
    ? true
    : false;
  check_result["topLeft"] = allowed.includes(
    inpMrx[current_seat.y - 1][current_seat.x - 1]
  )
    ? true
    : false;
  check_result["topRight"] = allowed.includes(
    inpMrx[current_seat.y - 1][current_seat.x + 1]
  )
    ? true
    : false;
  check_result["bottomLeft"] = allowed.includes(
    inpMrx[current_seat.y + 1][current_seat.x - 1]
  )
    ? true
    : false;
  check_result["bottomRight"] = allowed.includes(
    inpMrx[current_seat.y + 1][current_seat.x + 1]
  )
    ? true
    : false;

  return check_result;
}

function checkTop(inpMrx, current_seat, rule) {
  let allowed = ["L", "."];
  let check_result = {};
  check_result["left"] = allowed.includes(
    inpMrx[current_seat.y][current_seat.x - 1]
  )
    ? true
    : false;
  check_result["right"] = allowed.includes(
    inpMrx[current_seat.y][current_seat.x + 1]
  )
    ? true
    : false;
  check_result["bottom"] = allowed.includes(
    inpMrx[current_seat.y + 1][current_seat.x]
  )
    ? true
    : false;
  return check_result;
}

function checkBottom(inpMrx, current_seat, rule) {
  let allowed = ["L", "."];
  let check_result = {};
  check_result["left"] = allowed.includes(
    inpMrx[current_seat.y][current_seat.x - 1]
  )
    ? true
    : false;
  check_result["right"] = allowed.includes(
    inpMrx[current_seat.y][current_seat.x + 1]
  )
    ? true
    : false;
  check_result["top"] = allowed.includes(
    inpMrx[current_seat.y - 1][current_seat.x]
  )
    ? true
    : false;
  return check_result;
}

function checkLeft(inpMrx, current_seat, rule) {
  let allowed = ["L", "."];
  let check_result = {};

  check_result["right"] = allowed.includes(
    inpMrx[current_seat.y][current_seat.x + 1]
  )
    ? true
    : false;
  check_result["top"] = allowed.includes(
    inpMrx[current_seat.y - 1][current_seat.x]
  )
    ? true
    : false;
  check_result["bottom"] = allowed.includes(
    inpMrx[current_seat.y + 1][current_seat.x]
  )
    ? true
    : false;
  return check_result;
}
function checkRight(inpMrx, current_seat, rule) {
  let allowed = ["L", "."];
  let check_result = {};

  check_result["left"] = allowed.includes(
    inpMrx[current_seat.y][current_seat.x - 1]
  )
    ? true
    : false;
  check_result["top"] = allowed.includes(
    inpMrx[current_seat.y - 1][current_seat.x]
  )
    ? true
    : false;
  check_result["bottom"] = allowed.includes(
    inpMrx[current_seat.y + 1][current_seat.x]
  )
    ? true
    : false;
  return check_result;
}

function checkTopLeft(inpMrx, current_seat, rule) {
  let allowed = ["L", "."];
  let check_result = {};

  check_result["right"] = allowed.includes(
    inpMrx[current_seat.y][current_seat.x + 1]
  )
    ? true
    : false;
  check_result["bottom"] = allowed.includes(
    inpMrx[current_seat.y + 1][current_seat.x]
  )
    ? true
    : false;
  return check_result;
}

function checkTopRight(inpMrx, current_seat, rule) {
  let allowed = ["L", "."];
  let check_result = {};

  check_result["left"] = allowed.includes(
    inpMrx[current_seat.y][current_seat.x - 1]
  )
    ? true
    : false;
  check_result["bottom"] = allowed.includes(
    inpMrx[current_seat.y + 1][current_seat.x]
  )
    ? true
    : false;
  return check_result;
}

function checkBottomLeft(inpMrx, current_seat, rule) {
  let allowed = ["L", "."];
  let check_result = {};

  check_result["right"] = allowed.includes(
    inpMrx[current_seat.y][current_seat.x + 1]
  )
    ? true
    : false;
  check_result["top"] = allowed.includes(
    inpMrx[current_seat.y - 1][current_seat.x]
  )
    ? true
    : false;
  return check_result;
}

function checkBottomRight(inpMrx, current_seat, rule) {
  let allowed = ["L", "."];
  let check_result = {};

  check_result["left"] = allowed.includes(
    inpMrx[current_seat.y][current_seat.x - 1]
  )
    ? true
    : false;
  check_result["top"] = allowed.includes(
    inpMrx[current_seat.y - 1][current_seat.x]
  )
    ? true
    : false;
  return check_result;
}

function applyRule(inpMrx, current_seat, rule) {
  let char_to_return = null;
  let check_result = null;
  // checkMiddle
  if (
    (current_seat.x > 0) &
    (current_seat.y > 0) &
    (current_seat.y < field_y_size - 1) &
    (current_seat.x < field_x_size - 1)
  ) {
    check_result = checkMiddle(inpMrx, current_seat, rule);
  }
  // checkTop
  if (
    (current_seat.y == 0) &
    (current_seat.x < field_x_size - 1) &
    (current_seat.x > 0)
  ) {
    check_result = checkTop(inpMrx, current_seat, rule);
  }
  // checkBottom
  if (
    (current_seat.y == field_y_size - 1) &
    (current_seat.x < field_x_size - 1) &
    (current_seat.x > 0)
  ) {
    check_result = checkBottom(inpMrx, current_seat, rule);
  }
  // checkLeft
  if (
    (current_seat.y < field_y_size - 1) &
    (current_seat.x == 0) &
    (current_seat.y > 0)
  ) {
    check_result = checkLeft(inpMrx, current_seat, rule);
  }
  // checkRight
  if (
    (current_seat.y < field_y_size - 1) &
    (current_seat.x == field_x_size - 1) &
    (current_seat.y > 0)
  ) {
    check_result = checkRight(inpMrx, current_seat, rule);
  }
  // checkTopLeft
  if ((current_seat.y == 0) & (current_seat.x == 0)) {
    check_result = checkTopLeft(inpMrx, current_seat, rule);
  }
  // checkTopRight
  if ((current_seat.y == 0) & (current_seat.x == field_x_size - 1)) {
    check_result = checkTopRight(inpMrx, current_seat, rule);
  }
  // checkBottomLeft
  if ((current_seat.y == field_y_size - 1) & (current_seat.x == 0)) {
    check_result = checkBottomLeft(inpMrx, current_seat, rule);
  }
  // checkBottomRight
  if (
    (current_seat.y == field_y_size - 1) &
    (current_seat.x == field_x_size - 1)
  ) {
    check_result = checkBottomRight(inpMrx, current_seat, rule);
  }

  if (rule == "empty") {
    char_to_return = check_result
      ? Object.values(check_result).every((el) => el === true)
        ? "#"
        : "L"
      : inpMrx[current_seat.y][current_seat.x];
    return char_to_return;
  } else {
    arr_length = Object.values(check_result).length;
    switch (arr_length) {
      case 2:
        char_to_return = inpMrx[current_seat.y][current_seat.x];
        return char_to_return;
      case 8:
        char_to_return =
          Object.values(check_result).filter((x) => x === false).length >= 4
            ? "L"
            : "#";
        return char_to_return;
    }
  }
}

function doRound(inpMrx) {
  let new_matrix = inpMrx.map(function (arr) {
    return arr.slice();
  });
  for (let y = 0; y < field_y_size; y++) {
    for (let x = 0; x < field_x_size; x++) {
      let current_seat = inpMrx[y][x];
      switch (current_seat) {
        case "L":
          new_matrix[y][x] = applyRule(inpMrx, { x: x, y: y }, "empty");
          break;
        case "#":
          new_matrix[y][x] = applyRule(inpMrx, { x: x, y: y }, "occupied");
          break;
        case ".":
          continue;
      }
    }
  }
  return new_matrix;
}

let m = doRound(input);
console.log("doRound");
for (c of m) {
  console.log(c.join(""));
}

let next = doRound(m);
console.log("doRound");
for (c of next) {
  console.log(c.join(""));
}

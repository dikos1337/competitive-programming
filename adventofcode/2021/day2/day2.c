#include <stdbool.h>
#include <stdio.h>
#include <string.h>

void part1() {
  int num = 0;
  char dir[20] = {0};
  int x = 0, y = 0;

  while (scanf("%s %d", dir, &num) != EOF) {
    if (strcmp("forward", dir) == 0)
      x += num;
    if (strcmp("down", dir) == 0)
      y += num;
    if (strcmp("up", dir) == 0)
      y -= num;
  }

  printf("x=%d, y=%d, answer: %d\n", x, y, (x * y));
}

void part2() {
  int num = 0;
  char dir[20] = {0};
  int x = 0, y = 0, aim = 0;

  while (scanf("%s %d", dir, &num) != EOF) {
    if (strcmp("forward", dir) == 0) {
      x += num;
      y += num * aim;
    }
    if (strcmp("down", dir) == 0)
      aim += num;
    if (strcmp("up", dir) == 0)
      aim -= num;
  }

  printf("x=%d, y=%d, answer: %d\n", x, y, (x * y));
}

int main(int argc, char *argv[]) {
  // part1();
  part2();

  return 0;
}
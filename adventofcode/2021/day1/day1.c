#include <stdbool.h>
#include <stdio.h>

void part1() {
  int num = 0, lastnum = 0, cnt = 0;
  bool firstreaded = false;

  while (scanf("%d", &num) != EOF) {
    if (firstreaded) {
      if (num > lastnum) {
        ++cnt;
      }
    }

    lastnum = num;
    firstreaded = true;
  }
  printf("answer: %d\n", cnt);
}

void part2() {
  int n1 = 0, n2 = 0, n3 = 0, num = 0, cnt = 0, i = 0, lastsum = 0, sum = 0;
  bool n1r = false, n2r = false, n3r = false;
  while (scanf("%d", &num) != EOF) {
    if (!n1r) {
      n1 = num;
      n1r = true;
      ++i;
      printf("n1 inited: %d\n", n1);
      continue;
    }
    if (!n2r) {
      n2 = num;
      n2r = true;
      ++i;
      printf("n2 inited: %d\n", n2);
      continue;
    }
    if (!n3r) {
      n3 = num;
      n3r = true;
      lastsum = n1 + n2 + n3;
      ++i;
      printf("n3 inited: %d\n", n3);
      continue;
    }
    if (n3r) {
      switch (i % 3) {
      case 0:
        n1 = num;
        printf("i prc 3 = 0 : %d\n", i);
        break;
      case 1:
        n2 = num;
        printf("i prc 3 = 1 : %d\n", i);
        break;
      case 2:
        n3 = num;
        break;
      }
      sum = n1 + n2 + n3;
      printf("sum: %d %d %d %d\n", sum, n1, n2, n3);
      if (sum > lastsum) {
        ++cnt;
      }
      lastsum = sum;
    }
    ++i;
  }
  printf("answer: %d\n", cnt);
}

int main(int argc, char *argv[]) {
  //   part1();
  part2();

  return 0;
}
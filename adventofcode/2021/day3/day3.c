#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NUM_BITS 12
#define NUM_LINES 1000

void part1() {
  int power = 0;
  char *gamma_bits = malloc((NUM_BITS + 1) * sizeof(char));
  char *eps_bits = malloc((NUM_BITS + 1) * sizeof(char));

  // memset(gamma_bits, 0, NUM_BITS + 1);
  char num[NUM_BITS + 1];
  char **table = malloc(NUM_LINES * sizeof(*table));
  for (int i = 0; scanf("%s", num) != EOF; ++i) {
    table[i] = malloc(NUM_BITS + 1); // +1 for '\0'
    sprintf(table[i], "%s", num);
  }

  for (int j = 0; j < NUM_BITS; ++j) {
    int bit0cnt = 0;
    int bit1cnt = 0;
    int i = 0;

    // GAMMA and EPS count
    while (table[i] != NULL) {
      char tmp2[2];
      tmp2[0] = table[i][j];
      tmp2[1] = '\0';
      if (strcmp(tmp2, "0") == 0) {
        ++bit0cnt;
      } else {
        ++bit1cnt;
      }
      ++i;
    }

    printf("bit0cnt %d ; bit0cnt %d\n", bit0cnt, bit1cnt);

    if (bit0cnt > bit1cnt) {
      gamma_bits[j] = '0';
      eps_bits[j] = '1';

    } else {
      gamma_bits[j] = '1';
      eps_bits[j] = '0';
    }
  }

  // str bin to int 10
  int gamma = strtol(gamma_bits, NULL, 2);
  int eps = strtol(eps_bits, NULL, 2);
  power = gamma * eps;
  printf("answer: %d * %d = %d\n", gamma, eps, power);

  free(table);
  free(gamma_bits);
  free(eps_bits);
}

int len_table(char **table) {
  int cnt = 0;
  // for (int i = 0; table[i] != NULL; ++i) {
  //   printf("lentable str %s\n", table[i]);
  //   ++cnt;
  // }
  while (*table != NULL) {
    ++cnt;
    table++;
  }
  printf("len_table cnt: %d\n", cnt);
  return cnt;
}
char **filter_table(char **table, int table_len, char by_char, int char_pos,
                    int *new_table_len) {

  int cnt = 0, i = 0;
  char **new_table = malloc(table_len * sizeof(*new_table));
  printf("filter by %c\n", by_char);
  for (i = 0; i < table_len; ++i) {
    if (table[i][char_pos] == by_char) {
      new_table[cnt] = malloc(NUM_BITS + 1); // +1 for '\0'
      strcpy(new_table[cnt], table[i]);
      ++cnt;
    }
  }

  // free old table
  for (i = 0; i < table_len; ++i) {
    free(table[i]);
  }
  free(table);

  for (i = 0; i < cnt; ++i) {
    printf("new table: %s\n", new_table[i]);
  }
  printf("filter_table end, cnt=%d retsize=%d \n", cnt, len_table(new_table));
  new_table = realloc(new_table, cnt * sizeof(*new_table));
  *new_table_len = cnt;
  return new_table;
}

void part2() {
  char num[NUM_BITS + 1];
  // char oxygen[NUM_BITS + 1];
  // char co2[NUM_BITS + 1];

  char **table = malloc(NUM_LINES * sizeof(*table));
  char **table2 = malloc(NUM_LINES * sizeof(*table2));

  for (int i = 0; scanf("%s", num) != EOF; ++i) {
    table[i] = malloc(NUM_BITS + 1);  // +1 for '\0'
    table2[i] = malloc(NUM_BITS + 1); // +1 for '\0'

    sprintf(table[i], "%s", num);
    strcpy(table2[i], table[i]);
  }

  // TABLE 1
  int table_len = len_table(table);
  int *table_len_ptr = &table_len;
  printf("len_table: %d\n", *table_len_ptr);
  for (int j = 0; j < NUM_BITS || *table_len_ptr > 1; ++j) {
    printf("j=%d\n", j);
    int bit0cnt = 0;
    int bit1cnt = 0;

    for (int i = 0; i < *table_len_ptr; ++i) {
      printf("i=%d\n", i);

      char tmp2[2] = {table[i][j], '\0'};
      if (strcmp(tmp2, "0") == 0) {
        ++bit0cnt;
      } else {
        ++bit1cnt;
      }
    }

    printf("bit0cnt %d ; bit1cnt %d\n", bit0cnt, bit1cnt);
    printf("len_table: %d\n", *table_len_ptr);

    if (bit0cnt > bit1cnt) {
      table = filter_table(table, *table_len_ptr, '0', j, table_len_ptr);
      // table_len = len_table(table);
      printf("bit0cnt\n");
    } else {
      table = filter_table(table, *table_len_ptr, '1', j, table_len_ptr);
      // table_len = len_table(table);
      printf("bit1cnt\n");
    }
  }
  // TABLE 2
  int table2_len = len_table(table2);
  int *table2_len_ptr = &table2_len;
  printf("len_table2: %d\n", *table2_len_ptr);
  for (int j = 0; j<NUM_BITS && * table2_len_ptr> 1; ++j) {
    printf("j=%d\n", j);
    int bit0cnt = 0;
    int bit1cnt = 0;

    for (int i = 0; i < *table2_len_ptr; ++i) {
      printf("i=%d\n", i);

      char tmp22[2] = {table2[i][j], '\0'};
      if (strcmp(tmp22, "0") == 0) {
        ++bit0cnt;
      } else {
        ++bit1cnt;
      }
    }

    printf("bit0cnt %d ; bit1cnt %d\n", bit0cnt, bit1cnt);
    printf("len_table: %d\n", *table2_len_ptr);

    if (bit0cnt <= bit1cnt) {
      table2 = filter_table(table2, *table2_len_ptr, '0', j, table2_len_ptr);
      // table_len = len_table(table);
      printf("bit0cnt\n");
    } else {
      table2 = filter_table(table2, *table2_len_ptr, '1', j, table2_len_ptr);
      // table_len = len_table(table);
      printf("bit1cnt\n");
    }
  }
  char *oxygen_generator_rating_value = table[0];
  printf("oxygen_generator_rating_value: %s\n", oxygen_generator_rating_value);
  char *CO2_scrubber_rating = table2[0];
  printf("CO2_scrubber_rating: %s\n", CO2_scrubber_rating);
  printf("answer?: %ld\n", strtol(oxygen_generator_rating_value, NULL, 2) *
                               strtol(CO2_scrubber_rating, NULL, 2));
  free(table);
  free(table2);
}

int main(int argc, char *argv[]) {
  // part1();
  part2();

  return 0;
}
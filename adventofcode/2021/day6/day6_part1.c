#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int *update_state(int *old_state, int *size) {
  int *new_state = malloc((*size) * 2 * sizeof(int));
  memcpy(new_state, old_state, (*size) * sizeof(int));
  int size_add = 0;
  int append_idx = 0;
  for (int i = 0; i < *size; ++i) {
    if (old_state[i] > 0) {
      new_state[i] = old_state[i] - 1;
    }
    if (old_state[i] == 0) {
      new_state[i] = 6;
      new_state[*size + append_idx] = 8;
      ++append_idx;
      ++size_add;
    }
  }
  *size += size_add;
  new_state = realloc(new_state, *size * sizeof(int));
  free(old_state);
  return new_state;
}

void print_nums(const int *nums, const int *size) {
  for (int i = 0; i < *size; ++i) {
    printf("%d ", nums[i]);
  }
  printf("\n");
}

int main(int argc, char **argv) {
  int size = 0;
  int *size_ptr = &size;

  char *numstring = malloc(1000 * sizeof(char));
  int *nums = malloc(300 * sizeof(int));

  scanf("%s", numstring);
  printf("%s\n", numstring);

  char *token = strtok(numstring, ",");

  // loop through the string to extract all other tokens
  int i = 0;
  while (token != NULL) {
    nums[i] = atoi(token);
    token = strtok(NULL, ",");
    ++i;
    ++(*size_ptr);
  }
  print_nums(nums, size_ptr);

  int times;
  for (times = 0; times < 80; ++times) {
    nums = update_state(nums, size_ptr);
    // print_nums(nums, size_ptr);
  }
  printf("i=%d size=%d\n", times, *size_ptr);

  return 0;
}

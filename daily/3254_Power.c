#include <stdlib.h>
#include <stdio.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* resultsArray(int* nums, int numsSize, int k, int* returnSize) {
    *returnSize = numsSize - k + 1;
    int* rs = malloc(sizeof(int) * *returnSize);
    int consecutive_sorted_count = 0;
    int subarr = 0;
    for (int i = 0; i < numsSize; i++) {
        if (i == 0 || nums[i] - nums[i - 1] == 1) {
            consecutive_sorted_count++;
        } else {
            consecutive_sorted_count = 1;
        }
        if (consecutive_sorted_count >= k) {
            rs[subarr++] = nums[i];
        } else if (consecutive_sorted_count < k && i >= k - 1) {
            rs[subarr++] = -1;
        }
    }
    return rs;
}
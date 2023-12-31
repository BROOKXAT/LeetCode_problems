# 3 Sum Problem

## Problem Description
Given an array of integers, find all unique triplets in the array that sum up to a specific target.

## Example
- **Input:** `[-1, 0, 1, 2, -1, -4]`, **Target:** `0`
  - **Output:** `[ [-1, 0, 1], [-1, -1, 2] ]`

## Two Pointers Solution
The Two Pointers approach is an efficient way to solve the 3 Sum problem.

1. **Sort the array:** Arrange the input array in ascending order.

2. **Iterate through the array:** Use a loop to iterate through each element in the array.

3. **Use Two Pointers:** For each element at index `i`, use two pointers (`low` and `high`) to find a pair that sums to the target (`-nums[i]`). Adjust the pointers based on the comparison of the sum with the target.

   - If the sum is equal to the target, add the triplet to the result.
   - If the sum is less than the target, move the low pointer to the right.
   - If the sum is greater than the target, move the high pointer to the left.

4. **Handle Duplicates:** Skip identical elements during the iteration to avoid duplicate triplets.

### Time and Space Complexity
- **Time complexity:** O(n^2) - The two-pointer approach takes O(n) per iteration, and we have O(n) iterations.
- **Space complexity:** O(1) - The algorithm uses only a constant amount of space.

## HashMap Solution
The HashMap solution involves using a dictionary to efficiently check for the existence of a complement in the array.

1. **Sort the array:** Arrange the input array in ascending order.

2. **Edge Cases:** Check for edge cases where the length of the array is less than 3 or the first element is greater than 0.

3. **Create a HashMap:** Create a dictionary (`hashMap`) to store the indices of elements in the array.

4. **Hashing Indices:** Iterate through the array and hash the indices of each element.

5. **Iterate through the array:** Use two pointers (`i` and `j`) to traverse the array.

   - For each element at index `i`, calculate the complement needed for the sum to be zero (`complement = -nums[i] - nums[j]`).

   - Check if the complement exists in the `hashMap` and if its index is greater than `j`.

   - If true, add the triplet `[nums[i], nums[j], complement]` to the result.

   - Move the pointer `j` to the next index of the same element to avoid duplicates.

   - Move the pointer `i` to the next index of the same element to avoid duplicate triplets.

### Time and Space Complexity
   - **Time complexity:** O(n^2) - The two-pointer approach takes O(n) per iteration, and we have O(n) iterations.
   - **Space complexity:** O(n) - The algorithm uses additional space for the HashMap.
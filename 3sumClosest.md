# 3 Sum Closest Problem

## Problem Description
Given an array of integers `nums` and an integer `target`, find three integers in `nums` such that the sum is closest to `target`. Return the sum of those three integers.

## Example
- **Input:** `nums = [-1, 2, 1, -4], target = 1`
  - **Output:** `2`
  - **Explanation:** The sum that is closest to the target is `(-1) + 2 + 1 = 2`.

## Two Pointer Solution
The Two Pointer approach is an efficient way to solve the 3 Sum Closest problem.

1. **Sort the array:** Arrange the input array in ascending order.

2. **Initialize closest sum:** Set a variable `closest` to the sum of the first three elements of the sorted array, as this represents the initial closest sum.

3. **Iterate through the array:** Use a loop to iterate through each element in the array.

4. **Use Two Pointers:** For each element at index `i`, use two pointers (`low` and `high`) to find a pair that sums to the target. Adjust the pointers based on the comparison of the sum with the target.

   - If the absolute difference between the current sum and the target is smaller than the absolute difference between the current closest sum and the target, update `closest` to the current sum.

   - If the sum is greater than the target, move the high pointer to the left.
   - If the sum is less than the target, move the low pointer to the right.

5. **Return closest sum:** After completing the iteration, return the `closest` sum.

### Time and Space Complexity
- **Time complexity:** O(n^2) - The two-pointer approach takes O(n) per iteration, and we have O(n) iterations.
- **Space complexity:** O(1) - The algorithm uses only a constant amount of space.

## Edge Cases
- If the length of the array is less than 3, handle appropriately.
- If the array contains only 3 elements, return their sum.

## Note
This solution leverages the sorted nature of the array to efficiently explore possible triplet combinations. The two-pointer approach helps avoid unnecessary iterations and improves the overall efficiency of finding the closest sum to the target.

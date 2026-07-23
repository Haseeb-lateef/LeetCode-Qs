
#  * Find the Duplicate Number
#  * 
#  * Given: array `nums` of n+1 integers, each in range [1, n]
#  * There is exactly one repeated value (others appear once)
#  * 
#  * Return: the repeated integer
#  * 
#  * Example: [1,2,3,2,2] -> 2
#  * Example: [1,2,3,4,4] -> 4
#  * 
#  * Constraints:
#  *   1 <= n <= 10,000
#  *   nums.length == n + 1
#  *   1 <= nums[i] <= n
#  * 
#  * Follow-up: solve without modifying nums, using O(1) extra space
#  * (Hint: Floyd's Cycle Detection / Tortoise and Hare)
 

# 287. Find the Duplicate Number

# Problem: Given an array of n+1 integers where each value is in [1, n], find the one duplicate value. There is exactly one repeated integer, and every other integer appears at most once.

# Follow-up: Solve it without modifying the array and using O(1) extra space.

# Approach 1: Hash Set (Brute Force)

# Walk through the array and track seen values in a set. The first value we've already seen is the duplicate.

# python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1

# Complexity:

# Time: O(n)
# Space: O(n) — doesn't satisfy the follow-up







# Approach 2: Floyd's Cycle Detection (Tortoise and Hare)BEST SOLUTION

# Treat the array as a linked list where each index i points to nums[i]. Since there are n+1 values but only n possible indices, at least two indices must point to the same value — this guarantees a cycle exists. The duplicate number is exactly the entry point of that cycle.

# Steps:

# Phase 1 — Detect the cycle: Move slow one step at a time (slow = nums[slow]) and fast two steps at a time (fast = nums[nums[fast]]) until they meet inside the cycle.
# Phase 2 — Find the cycle entrance: Reset slow to the start. Move both pointers one step at a time — the point where they meet again is the duplicate number.


# Complexity:

# Time: O(n)
# Space: O(1) ✅ satisfies the follow-up

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow2 = 0

        while True:
            slow2 = nums[slow2]
            slow = nums[slow]

            if slow == slow2:
                return slow


#EDGE CASES
# 1. n = 1 — smallest possible input

# python
# nums = [1, 1]

# Minimum valid array per constraints (n >= 1). Both indices point to the same value immediately, so the cycle is detected on the first iteration.


# 2. Duplicate value repeats more than twice

# python
# nums = [2, 2, 2, 2, 2]

# The problem guarantees "exactly one repeated integer" but not that it only repeats twice. The pointer logic handles any repeat count naturally since it's just following index → value links, not counting occurrences.
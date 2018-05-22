"""

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""

def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Let rob(n) be the maximum value that can be stolen given the houses nums[0:n].

        Base cases:
        rob(0) = nums[0] rob the first house.
        rob(1) = max(nums[0], nums[1]) either rob the first house or second house.

        Recursive relation:
        rob(n) = max(nums[n] + rob(n-2), rob(n-1)) for a house, we can either rob it or don't rob it, so nums[n] + rob(n-2) is robbing it, rob(n-1) is not          robbing it.
        """
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        rob = [0]*len(nums)
        rob[0] = nums[0]
        rob[1] = max(nums[0], nums[1])
        for i in xrange(2,len(nums)):
            rob[i] = max(nums[i] + rob[i-2], rob[i-1])

        return rob[-1]

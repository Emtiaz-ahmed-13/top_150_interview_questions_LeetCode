
#PROBLEM LINK: https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        for i in range(n-k):
            nums.append(nums.pop(0))
        
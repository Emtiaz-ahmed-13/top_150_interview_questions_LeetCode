#PROBELM_LINK: https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        index=0
        for i in range(len(nums)):
            if nums[i] !=val:
                nums[index]=nums[i]
                index+=1
        return index

# Time Complexity: O(n)
# Space Complexity: O(1)

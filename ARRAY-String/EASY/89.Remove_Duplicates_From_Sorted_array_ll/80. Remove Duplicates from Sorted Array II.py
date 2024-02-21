#PROBLEM LINK: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        index=1
        occurance=1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                occurance+=1
            else:
                occurance=1
            if occurance <=2:
                nums[index]=nums[i]
                index+=1

        return index
        
nums = [1, 1, 2]
j = 1

Iteration 1:
i = 1
nums[i] = 1, nums[i-1] = 1
Since nums[i] == nums[i-1], nothing happens.

Iteration 2:
i = 2
nums[i] = 2, nums[i-1] = 1
Since nums[i] != nums[i-1], nums[j] (which is nums[1]) is assigned nums[i] (which is 2).
nums = [1, 2, 2]
j += 1, so j is now 2.

Return j, which is 2.

Time Complexity (T.C.): The algorithm iterates through the entire array once, 
sothe time complexity is O(n), where n is the length of the input array nums.

Space Complexity (S.C.): The algorithm operates in-place, modifying the input array nums, so the space complexity is O(1), as it uses only a constant amount of extra space regardless of the size of the input.
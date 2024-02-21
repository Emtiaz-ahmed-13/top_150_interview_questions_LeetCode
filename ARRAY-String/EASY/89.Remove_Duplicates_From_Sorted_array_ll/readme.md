nums = [1, 1, 1, 2, 2, 3]
index = 1
occurrence = 1

Iteration 1:
i = 1
nums[i] == nums[i-1], so occurrence = 2

Iteration 2:
i = 2
nums[i] == nums[i-1], so occurrence = 3

Iteration 3:
i = 3
nums[i] != nums[i-1], so reset occurrence to 1
Since occurrence <= 2, nums[index] = nums[i] (which is 2), index += 1

Iteration 4:
i = 4
nums[i] != nums[i-1], so reset occurrence to 1
Since occurrence <= 2, nums[index] = nums[i] (which is 2), index += 1

Iteration 5:
i = 5
nums[i] != nums[i-1], so reset occurrence to 1
Since occurrence <= 2, nums[index] = nums[i] (which is 3), index += 1

Return index, which is 5.


nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
index = 1
occurrence = 1

...Skipping similar iterations...

Iteration 6:
i = 6
nums[i] != nums[i-1], so reset occurrence to 1
Since occurrence <= 2, nums[index] = nums[i] (which is 2), index += 1

Iteration 7:
i = 7
nums[i] != nums[i-1], so reset occurrence to 1
Since occurrence <= 2, nums[index] = nums[i] (which is 3), index += 1

Iteration 8:
i = 8
nums[i] != nums[i-1], so reset occurrence to 1
Since occurrence <= 2, nums[index] = nums[i] (which is 3), index += 1

Return index, which is 7.


Time Complexity (T.C.): The algorithm iterates through the entire array once, so the time complexity is O(n), where n is the length of the input array nums.

Space Complexity (S.C.): The algorithm operates in-place, modifying the input array nums, so the space complexity is O(1), as it uses only a constant amount of extra space regardless of the size of the input.

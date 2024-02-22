Initially, nums = [1, 2, 3, 4, 5, 6, 7] and k = 3.

Calculate n = len(nums) = 7 and k %= n = 3 % 7 = 3.
Iterate for i in range(n-k) which is for i in range(7-3), so i will iterate from 0 to 3.
In the first iteration:
nums.pop(0) removes the first element 1 and returns it.
Then nums.append(1) appends it to the end of the list.
Now nums = [2, 3, 4, 5, 6, 7, 1].
In the second iteration:
nums.pop(0) removes the first element 2 and returns it.
Then nums.append(2) appends it to the end of the list.
Now nums = [3, 4, 5, 6, 7, 1, 2].
In the third iteration:
nums.pop(0) removes the first element 3 and returns it.
Then nums.append(3) appends it to the end of the list.
Now nums = [4, 5, 6, 7, 1, 2, 3].
Output: [4, 5, 6, 7, 1, 2, 3]

So, after rotating nums 3 steps to the right, the resulting list is [4, 5, 6, 7, 1, 2, 3].
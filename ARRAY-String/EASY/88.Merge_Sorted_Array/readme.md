Input: nums1 = [1,2,3,0,0,0], 
        m = 3, 
        nums2 = [2,5,6], 
        n = 3
Initialize indices:
        i = m - 1 = 3 - 1 = 2
        j = n - 1 = 3 - 1 = 2
        k = m + n - 1 = 3 + 3 - 1 = 5
Start the while loop:
        Since j (the index for nums2) is not less than 0, we enter the loop.    
        We compare nums1[i] and nums2[j]:
        nums1[i] = nums1[2] = 3
        nums2[j] = nums2[2] = 6

Since nums1[i] > nums2[j], we place nums1[i] (3) at nums1[k] (index 5).
        nums1 = [1,2,3,0,0,3]
        Decrement k, i:
        k = 4, i = 1

Continue inside the loop:
        i (1) is still greater than or equal to 0.
        nums1[i] = nums1[1] = 2
        nums2[j] = nums2[2] = 6

Since nums1[i] > nums2[j], we place nums1[i] (2) at nums1[k] (index 4).
        nums1 = [1,2,3,0,2,3]
        Decrement k, i:
        k = 3, i = 0

Continue inside the loop:
        i (0) is still greater than or equal to 0.
        nums1[i] = nums1[0] = 1
        nums2[j] = nums2[2] = 6

Since nums1[i] < nums2[j], we place nums2[j] (6) at nums1[k] (index 3).
        nums1 = [1,2,3,6,2,3]
        Decrement k, j:
        k = 2, j = 1
Continue inside the loop:
        j (1) is still greater than or equal to 0.
        nums1[i] = nums1[0] = 1
        nums2[j] = nums2[1] = 5

Since nums1[i] > nums2[j], we place nums1[i] (1) at nums1[k] (index 2).
        nums1 = [1,2,5,6,2,3]
        Decrement k, j:
        k = 1, j = 0
Continue inside the loop:
        j (0) is still greater than or equal to 0.
        nums1[i] = nums1[0] = 1
        nums2[j] = nums2[0] = 2
Since nums1[i] > nums2[j], we place nums1[i] (1) at nums1[k] (index 1).

        nums1 = [1,2,2,5,6,3]
        Decrement k, j:
        k = 0, j = -1
We've exhausted nums2. The loop terminates.

Final Result: nums1 = [1,2,2,3,5,6]
def nextPermutation(nums):
    """
    Rearranges nums into the lexicographically next greater permutation.
    If not possible, rearranges to the lowest possible order (ascending).
    Modifies nums in-place and uses O(1) extra memory.
    """
    n = len(nums)
    if n <= 1:
        return

    # 1) Find the first decreasing element from the right: nums[i] < nums[i+1]
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        # 2) Find rightmost element greater than nums[i]
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        # 3) Swap
        nums[i], nums[j] = nums[j], nums[i]

    # 4) Reverse the suffix starting at i+1 to get the smallest order
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

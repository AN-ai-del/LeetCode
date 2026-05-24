class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:                        # Edge case: empty array
            return 0

        pos = 1                             # Write pointer (start from index 1)

        for i in range(1, len(nums)):       # Start scanning from index 1
            if nums[i] != nums[i - 1]:      # Current ≠ previous → unique!
                nums[pos] = nums[i]         # Write it to pos
                pos += 1                    # Advance write pointer

        return pos                          # k = number of unique elements
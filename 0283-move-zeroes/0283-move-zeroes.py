class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        left = 0                            # Points to current zero position

        for right in range(len(nums)):
            if nums[right] != 0:            # Found a non-zero element
                nums[left], nums[right] = nums[right], nums[left]  # Swap
                left += 1                   # Move left pointer forward
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        left = 0                            # Start of array
        right = len(nums) - 1              # End of array

        while left <= right:
            if nums[left] == val:           # Found val at left
                nums[left] = nums[right]    # Replace with rightmost element
                right -= 1                  # Shrink array from right
            else:
                left += 1                   # Valid element, move left forward

        return left                         # k = left pointer position
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        count = [0, 0, 0]               # count[0]=reds, count[1]=whites, count[2]=blues

        for num in nums:                # Pass 1: count each color
            count[num] += 1

        pos = 0
        for color in range(3):          # Pass 2: overwrite array
            for _ in range(count[color]):
                nums[pos] = color
                pos += 1
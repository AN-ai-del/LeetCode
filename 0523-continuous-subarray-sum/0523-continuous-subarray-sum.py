class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        # remainder -> first index
        remainder_map = {0: -1}

        prefix_sum = 0

        for i in range(len(nums)):

            prefix_sum += nums[i]

            remainder = prefix_sum % k

            # If same remainder seen before
            if remainder in remainder_map:

                prev_index = remainder_map[remainder]

                # Length at least 2
                if i - prev_index >= 2:
                    return True

            else:
                # Store first occurrence only
                remainder_map[remainder] = i

        return False
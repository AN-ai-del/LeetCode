class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_count = {0: 1}

        current_sum = 0

        count = 0

        for num in nums:

            current_sum += num

            # Needed prefix sum
            needed = current_sum - k

            # If exists, add frequency
            if needed in prefix_count:
                count += prefix_count[needed]

            # Store current prefix sum
            if current_sum in prefix_count:
                prefix_count[current_sum] += 1
            else:
                prefix_count[current_sum] = 1

        return count
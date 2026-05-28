from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):

        # Step 1: Frequency count
        count = Counter(nums)

        # Step 2: Create buckets
        freq = [[] for _ in range(len(nums) + 1)]

        for num, c in count.items():
            freq[c].append(num)

        # Step 3: Gather top k frequent elements
        result = []

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)

                if len(result) == k:
                    return result
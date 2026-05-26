from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_map = defaultdict(list)         # key → list of anagrams

        for word in strs:
            key = ''.join(sorted(word))         # Sort chars → canonical form
            anagram_map[key].append(word)        # Group by key

        return list(anagram_map.values())        # Return all groups
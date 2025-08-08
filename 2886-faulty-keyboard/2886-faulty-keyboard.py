class Solution:
    def finalString(self, s: str) -> str:
        ans = ""
        for char in s:
            # ans += char
            if char != 'i':
                ans += char
            elif char == 'i':
                ans = ans[::-1]

        return ans   
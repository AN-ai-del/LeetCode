class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        result = ""
        for i in range (len(number)):
            if number[i]==digit:
                tn = number[:i]+ number[i+1:]
                if not result or tn>result:
                    result = tn
        return result
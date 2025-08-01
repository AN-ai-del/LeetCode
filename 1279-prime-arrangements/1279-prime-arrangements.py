class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7

        def is_prime(x):
            if x < 2:
                return False
            for i in range(2, int(x**0.5) + 1):
                if x % i == 0:
                    return False
            return True

        def factorial(x):
            result = 1
            for i in range(1, x + 1):
                result = (result * i) % MOD
            return result

        prime_count = sum(is_prime(i) for i in range(1, n + 1))
        return (factorial(prime_count) * factorial(n - prime_count)) % MOD

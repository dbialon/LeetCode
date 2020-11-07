class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        l = len(b)
        n = 0
        for i in range(l):
            n += b[i]*10**(l-i-1)
        return self.power(a, n) % 1337


    def power(self, x: int, n: int) -> int:
        x %= 1337
        if n == 1:
            return x
        elif n % 2 == 1:
            return x * self.power(x*x, n//2)
        else:
            return self.power(x*x, n//2)

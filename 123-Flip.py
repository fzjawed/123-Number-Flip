class Solution:
    def solve(self, n):
        x = list(str(n))
        for i in range(len(x)):
            if x[i] != '3':
                x[i] = '3'
                break
        result = int("".join(x))
        return result
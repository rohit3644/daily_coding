class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sub = {"I": ["V", "X"], "X": ["L", "C"], "C": ["D", "M"]}
        op = []
        last = None
        for i in s:
            if last in sub and i in sub[last]:
                op[-1] = -1 * op[-1]
            op.append(d[i])
            last = i
        res = 0
        for num in op:
            res += num
        return res

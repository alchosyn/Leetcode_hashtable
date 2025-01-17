class Solution:
    def romanToInt(self, s: str) -> int:
        RomanInt = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        ans = RomanInt[s[len(s)-1]]
        for index in range(len(s)-1):
            if(RomanInt[s[index]]>=RomanInt[s[index+1]]):
                ans += RomanInt[s[index]]
            else:
                ans -= RomanInt[s[index]]

        return ans

s="MCMXCIV"
a = Solution()
print(a.romanToInt(s))
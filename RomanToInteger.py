class Solution(object):
    def romanToInt(self, s):
        roman_list = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        n = len(s)
        for i in range(n):
            value = roman_list[s[i]]
            if i < n - 1 and value < roman_list[s[i+1]]:
                total -= value
            else:
                total += value

        return total


    

solution = Solution()
print(solution.romanToInt("III"))
print(solution.romanToInt("LVIII"))
print(solution.romanToInt("MCMXCIV"))

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        int_val = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i+1]]:
                int_val += roman_to_int[s[i+1]]-roman_to_int[s[i]]
                i += 2
            else:
                int_val += roman_to_int[s[i]]
                i += 1
        return int_val


if __name__ == "__main__":
    # s = "MCMXCIV"
    s = "III"
    obj = Solution()
    print(obj.romanToInt(s))
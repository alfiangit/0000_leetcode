# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        output = int()
        roman_numerals_combination = {
            "CM": 900,
            "CD": 400,
            "XC": 90,
            "XL": 40,
            "IX": 9,
            "IV": 4,
        }

        roman_numerals = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,
        }

        for key, value in roman_numerals_combination.items() : 
            if key in s : 
                s = s.replace(key, "")
                output += value

        for a in s :
            if a in roman_numerals : 
                output += roman_numerals[a]
            
        return output

# God Damn AI
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        total = 0
        n = len(s)

        for i in range(n):
            val = roman[s[i]]
            if i + 1 < n and val < roman[s[i + 1]]:
                total -= val
            else:
                total += val

        return total

# i | Char |  val | Next (val) | i + 1 < 7 and val < next | Action | Total
# ---+------+------+------------+--------------------------+--------+------
#  0 |  M   | 1000 |  C (100)   | False (1000 < 100)       | +1000  |  1000
#  1 |  C   |  100 |  M (1000)  | True  (100 < 1000)       | -100   |   900
#  2 |  M   | 1000 |  X (10)    | False (1000 < 10)        | +1000  |  1900
#  3 |  X   |   10 |  C (100)   | True  (10 < 100)         | -10    |  1890
#  4 |  C   |  100 |  I (1)     | False (100 < 1)          | +100   |  1990
#  5 |  I   |    1 |  V (5)     | True  (1 < 5)            | -1     |  1989
#  6 |  V   |    5 |  None      | False (end of string)    | +5     |  1994
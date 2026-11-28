# https://leetcode.com/problems/longest-common-prefix/description/
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # it's prefix : a letter or group of letters added to the beginning of a word
        if len(strs) == 1 :
            return strs[0]
        else : 
            number_strs = [len(x) for x in strs]
            n_max_words = max(number_strs)

            for i in range(n_max_words, 0, -1) : 

                prefix = strs[0][:i]

                counter = 0
                for word in strs :
                    if word.startswith(prefix) : 
                        counter += 1

                if counter == len(strs) :
                    return prefix
                
            return ""

# AI Solution
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        for i, ch in enumerate(strs[0]):
            for word in strs[1:]:
                if i >= len(word) or word[i] != ch:
                    return strs[0][:i]

        return strs[0]

# === 1. SAMPLE INPUTS & OUTPUTS ===

# #  | Input `strs`                                          | Output     | Reason
# ---+-------------------------------------------------------+------------+-----------------------------------------------------------------------------
# 1  | ["flower", "flow", "flight"]                          | "fl"       | i=0 ('f') and i=1 ('l') match all; i=2 mismatches ('o' vs 'i') -> "fl"
# 2  | ["dog", "racecar", "car"]                             | ""         | i=0 ('d') mismatches "racecar" ('r') immediately -> ""
# 3  | ["interspecies", "interstellar", "interstate"]        | "inters"   | Matches i=0..5 ("inters"); i=6 differs ('p' vs 't' vs 'a') -> "inters"
# 4  | ["ab", "a"]                                           | "a"        | i=0 ('a') matches; at i=1, 1 >= len("a") triggers early exit -> "a"
# 5  | ["prefix", "pre", "prevent"]                          | "pre"      | Matches i=0..2 ("pre"); at i=3, 3 >= len("pre") stops -> "pre"
# 6  | ["single"]                                            | "single"   | strs[1:] is empty; loop finishes without mismatch -> "single"
# 7  | ["", "abc"]                                           | ""         | strs[0] is "", so enumerate("") runs 0 times -> ""
# 8  | []                                                    | ""         | Caught by `if not strs: return ""` guard -> ""
# https://leetcode.com/problems/two-sum/

# First Solution
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        combinations = set()
        for i in range(len(nums)) : 
            for v in range((i + 1), len(nums)) :
                combination = tuple(sorted([i, v]))
                if combination in combinations : 
                    continue
                if nums[i] + nums[v] == target :
                    combinations.add(combination)
                    return list(combination)


# Second Solution : Asking Ai
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i, num in enumerate(nums) : 
            complimentary = target - num

            if complimentary in seen : 
                return [seen[complimentary], i]
            
            seen[num] = i
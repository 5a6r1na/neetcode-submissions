class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)
        longest = 0
        curr = 0

        for num in nums:
            if (num-1) not in num_set:
                curr = num
                streak = 1
                while curr + 1 in num_set:
                    streak += 1
                    curr += 1
                longest = max(streak, longest)

        return longest
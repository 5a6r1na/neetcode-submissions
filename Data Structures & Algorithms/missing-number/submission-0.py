class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        length = len(nums)
        expected = 0
        actual = 0

        for i in range(length+1):
            expected += i

        for num in nums:
            actual += num

        if actual == expected:
            return 0
        
        result = expected - actual

        return result
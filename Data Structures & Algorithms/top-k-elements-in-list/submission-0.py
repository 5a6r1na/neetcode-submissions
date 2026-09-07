class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # construct freq map
        # create bucket to store count


        count = {}
        buckets = [ [] for _ in range(len(nums)+1)]
        result = []

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        for n, freq in count.items():
            buckets[freq].append(n)

        for i in range(len(buckets)-1, 0, -1):
            for n in buckets[i]:
                result.append(n)
                if len(result) == k:
                    return result


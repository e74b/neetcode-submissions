class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = []
        for _ in range((len(nums) + 1)):
            buckets.append([])
        
        maxFrequency = len(nums)

        freqMap = {}

        for num in nums:
            if num not in freqMap:
                freqMap[num] = 0
            freqMap[num] += 1

        for element, count in freqMap.items():
            buckets[count].append(element)

        results = []
        for bucket in buckets:
            if bucket == []:
                continue

            results.extend(bucket)

        return results[-k:]
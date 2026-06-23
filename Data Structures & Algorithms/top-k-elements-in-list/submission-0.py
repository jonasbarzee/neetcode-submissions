class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       # use bucket sort, put the number in the bucket corresponding to its frequency or count

        counts = Counter(nums)
        buckets = [[] for i in range(len(nums) + 1)] 
        print(counts)
        print(buckets)

        for key, value in counts.items():
            buckets[value].append(key)

        result = [] 
        for i in range(len(buckets) - 1, 0, -1):
            for value in buckets[i]:
                result.append(value)
                if len(result) == k:
                    return result
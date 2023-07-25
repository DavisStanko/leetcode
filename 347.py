# Given an integer array nums and an integer k, return the k most frequent elements.

def topKFrequent(nums, k):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [freq[i][0] for i in range(k)]
from ast import List

def topKFrequent(nums, k) :

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for c in nums:
            count[c] = 1 + count.get(c,0)
            print(count)

        for c, n in count.items():
            freq[n].append(c)
            print(freq[n])

        res =[]
        for i in range(len(freq)-1 , 0, -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k :
                return res
            
nums = [1,1,1,2,2,3]
k=2
print(topKFrequent(nums,k))
        
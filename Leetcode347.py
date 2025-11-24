class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # 1. 직접 빈도수 세기
        freq = {}
        for x in nums:
            if x in freq:
                freq[x] += 1
            else:
                freq[x] = 1

        # 2. bucket 만들기 (인덱스 = 빈도수)
        bucket = [[] for _ in range(len(nums) + 1)]

        # 3. 빈도수에 맞춰 bucket에 넣기
        for num, count in freq.items():
            bucket[count].append(num)

        # 4. 뒤에서부터 k개 추출
        result = []
        for count in range(len(bucket) - 1, 0, -1):
            for num in bucket[count]:
                result.append(num)
                if len(result) == k:
                    return result
class Solution:
    def reorganizeString(self, s: str) -> str:
        str_len = len(s)
        hash_map = {}

        for char in s:
            hash_map[char] = hash_map.get(char, 0) + 1
            if hash_map[char] > (len(s) + 1) // 2:
                return ""
           
        max_heap = [[-cnt, char] for char, cnt in hash_map.items()]
        heapq.heapify(max_heap)

        res = ""
        prev = None
        while max_heap or prev:
            if prev and not max_heap:
                return ""
            cnt, char = heapq.heappop(max_heap)

            res += char
            cnt += 1
            
            if prev:
                heapq.heappush(max_heap, prev)
                prev = None
            if cnt !=0:
                prev = [cnt, char] 
        return res
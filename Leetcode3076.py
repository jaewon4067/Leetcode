class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        n = len(arr)
        answer : List(str)= []

        for i, string in enumerate(arr):
            m = len(string)
            # i = index
            for L in range(1, m+1): # L is the length for checking
                for start in range(m-L+1):
                    sub = string[start:start+L]
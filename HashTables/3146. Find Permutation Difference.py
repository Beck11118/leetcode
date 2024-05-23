class Solution:  
    # this brute force solution has the time complexity O(n**2)  
    # def findPermutationDifference(self, s: str, t: str) -> int:
    #     permutation_difference = 0
    #     for i, letter1 in enumerate(s):
    #         for j, letter2 in enumerate(t):
    #             if letter1 == letter2:
    #                 permutation_difference += abs(i - j)
        
    #     return permutation_difference
    
    # Using Index map to save indecies of characters have instant look up O(1)
    def findPermutationDifference(self, s:str, t:str) -> int:
        idx_map = {char:idx for idx, char in enumerate(t)}

        #Calculation permutation difference
        return sum(abs(i - idx_map[char]) for i, char in enumerate(s))

test1 = Solution()
test1.findPermutationDifference("abc", "bas")
print(test1.findPermutationDifference("abc", "bas"))



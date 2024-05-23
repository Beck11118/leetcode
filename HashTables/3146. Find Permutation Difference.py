class Solution:  
    # this brute force solution has the time complexity O(n**2)  
    def findPermutationDifference_original(self, s: str, t: str) -> int:
        permutation_difference = 0
        for i, letter1 in enumerate(s):
            for j, letter2 in enumerate(t):
                if letter1 == letter2:
                    permutation_difference += abs(i - j)
        
        return permutation_difference
    
    # Using Index map to save indecies of characters have instant look up O(1)
    def findPermutationDifference_optimized(self, s:str, t:str) -> int:
        idx_map = {char:idx for idx, char in enumerate(t)}

        #Calculation permutation difference
        return sum(abs(i - idx_map[char]) for i, char in enumerate(s))

#Adding Testing to find time difference
import timeit
def test_findPermutationDifference():
    sol = Solution()

    # Test cases
    test_cases = [
        ("abc", "bac"),
        ("abcde", "edbac"),
        ("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba")
    ]

    for s, t in test_cases:
        # Timing the original solution
        original_time = timeit.timeit(lambda: sol.findPermutationDifference_original(s, t), number=1000)
        # Timing the optimized solution
        optimized_time = timeit.timeit(lambda: sol.findPermutationDifference_optimized(s, t), number=1000)

        print(f"Test case s='{s}' t='{t}'")
        print(f"Original time: {original_time:.6f} seconds")
        print(f"Optimized time: {optimized_time:.6f} seconds")
        print()

test_findPermutationDifference()
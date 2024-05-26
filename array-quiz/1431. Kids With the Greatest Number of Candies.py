from typing import List
class Solution:
    def kidsWithCandies_original(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = [False]*len(candies)
        for idx in range(len(candies)):
            if candies[idx] + extraCandies > max_candies:
                result[idx] = True
            else:
                result[idx] = False
        return result   

    def kidsWithCandies_optimized(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        return[candy + extraCandies >= max_candies for candy in candies] 

import timeit
def test_kidsWithCandies():
    sol = Solution()
    test_case = [
        ([2,3,5,1,3], 3),
        ([4,2,1,1,2], 1),
        ([12, 1, 12], 10)
    ]

    for candies, extra_candies in test_case:
        test_original = timeit.timeit(lambda: sol.kidsWithCandies_original(candies, extra_candies), number=1000)
        test_optimized = timeit.timeit(lambda: sol.kidsWithCandies_optimized(candies, extra_candies), number=1000)
        print(f"test_original: {test_original:.6f}")
        print(f"test_optimized: {test_optimized:.6f}")

test_kidsWithCandies()
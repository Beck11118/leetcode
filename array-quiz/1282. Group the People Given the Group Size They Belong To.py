from typing import List
class Solution:
    def groupThePeople_original(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        result = []
        for person, group in enumerate(groupSizes):
            if group in groups:
                groups[group].append(person)
            else:
                groups[group] = [person]
        
        for key in groups:
            if key == len(groups[key]):
                result.append(groups[key])
            else:
                left = 0
                right = key
                while left < len(groups[key]):
                    result.append(groups[key][left:right])
                    left += key
                    right += key 
        return result
    
    def groupThePeople_optimized(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        result = []
        for person, group in enumerate(groupSizes):
            if group in groups:
                groups[group].append(person)
            else:
                groups[group] = [person]
        
            if len(groups[group]) == group:
                result.append(groups[group])
                groups[group] = []
        return result

import timeit
def test():
    sol = Solution()
    test_case = (
        [3,3,3,3,3,1,3],
        [2,1,3,3,3,2]
    )
    for groupSizes in test_case:
        test_original = timeit.timeit(lambda: sol.groupThePeople_original(groupSizes), number = 1000) 
        test_optimized = timeit.timeit(lambda: sol.groupThePeople_original(groupSizes), number = 1000)
        print(f'test original: {test_original:.6f}')
        print(f'test optimized: {test_optimized:.6f}')

test()
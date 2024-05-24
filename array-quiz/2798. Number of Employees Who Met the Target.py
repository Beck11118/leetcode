from typing import List
class Solution:
    def numberOfEmployeesWhoMetTarget_original(self, hours: List[int], target: int) -> int:
        employees = 0
        for employee_hours in hours:
            if employee_hours >= target:
                employees +=1
        return employees
    
    def numberOfEmployeesWhoMetTarget_optimized(self, hours: List[int], target: int) -> int:
        return sum(employee_hours >= target for employee_hours in hours)
    
import timeit
def test_numberOfEmpoyeesWhoMetTarget():
    sol = Solution()

    test_case = [
        ([0, 1, 2, 3, 4], 2),
        ([8, 9, 10, 11, 12], 10), 
        ([5, 3, 8, 2, 1, 4, 9, 7, 6, 10, 3, 2, 5, 8, 1, 4, 7, 9, 2, 6, 3, 8, 10, 4, 7, 9, 1, 5, 3, 6, 8, 2, 4, 7, 9, 1, 3, 6, 10, 8, 5, 2, 4, 9, 1, 7, 3, 6, 8, 10, 5, 2], 5),
        ([7, 5, 2, 8, 9, 3, 6, 1, 4, 10, 7, 5, 2, 8, 9, 3, 6, 1, 4, 10, 7, 5, 2, 8, 9, 3, 6, 1, 4, 10, 7, 5, 2, 8, 9, 3, 6, 1, 4, 10, 7, 5, 2, 8, 9, 3, 6, 1, 4, 10, 7, 5, 2, 8, 9, 3, 6, 1, 4, 10, 7, 5, 2, 8, 9, 3, 6, 1, 4, 10, 7, 5, 2, 8, 9, 3, 6, 1, 4, 10, 7, 5, 2, 8, 9, 3, 6, 1, 4, 10, 7, 5, 2, 8, 9, 3, 6, 1, 4, 10, 7, 5, 2, 8, 9, 3, 6, 1, 4, 10, 7, 5, 2, 8, 9, 3, 6, 1, 4, 10, 7, 5, 2, 8, 9, 3, 6, 1, 4, 10, 7, 5, 2, 8, 9, 3, 6, 1, 4, 10], 7)
    ]

    for h, t in test_case:
        original_time = timeit.timeit(lambda: sol.numberOfEmployeesWhoMetTarget_original(h, t), number=1000)
        optimized_time = timeit.timeit(lambda: sol.numberOfEmployeesWhoMetTarget_optimized(h, t), number = 1000)

        print(f'Test case hours="{h}" t="{t}"')
        print(f"Original time: {original_time:.6f} seconds")
        print(f"Optimized time: {optimized_time:.6f} seconds")

test_numberOfEmpoyeesWhoMetTarget()
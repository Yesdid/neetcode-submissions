class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        solution_list = []
        for i in range(len(nums)):
            needed = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == needed:
                    solution_list.append(i)
                    solution_list.append(j)
        return solution_list
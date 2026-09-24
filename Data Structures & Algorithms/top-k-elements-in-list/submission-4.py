class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = defaultdict(int)
        count_list = list()
        result_list = list()
        for num in nums:
            count_dict[num] += 1

        for key in count_dict:
            count_list.append([count_dict[key], key])
        sorted_count_list = sorted(count_list, key = lambda x: x[0])
        sorted_count_list = sorted_count_list[::-1]

        for i in range(k):
            result_list.append(sorted_count_list[i][1])

        return result_list
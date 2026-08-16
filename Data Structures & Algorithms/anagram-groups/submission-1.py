class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            anagram_dict[sorted_word].append(word)
        
        anagram_list = []
        for key in anagram_dict:
            anagram_list.append(anagram_dict[key])

        return anagram_list
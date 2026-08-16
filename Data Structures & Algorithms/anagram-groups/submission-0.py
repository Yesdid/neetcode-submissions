class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord("a")] += 1
            
            anagram_dict[tuple(count)].append(word)

        
        anagram_list = []
        for key in anagram_dict:
            anagram_list.append(anagram_dict[key])
        
        return anagram_list
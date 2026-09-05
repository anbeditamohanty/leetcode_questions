class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        list1 = list(word1)
        list2 = list(word2)
        merged_list = []
        for i in range(max(len(list1), len(list2))):
            if i < len(list1):
                merged_list.append(list1[i])
            if i < len(list2):
                merged_list.append(list2[i])
        return "".join(merged_list)

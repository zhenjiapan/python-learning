class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = ''

        for i, chat in enumerate(strs[0]):
            for ele in strs[1:]:
                if i > len(ele)-1 or ele[i] != chat:
                   return result
            result += chat

        return result
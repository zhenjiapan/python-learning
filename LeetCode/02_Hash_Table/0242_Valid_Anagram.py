class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
        for char in t:
            if char in t_dict:
                t_dict[char] += 1
            else:
                t_dict[char] = 1
        for key in s_dict:
            if (key not in t_dict) or s_dict[key] != t_dict[key]:
                return False
        for key in t_dict:
            if (key not in s_dict) or t_dict[key] != s_dict[key]:
                return False
        return True
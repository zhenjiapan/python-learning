class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {')': '(', ']': '[', '}': '{'}
        had_read = []

        for char in s:
            if had_read == [] and char in ')]}':
                return False

            if char in '([{':
                had_read.append(char)

            elif char in ')]}':
                if parentheses[char] != had_read[-1]:
                    return False
                else:
                    had_read.pop(-1)

        if had_read != []:
            return False

        return True

        # if len(s)%2 != 0:
        #     return False
        #
        # elif parentheses[s[0]] + 1 == parentheses[s[1]]:
        #     for i in range(int(len(s)/2)):
        #         if parentheses[s[2*i]] + 1 != parentheses[s[2*i+1]]:
        #             return False
        #
        # elif parentheses[s[0]] + 1 == parentheses[s[-1]]:
        #     for i in range(int(len(s)/2)):
        #         if parentheses[s[i]] + 1 != parentheses[s[-i-1]]:
        #             return False
        #
        # else:
        #     return False
        #
        # return True

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # x_list = list(str(x))
        # x_list_rev = list(reversed(x_list))
        # return x_list == x_list_rev
        q = str(int)
        return q == q[::-1]
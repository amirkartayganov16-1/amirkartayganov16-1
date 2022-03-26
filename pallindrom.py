class Solution:

    @staticmethod

    def palindrome_conv(x):

        x = str(x)
        x_len = len(x)
        i = 0
        j = x_len - 1
        while i <= j:
            char_l = x[i]
            char_r = x[j]
            if char_r != char_l:
                return False
            else:
                i += 1
                j -= 1
        return True

    @staticmethod
    def palindrome(x):

        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        x_rev = 0
        while x_rev < x:
            x_rev = x_rev * 10 + x % 10
            x = x // 10
            if x_rev == x:
                return True
        if x_rev == x or x_rev // 10 == x:
            return True
        return False


if __name__ == '__main__':
    print(Solution.palindrome_conv(121))
    print(Solution.palindrome_conv(1211))
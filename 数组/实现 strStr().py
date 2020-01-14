'''
实现 strStr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
'''


class Solution:
    def strStr(self, haystack, needle):
        rst = haystack.find(needle)
        return rst


if __name__ == '__main__':
    s = Solution()
    haystack = "hello"
    needle = "ll"
    print(s.strStr(haystack=haystack, needle=needle))

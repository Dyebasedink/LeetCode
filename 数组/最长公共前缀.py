'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
'''


class Solution:
    def longestCommonPrefix(self, strs):
        rst = ""
        if strs.__len__() == 0: return rst
        if strs.__len__() == 1: return strs[0]
        for char in strs[0]:
            for i in strs:
                if not i.startswith(rst + char): return rst
            rst += char
        return rst


if __name__ == '__main__':
    s = Solution()
    strs = ["flower", "flow", "flight"]
    print(s.longestCommonPrefix(strs))

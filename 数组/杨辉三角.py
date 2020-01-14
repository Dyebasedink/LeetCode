'''
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
'''


class Solution:
    def generate(self, numRows):
        if numRows == 0: return []
        list = [[1]]
        for row in range(1, numRows):
            line = []
            for i in range(row + 1):
                if i == 0:
                    line.append(1)
                elif i == row:
                    line.append(1)
                else:
                    line.append(list[row - 1][i - 1] + list[row - 1][i])
            list.append(line)
        return list


if __name__ == '__main__':
    s = Solution()
    print(s.generate(5))

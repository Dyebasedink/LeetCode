'''
题目：给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素。
思路：分析一下遍历顺序的特点，可以看出，对角线的方向跟索引和（行的索引值+列的索引值）的奇偶性有关，然后加上边界情况，遍历的路线大概就出来了。
具体可以分为以下几种情况：

    索引和为偶数：
        元素在第一行，往右走
        元素在最后一列，往下走
        其他情况，往右上走
    索引和为奇数：
        元素在第一列，往下走
        元素在最后一行，往右走
        其他情况，往左下走

'''


class Solution:
    def findDiagonalOrder(self, matrix):
        row = len(matrix)
        if row == 0: return []
        line = len(matrix[0])
        rst = []
        r = 0
        c = 0
        for _ in range(row * line):
            rst.append(matrix[r][c])
            if (r + c) % 2 == 0:  # 索引和为偶数
                if c == line - 1:  # 最后一列往下走
                    r += 1
                elif r == 0:  # 第一行往右走
                    c += 1
                else:  # 其他情况往右上走
                    r -= 1
                    c += 1
            else:  # 索引和为奇数
                if r == row - 1:  # 最后一行往右走
                    c += 1
                elif c == 0:  # 第一列往下走
                    r += 1
                else:  # 其他情况左下走
                    r += 1
                    c -= 1
        return rst


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s = Solution()
    print(s.findDiagonalOrder(matrix))

'''
给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
'''


def getRow(rowIndex):
    nk = 1
    res = []
    for i in range(rowIndex+1):
        res.append(int(nk))
        nk = nk * (rowIndex - i) / (i + 1)
    return res


print(getRow(4))

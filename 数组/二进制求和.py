class Solution:
    def addBinary(self, a, b):
        a = int(a,2)
        b = int(b,2)
        rst = bin(a+b)
        return rst

if __name__ == '__main__':
    a="1010"
    b="1100"
    s = Solution()
    print(s.addBinary(a,b))

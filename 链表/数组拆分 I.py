'''
给定长度为 2n 的数组, 你的任务是将这些数分成 n 对, 例如 (a1, b1), (a2, b2), ..., (an, bn) ，
使得从1 到 n 的 min(ai, bi) 总和最大。
'''

class Solution:
    def arrayPairSum(self, nums):
        nums.sort()
        rst = [nums[i] for i in range(len(nums)) if i%2 == 0]
        nums_sum = sum(rst)
        return nums_sum

if __name__ == '__main__':
    s = Solution()
    nums=[1,4,3,2]
    print(s.arrayPairSum(nums=nums))
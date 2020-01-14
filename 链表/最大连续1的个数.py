'''给定一个二进制数组， 计算其中最大连续1的个数。'''


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_count_1 = temp_length = 0
        for v in nums:
            if v:
                temp_length += 1
            else:
                max_count_1 = max(max_count_1, temp_length)
                temp_length = 0
        return max(max_count_1, temp_length)

if __name__ == '__main__':
    s = Solution()
    nums = [1,1,1,1,0,1,1,1,1]
    print(nums.__len__())
    print(s.findMaxConsecutiveOnes(nums=nums))

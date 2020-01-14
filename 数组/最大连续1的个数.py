'''给定一个二进制数组， 计算其中最大连续1的个数。'''

class Solution:
    def findMaxConsecutiveOnes(self, nums) :
        max_number = 0
        number = 0
        for n in range(1, len(nums)):
            if nums[n] == nums[n-1] == 1:
                number += 1
            else:
                if number>max_number:
                    max_number = number
                number = 0
        return (max_number+1)
#todo 快指针每次向后遍历，如果不等于1，则用快指针减慢指针得到长度，然后将快指针赋值给满指针，快指针继续遍历


if __name__ == '__main__':
    s = Solution()
    nums = [1,0,1,1,0,1]
    print(s.findMaxConsecutiveOnes(nums=nums))
'''
给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
'''

class Solution:
    def removeElement(self, nums, val):
        if len(nums) == 0:return 0
        length = 0    #慢指针
        for num in nums:
            if num != val:
                nums[length] = num    #如果num不等于val，则将num的值赋给慢指针指向的位置
                length += 1           #慢指针向后移动一位，最后的数组只包含不为val的元素且长度为length，
        return length


if __name__ == '__main__':
    s = Solution()
    nums = [3,2,2,3]
    val = 3
    print(s.removeElement(nums=nums, val=val))
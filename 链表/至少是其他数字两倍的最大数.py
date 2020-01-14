'''
在一个给定的数组nums中，总是存在一个最大元素 。

查找数组中的最大元素是否至少是数组中每个其他数字的两倍。

如果是，则返回最大元素的索引，否则返回-1。
'''

def dominantIndex(nums):
    if len(nums) == 1:
        return 0
    max_number_index = nums.index(max(nums))       #获取最大值索引
    max_number = nums.pop(max_number_index)         #弹出最大值
    second_number = max(nums)             #获取第二大值
    if max_number/2 >= second_number:     #判断条件
        return max_number_index
    return -1


nums=[3, 6, 1, 0]
print(dominantIndex(nums))
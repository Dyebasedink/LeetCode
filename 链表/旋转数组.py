'''
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
'''

def rotate(nums, k):
    k %= len(nums)
    nums[:] = nums[::-1]
    nums[:k] = nums[:k][::-1]
    nums[k:] = nums[k:][::-1]


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums,k)
'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
'''

def moveZeroes(nums):
    left = 0

    for n in range(len(nums)):
        if not nums[n]:
            nums.pop(n)
            nums.append(0)
        else:
            left+= 1
    return nums
nums = [0,0,1]
print(moveZeroes(nums))
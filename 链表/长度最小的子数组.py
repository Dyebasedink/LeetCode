'''给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。
如果不存在符合条件的连续子数组，返回 0。'''
import builtins
def minSubArrayLen(s, nums):
    if sum(nums) == s:
        return len(nums)
    if sum(nums) < s:
        return 0
    temp_sum = begin = 0
    min_len = len(nums)
    for end in range(len(nums)):
        temp_sum += nums[end]
        while temp_sum >= s:
            min_len = min(min_len, end-begin+1)
            temp_sum -= nums[begin]
            begin += 1
    return min_len



s = 7
nums = [2,3,1,2,4,3]
print(minSubArrayLen(s, nums))
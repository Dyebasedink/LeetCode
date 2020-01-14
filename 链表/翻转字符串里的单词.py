'''
给定一个字符串，逐个翻转字符串中的每个单词。
'''

#new
def reverseWords(s):
    s_list = s.split(' ')
    s_list = s_list[::-1]
    return "".join(s_list)


s = "a good   example"

print(reverseWords(s))

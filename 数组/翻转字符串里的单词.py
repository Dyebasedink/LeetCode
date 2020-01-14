'''
给定一个字符串，逐个翻转字符串中的每个单词。
'''


def reverseWords(s):
    '''
   s = s.split(' ')
    ans = ''
    for i in range(len(s)-1,-1,-1):
        if s[i]:
            ans = ans + s[i] +
             ' '
    return ans.rstrip()
    '''
    return " ".join(s.split()[::-1])



s = "a good   example"
print(reverseWords(s))
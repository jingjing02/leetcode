# coding:utf-8

"""
创造了一个额外的同长度数组，不符合要求
顺便list格式的入参s[::-1]是目前广泛认同的
def reverse_string(s: str):
    s_reverse = ''
    for i in s:
        s_reverse = i + s_reverse
        return s_reverse
"""


def reverseString(s) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    start = 0
    end = len(s) - 1

    while end > start:
        s[start], s[end] = s[end], s[start]  # 学习了
        start += 1
        end -= 1

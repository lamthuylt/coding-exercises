"""
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. 
"""


def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    # if needle is an empty string, return 0
    if needle=='':
        return 0
    else:
        for i,char0 in enumerate(haystack):
            # if the first character of needle is found
            if char0==needle[0]:
                # check if the following characters match needle
                if len(haystack)-i >= len(needle):
                    check = True
                    for j,char in enumerate(needle[1:]):
                        if haystack[i+j+1] != char:
                            check = False
                    if check==True:
                        return i
    return -1
                            
                        
                        
                    
if __name__ == '__main__':
    print(strStr("hello", "ll"))
    print(strStr("aaaaa", "bba"))
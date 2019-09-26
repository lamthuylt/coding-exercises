"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

MIN = -2**31
MAX = 2**31 - 1

def reverse(x):
    out = 0
    
    if x>=0:
        ndigits = len(str(x))
        # reverse x from left to right except the last digit
        for i in range(ndigits-1):
            out += int(str(x)[i]) * 10**i
        # check overflow before reversing the last digit
        if (MAX-out) / 10**(ndigits-1) >= int(str(x)[-1]):
            out += int(str(x)[-1]) * 10**(ndigits-1)
        else:
            return 0
    
    elif x<0:
        x = abs(x)
        ndigits = len(str(x))
        # reverse x from left to right except the last digit
        for i in range(ndigits-1):
            out += int(str(x)[i]) * 10**i
        # check overflow before reversing the last digit
        if (-MIN-out) / 10**(ndigits-1) >= int(str(x)[-1]):
            out += int(str(x)[-1]) * 10**(ndigits-1)
        else:
            return 0
        out *= -1        
        
    return out        
    

if __name__ == '__main__':
    print(reverse(123))
    print(reverse(-123))
    print(reverse(120))
    print(reverse(2147483648))
    print(reverse(-2147483648))
    
    
    
    

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
* Open brackets must be closed by the same type of brackets.
* Open brackets must be closed in the correct order.
* Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
"""


def isValid(s):
    brackets = {'(': 1, ')':-1,
                '{': 2, '}':-2,
                '[': 3, ']':-3}
     
        
    # if s is empty, return True
    if s=='':
        return True   

    # if s starts with a closing brackets, return False
    if brackets[s[0]]<0:
        return False
    
    # if s starts with an opening brackets
    temp = ''
    for char in s:
        # add opening brackets to temp
        if brackets[char]>0:
            temp += char
        else:
            # if one abundant closing bracket subsequents a valid string, return False
            if temp == '':
                return False
            # remove an opening bracket if the subsequent bracket is a closing bracket of the same type
            elif brackets[temp[-1]] + brackets[char] == 0:
                temp = temp[:-1]
            # if the current closing bracket doesn't match the precedent opening one, return False
            else:
                return False
    if temp=='':
        return True
    else:
        return False
            
                          
    
if __name__ == '__main__':
    print(isValid("()"))
    print(isValid("()[]{}"))
    print(isValid("(]"))
    print(isValid("([)]"))
    print(isValid("{[]}"))
    print(isValid("()]"))
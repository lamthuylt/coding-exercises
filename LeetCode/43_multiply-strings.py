"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Note:
1. The length of both num1 and num2 is < 110.
2. Both num1 and num2 contain only digits 0-9.
3. Both num1 and num2 do not contain any leading zero, except the number 0 itself.
4. You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


#######################################
# This solution satisfies all the notes
#######################################
def multiply(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """    
    out = ''
    carry = 0
    
    # compute len(num2) last digits of the product
    for pos2 in range(len(num2)):
        sum_at_pos2 = carry
        for i in range(pos2+1):
            if len(num1) > pos2-i:
                sum_at_pos2 += int(num2[-(i+1)]) * int(num1[-(pos2-i+1)])
        out = str(sum_at_pos2)[-1] + out
        if sum_at_pos2 >= 10:
            carry = int(str(sum_at_pos2)[:-1])
        else:
            carry = 0

    # compute the first digits of the product
    for pos1 in range(len(num1)-2,-1,-1):
        sum_at_pos1 = carry
        for i in range(pos1+1):
            if len(num2) > i:
                sum_at_pos1 += int(num2[i]) * int(num1[pos1-i])
        out =str(sum_at_pos1)[-1] + out        
        if sum_at_pos1 >= 10:
            carry = int(str(sum_at_pos1)[:-1])
        else:
            carry = 0
    
    # fill the product with the remaining carry
    if carry > 0:
        out = str(carry) + out
        
    # remove all leading zeros of the output
    for digit in out:
        if digit != '0':
            break
        elif digit=='0' and len(out)>1:
            out = out[1:]
        
    return out
    
            
            
###################################
# This solution violates the note 4
###################################
def multiply2(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    def multiply_by_one_digit(num, num_one_digit):
        out = ''
        carry = 0
        # multiply num_one_digit to each digit of num from right to left 
        for char in reversed(num):
            prod = int(num_one_digit) * int(char) + carry
            out = str(prod)[-1] + out
            if prod>=10:
                carry = int(str(prod)[0])
            else:
                carry = 0
        # when num exhausts, add carry to the front of the result if it is not zero 
        if carry!=0:
            out = str(carry) + out
            
        return out    
    
    out = 0
    for pos,char2 in enumerate(reversed(num2)):
        out += int(multiply_by_one_digit(num1,char2) + '0'*pos)
    
    return str(out)
    

    
    
if __name__ == '__main__':
    print('Test 1: 123*456 = 56088 -> Output: '+multiply('123','456'))
    print('Test 2: 9*9 = 81 -> Output: '+multiply('9','9'))
    print('Test 3: 9*99 = 891 -> Output: '+multiply('9','99'))
    print('Test 4: 9133*0 = 0 -> Output: '+multiply('9133','0'))
    
    


"""
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]
Output: 1
Explanation: The third maximum is 1.

Example 2:
Input: [1, 2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: [2, 2, 3, 1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""

MIN = -999999999999


def thirdMax(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    triMax = [MIN, MIN, nums[0]]
    for num in nums[1:]:
        if num>triMax[0] and num<triMax[1]:
            triMax[0] = num
        elif num>triMax[1] and num<triMax[2]:
            triMax[0] = triMax[1]
            triMax[1] = num
        elif num>triMax[2]:
            triMax[0] = triMax[1]
            triMax[1] = triMax[2]
            triMax[2] = num
    
    if triMax[0]==MIN:
        return triMax[2]
    else:
        return triMax[0]
        


if __name__ == '__main__':
    print('Thirdmax: [3,2,1] -> {}'.format(thirdMax([3,2,1])))
    print('Thirdmax: [1,2] -> {}'.format(thirdMax([1,2])))
    print('Thirdmax: [2,2,3,1] -> {}'.format(thirdMax([2,2,3,1])))
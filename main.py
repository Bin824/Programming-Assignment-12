"""
Name: Bin Ni
Email: bin.ni81@myhunter.cuny.edu
Resources: None
"""

from typing import List

def find_duplicate(nums: List[int]) -> int:
    """
    Given an array of integers nums containing n + 1 integers where each integer 
    is in the range [1, n] inclusive, this function finds the repeated number in nums
    """
    low, high = 1, len(nums) - 1

    while low < high:
        mid = (low + high) // 2
        count = sum(num <= mid for num in nums)

        if count > mid:
            high = mid
        else:
            low = mid + 1

    return low

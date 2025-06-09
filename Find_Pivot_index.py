'''
🌟Problem Statement:
Given an array of integers nums, return the pivot index of this array.

🚩 The pivot index is the index where the sum of all the numbers strictly to the 
   left of the index is equal to the sum of all the numbers strictly to the right of the index.

🚩 If no such index exists, return -1. If there are multiple such indices, return the 
   left-most one.

☑️Constraints:
    1.You must solve it in O(n) time (avoid nested loops).
    2.You can use prefix sums or a running total strategy.
    
'''

# Naive approach # Time Complexity : O(n^2)
def get_left_sum(nums:list[int], index:int) -> int :
    if index == 0 :
        return 0
    total = 0
    for i in range(0,index):
        total += nums[i]
    
    return total
    pass

def get_right_sum(nums:list[int], index:int) -> int :
    if index == len(nums)-1 :
        return 0
    total = 0
    for i in range(index+1, len(nums)):
        total += nums[i]
    
    return total
    pass

def pivot_index(nums: list[int]) -> int:
    for i in range(len(nums)):
        left_sum = get_left_sum(nums, i)        
        right_sum = get_right_sum(nums, i)
        print(left_sum, right_sum)
        if left_sum == right_sum:
            return i
    return -1
    pass


# Optimized Approach # Time Complexity: O(n)
def pivot_index2(nums: list[int]) -> int:
    left_sum = 0
    total_sum = sum(nums)
    
    for i in range(len(nums)):
       if left_sum == (total_sum-left_sum-nums[i]):
           return i
       left_sum += nums[i]
       
    return -1
    pass

def main():
    nums = [3, 10, 2, 8, 7, 8]
    index = pivot_index2(nums)
    print(index)

main()
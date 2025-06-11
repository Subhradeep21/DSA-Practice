'''
🌟Problem Statement:
  Given an array of positive integers nums and an integer target, return the minimum 
  length of a contiguous subarray of which the sum is greater than or equal to target.
  If there is no such subarray, return 0.
    
⭐ Example:
    1.target = 7, nums = [2,3,1,2,4,3]  
      Output: 2  
      Explanation: The subarray [4,3] has the minimal length under the condition.
    
    2.Input: target = 15, nums = [1,2,3,4,5] 
      Output: 5
    
🚩Constraints:
    1.All numbers in nums are positive.
    2.Use a sliding window approach — no nested loops.
    3.Time Complexity should be O(n).
    
🧠 Hint:
    1.Use two pointers (start and end) to form a sliding window.
    2.Expand end to increase the sum.
    3.Once the sum ≥ target, move start forward to try to shrink the window and 
      update the minimum length.

'''

def min_subarray_len(target:int, nums:list[int]) -> int:
    left = 0
    current_sum = 0
    min_len = float('inf')
    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum >= target:
            min_len = min(min_len, right-left+1)
            current_sum -= nums[left]
            left += 1
            
    return min_len if min_len != float('inf') else 0
    pass 

def main():
    nums = [2,3,1,2,4,3,1,2]
    target = 7
    result = min_subarray_len(target, nums)
    print(result)

main()
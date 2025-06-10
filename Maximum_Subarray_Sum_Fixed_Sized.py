'''
🌟Problem Statement:
    Given an array of integers nums and an integer k, find the maximum sum of any 
    contiguous subarray of length k

⭐Example:
    Input: nums = [2, 1, 5, 1, 3, 2], k = 3  
    Output: 9  
    Explanation: Subarray [5,1,3] has the maximum sum = 9
    
🚩Constraints:
    1.Array length n ≥ k
    2.Time Complexity must be O(n) (do not use nested loops)

🧠 Hint:
Use the sliding window technique:
    1.Compute the sum of the first k elements
    2.Slide the window by removing the first element of the previous window and adding
      the next element.
    3.Track the maximum sum seen

'''

def max_subarray_sum(nums: list[int], k: int) -> int:
    sub_sum = 0
    max_sum = -10000
    ln = 0
    for i,num in enumerate(nums):
        sub_sum += num 
        ln += 1
        if ln == k :
            max_sum = max(max_sum, sub_sum)
            sub_sum -= nums[i-k+1]
            ln -= 1
    return max_sum
    pass

# Same approach better/cleaner code. Calculating the initial window sum at the beginning
def max_subarray_sum2(nums:list[int], k:int) -> int:
    sub_sum = sum(nums[:k])
    max_sum = sub_sum
    for i in range(k, len(nums)):
        sub_sum += nums[i] - nums[i-k]
        max_sum = max(max_sum, sub_sum)
        
    return sub_sum
    pass 

def main():
    arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
    # arr = [2,1,5,1,3,2]
    k = 4
    result = max_subarray_sum2(arr,k)
    print(result)
    
main()
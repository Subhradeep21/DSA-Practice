def longestSubarraySum(nums:list[int], k:int) -> int:
    left = 0
    mx_len = 0
    sub_sum = 0
    for right, num in enumerate(nums):
        sub_sum += num
        while sub_sum > k:
            sub_sum -= nums[left]
            left += 1
        mx_len = max(mx_len, right-left+1)
    return mx_len
    pass 

def main():
    nums = [1, 2, 1, 0, 1, 1, 0]
    k = 4
    result = longestSubarraySum(nums, k)
    print(result)

main()
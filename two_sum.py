'''
🌟Problem Statement:
Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may 
not use the same element twice.

Return the answer as a list of two indices.

🧠Hint - Hash Map Trick (One-pass approach):
Use a dictionary (num_to_index) to store numbers you've already seen along with 
their index.

As you loop through the array:
    1.For the current number num, calculate its complement:
    2.Check: Is this complement already in the dictionary?
        ✅ If yes → you've found the two numbers.
        ❌ If no → store num and its index in the dictionary.
'''

def two_sum(nums: list[int], target: int) -> list[int]:
    hashmap = dict()
        
    for i, num in enumerate(nums):
        complement = target - nums[i]
        if complement in hashmap:
            return [hashmap[complement], i]
        hashmap[num] = i

    return [-1,-1]

def main():
    nums = [2, 7, 11, 15]
    target = 10
    r = two_sum(nums, target)
    print(r)



main()
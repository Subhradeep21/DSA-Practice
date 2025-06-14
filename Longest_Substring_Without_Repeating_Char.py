'''
🌟Problem Statement:
  Given a string s, find the length of the longest substring without repeating 
  characters.
  
⭐Examples:
    1.Input: s = "abcabcbb"
      Output: 3
      Explanation: The answer is "abc", with length 3.
    
    2.Input: s = "bbbbb"
      Output: 1
      Explanation: The answer is "b", with length 1.
    
    3.Input: s = "pwwkew"
      Output: 3
      Explanation: The answer is "wke", with length 3.
      
🚩Constraints:
    1.Characters are all ASCII (no special unicode needed)
    2.You should aim for O(n) time using a hash map or set to track seen 
      characters.

🧠 Hint:
    1.Use a sliding window: start and end pointers.
    2.Use a set or dict to track characters in the current window.
    3.When you hit a duplicate, shrink the window from the left until the 
      duplicate is removed.

'''

def length_of_longest_substring(s: str) -> int:
    left = 0
    max_len = 0
    char_dict = dict()
    
    for right, ch in enumerate(s):
        if ch in char_dict:
            left = max(left,char_dict[ch]+1)
        max_len = max(max_len, right-left+1)
        char_dict[ch] = right
        
    return max_len
    pass

def main():
    # st = "tmmzuxtm"
    st = "abbac"
    result = length_of_longest_substring(st)
    print(result)
    
main()
'''
📝 Description:
   You are given a string s and an integer k. You can choose any character in the 
   string and replace it with any other uppercase English letter at most k times.

   Return the length of the longest substring that can be obtained containing 
   only the same character after performing at most k replacements.
   
   Example 1:
    Input: s = "ABAB", k = 2
    Output: 4
    Explanation: Replace the two 'A's with two 'B's or vice versa.
    
  Example 2:
    Input: s = "AABABBA", k = 1
    Output: 4
    Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
    The substring "BBBB" has the longest repeating letters, which is 4.
    There may exists other ways to achieve this answer too.
    
🚩Constraints:
    1. 1 <= s.length <= 105
    2. s consists of only uppercase English letters.
    3. 0 <= k <= s.length
    
    
🧮 Algorithm Approach (Sliding Window)
    1. Initialize Pointers and Helpers
        * Use two pointers left and right to maintain a sliding window.
        * Use a dictionary char_freq to count character frequencies in the 
          current window.
        * Use a variable max_freq to store the maximum frequency of any character
          in the current window.
        * Use max_len to store the result — the length of the longest valid 
          window found.
    
    2. Expand the Window
        * Iterate over the string using the right pointer.
        * Add s[right] to the char_freq dictionary and update its count.
        * Update max_freq to reflect the highest frequency of any character in 
          the window.
    
    3. Shrink the Window if Invalid
        * If (right - left + 1) - max_freq > k, the window is invalid:
        * Reduce the count of s[left] in the dictionary.
        * Move the left pointer to shrink the window.
    
    4. Update the Result
        * At each step, update max_len with the maximum valid window length 
          encountered so far.
'''


def characterReplacement(s: str, k: int) -> int:
    left = 0
    char_freq = dict()
    mx_len = 0
    mx_freq = 0
    for right, ch in enumerate(s):
        char_freq[ch] = char_freq.get(ch,0)+1
        mx_freq = max(mx_freq,char_freq[ch])
        if (right-left+1)-mx_freq <= k :
            mx_len = max(mx_len, right-left+1)
        else:
            char_freq[s[left]] -= 1
            left += 1
    return mx_len
    pass

def main():
    st = "AABABBABB"
    k = 2
    result = characterReplacement(st, k)
    print(result)
    
main()
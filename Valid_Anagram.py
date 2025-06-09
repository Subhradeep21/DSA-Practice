'''
🌟Problem Statement:
Given two strings s and t, return True if t is an anagram of s, and False otherwise.

🚩An anagram is a word or phrase formed by rearranging the letters of another, using 
all the original letters exactly once.

☑️Constraints:
    1.You may assume the strings contain only lowercase alphabets.
    2.Try to solve it in O(n) time using a hash map (dictionary).
    3.Don't use built-in sorted() or collections.Counter() for now — try to build your own logic.

🧠 Hint:
    1.Create two dictionaries to store the character frequencies of each string.
    2.Compare both dictionaries — if they're identical, the strings are anagrams.
'''

def get_frequency(st:str) -> dict:
    frequency = {}
    for s in st:
        if s in frequency:
            frequency[s] += 1
        else:
            frequency[s] = 1
    return frequency
    pass

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    s_freq = get_frequency(s)
    t_freq = get_frequency(t)

    if s_freq == t_freq:
        return True
    else:
        return False
    
    pass


# Slight variation where we are only using one dictionary 
def is_anagram2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    s_freq = get_frequency(s)
    # t_freq = get_frequency(t)

    for ch in t:
        if ch in s_freq:
            s_freq[ch] -= 1
        else:
            return False

    for value in s_freq.values():
        if value != 0:
            return False

    return True

def main():
    s = "apple"
    t = "applen"
    print(is_anagram(s,t))
    print(is_anagram2(s,t))
    
main()
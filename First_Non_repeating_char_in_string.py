def first_non_repeating_char(my_str: str) -> str:
    frequency = {}

    for ch in my_str:
        frequency[ch] = frequency.get(ch, 0) + 1
    #     if ch in frequency:
    #         frequency[ch] += 1
    #     else:
    #         frequency[ch] = 1
    

    print(frequency)
        
    for key,value in frequency.items():
        if value == 1:
            return key
        
    return 'None'

def main():
    s = "swiss"
    print(first_non_repeating_char(s))
    
main()
    
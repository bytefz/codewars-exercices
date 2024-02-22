from collections import Counter

def solution(roman_num: str) -> int|str:
    
    if isinstance(roman_num, str):
        dicc_roman_num = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        num_total = 0
        
        # Optional - Validate the form of the Roman Numeral
        # print(Counter(roman_num))

        # Functionality
        list_num_convert = list(map(lambda l: [value for letter, value in dicc_roman_num.items() if letter==l][0], roman_num))
        list_num_convert = list_num_convert[::-1]
        
        for i, num in enumerate(list_num_convert):
            if i == 0: # First number
                num_total += num
            elif num < list_num_convert[i-1]: # If the number is less than the previous number
                num_total -= num
            else: # If the number is greater than the previous number
                num_total += num
        
        return num_total
        
    else: return f"The Roman Numeral({roman_num}) is not a string"
    
if __name__ == '__main__':
    print(solution("MCMXC"))
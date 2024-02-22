from typing import Union

Digit = Union[int, float]

def max_3(*args: Digit) -> Digit:
    
    stack:list = [num for num in args]
    stack.sort()
    return stack[-1]
    
# I ussualy think that we must make general function.

if __name__ == "__main__":
    print(max_3(1,2,4))
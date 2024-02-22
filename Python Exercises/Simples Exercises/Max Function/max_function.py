"""
Define a max() function that takes two numbers as arguments and returns the largest of them.
"""
from typing import Union

class NotSupportedNumber(Exception): ...


def max(num1: Union[int, float], num2:int|float) -> int|float:
    """Function to compare teo numbers and return the largest of them
    
    Keyword arguments:
    num1, num2 -- Numbers to compare
    Return: int | float
    """
    if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
        if num1 > num2:
            return num1
        
        if num1 < num2:
            return num2
        
        if num1 == num2:
            return -1
    
    raise NotSupportedNumber(f"{num1} or {num2} are not supported.")

if __name__ == "__main__":
    
    # Test 1: int | int
    print(f"El número mayor entre 1 y 2 es: {max(1, 2)}")
    
    # Test 2: int | float
    # max(5, 6.2)
    print(f"El número mayor entre 5 y 6.2 es: {max(5, 6.2)}")

    # Test3: str | float
    # max("5", 6.2)
    print(f"El número mayor entre '5' y 6.2 es: {max(5, 6.2)}")
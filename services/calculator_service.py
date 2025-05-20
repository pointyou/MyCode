from typing import Literal


def calculate(num1: float, op: Literal['+','-','*','/'], num2: float) -> float:
    """Perform a basic arithmetic calculation."""
    if op == '+':
        return num1 + num2
    if op == '-':
        return num1 - num2
    if op == '*':
        return num1 * num2
    if op == '/':
        if num2 == 0:
            raise ValueError("除數不能為零")
        return num1 / num2
    raise ValueError("未知運算")

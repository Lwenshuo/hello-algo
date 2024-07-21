import random

def while_loop(num: int) ->int:
    """while loop"""
    res = 0
    i = 1
    while i <= num:
        res += i
        i += 1
    return res

if __name__ == "__main__":
    num = 5
    res = while_loop(num)
    print("result=", res)

import random

def while_loop(num: int) ->int:
    """while loop"""
    res = 0
    i = 1
    while i <= num:
        res += i
        i += 1
        i = i*2
    return res

def double_loop(num: int) ->int:
    """double loop"""
    res = ""
    for i in range(1, num):
        for j in range(1, num):
            res += f"({i} {j});"
    return res

def recur(num: int) ->int:
    """recursion"""
    if num == 2:
        return 2
    return num + recur(num-1)

def tail_recur(num: int, res: int) ->int:
    """tail recursion"""
    if num == 0:
        return res
    return tail_recur(num-1, res+num) 

def fib(num: int) -> int:
    if num == 0 or num == 1:
        return num - 1
    return (fib(num-1) + fib(num-2))

def for_recur_loop(num: int) ->int:
    stack = []
    res = 0
    for i in range(n,0,-1):
        stack.append(i)
    while stack:
        res += stack.pop()
    return res

if __name__ == "__main__":
    num = 5
    res = while_loop(num)
    print("result=", res)
    
    res_f = double_loop(num)
    print("result_double_loop=", res_f)
    
    res_recur = recur(num)
    print("result_recur=", res_recur)
    
    res_fib = fib(num)
    print("result_fib=", res_fib)

# The moment you call a function, the stack is involved by definition.

# 1️⃣ Base Case → stops recursion: It is the condition where recursion must stop.

# 2️⃣ Recursive Case → reduces problem size: It is where the function calls itself with a smaller input.

def f(n):
    if base_condition:
        return base_value
    return work + f(smaller_input)

def fact(num):
    if num == 0 or num == 1:
        return 1  # base case
    return num * fact(num - 1)  # recursive case

print(fact(5))

def palindrom(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and palindrom(s[1:-1])

print(palindrom('madam'))

def sum_of_num(num):
    if num == 0:
        return 0     
    return num + sum_of_num(num - 1)   

print(sum_of_num(10))

def sum_of_list_ele(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum_of_list_ele(arr[1:])  # indexing + slicing.

nums = [1, 2, 3, 4, 5, 6]
print(sum_of_list_ele(nums))

def count_digit(num_str):
    if num_str == "":
        return 0
    else:
        return 1 + count_digit(num_str[1:])

print(count_digit('059957fnuh09403'))

def reverse_str(st):
    if st == "":
        return ""
    return st[-1] + reverse_str(st[:-1])
print(reverse_str('Tyson'))

def cal_power(a, b):
    if b == 0:
        return 1
    return a * cal_power(a, b - 1)
print(cal_power(3, 5))

def fib(num):
    if num == 0 or num == 1:
        return num
    return fib(num - 1) + fib(num - 2)
print(fib(3))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)
print(gcd(12, 28))

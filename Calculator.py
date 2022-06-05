from math import pow
numbers = [chr(_) for _ in range(ord('0'), ord('9') + 1)] + \
          [chr(_) for _ in range(ord('A'), ord('F') + 1)]


def calculate(number, base=2):
    total = 0
    str_number = str(number)[::-1]

    for i in range(len(str_number)):
        total += numbers.index(str_number[i]) * int(pow(base, i))
    return total


def trans_10_to_base(num, base=2):
    res = ''
    while num:
        num, d = divmod(num, base)
        sd = str(d) if d < 10 else chr(ord('A')+d-10)
        res = sd + res
    return res


print(trans_10_to_base(513))

'''for __ in range(9, 6000):
    print(f'{calculate(88, __)} = {calculate(32, __) + calculate(22, __) + calculate(16, __) + calculate(17, __)}')
    if calculate(88, __) == calculate(32, __) + calculate(22, __) + calculate(16, __) + calculate(17, __):
        break
else:
    print('fuck off')'''

print(0x1F1C8)
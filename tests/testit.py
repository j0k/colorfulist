import sys
sys.path.append("..")

import colorfulist as CL
colorama = CL.colorama

l = CL.Colorfulist([1,2,3,4,5])
l.colors[1] = 'red'
print(str(l))

l.colors[1:3] = 'magenta'
print(str(l))


l = CL.Colorfulist([1,2,3,4,5], autocoloring=False, default_color=colorama.Fore.BLUE + colorama.Back.BLACK)
print(l)

l.colors[1:3] = colorama.Fore.MAGENTA = colorama.Back.WHITE
print(str(l))
print(l.colors)

numbers = CL.Colorfulist(range(10))

print(colorama.Fore.RESET)

is_odd = lambda x: (x % 2) == 1
numbers.coloring(is_odd, 'cyan')

print(str(numbers))
print(colorama.Fore.RESET)

def is_prime(x):
    if x<=3:
        return True

    for d in range(2, x):
        if x % d == 0:
            return False
    return True

numbers.coloring(is_prime, 'green')
print(str(numbers))

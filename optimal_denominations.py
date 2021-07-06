# CodeChef July Challenge 2021
# Problem code: MINNOTES

# TLE - optimization left
import math
 
d = {}

def get_gcd(l):
    if len(l) == 1:
        return l[0]
    else:
        n = len(l)//2
        g_left, g_right = get_gcd(l[:n]), get_gcd(l[n:])
        if (g_left, g_right) in d.keys():
            return d[(g_left, g_right)]
        else:
            return math.gcd(g_left, g_right)

def get_minnotes(elements, index):
    if len(elements) == 1:
        return elements[0]
    gcd = int
    s = 0
    length = len(elements)
    if index == 0:
        gcd = get_gcd(elements[1:])
    elif index == length - 1:
        gcd = get_gcd(elements[:index])
    else:
        gcd = math.gcd(get_gcd(elements[:index]), get_gcd(elements[index + 1:]))
    s = sum(elements[:index]) + sum(elements[index + 1:])
    return s//gcd

def get_optimal_denominations(salary_list, n):
    notes = []
    for i in range(n):
        notes.append(get_minnotes(salary_list, i) + 1)
    return min(notes)

T = int(input())
output = []

while T > 0:
    n = int(input())
    salary = [int(i) for i in input().strip().split()]
    output.append(get_optimal_denominations(salary, n))
    T -= 1

for o in output:
    print(o)
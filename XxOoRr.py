# cook your dish here
# codechef July Challenge 2021: Problem Code: XXOORR
import math

def XXOORR(elements: list, n, k):
    elements.sort()
    p = 0
    total_operations = 0
    while n > 0:
        cost = 0
        for i in range(n):
            t = (2 ** p) ^ elements[i]
            if t < elements[i]:
                elements[i] = t
                cost += 1
        total_operations += math.ceil(cost/k)
        elements = [e for e in elements if e != 0]
        p += 1
        n = len(elements)          
    return total_operations


T = int(input().strip())
output = []

while T>0:
    n, k = [int(i) for i in input().strip().split()]
    l = [int(i) for i in input().strip().split()]
    output.append(XXOORR(l, n, k))
    T -= 1

for i in output:
    print(i)

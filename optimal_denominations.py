# CodeChef July Challenge 2021
# Problem code: MINNOTES

# 1 task - WA
import math

def get_gcd(elements):
    d = {}
    if len(elements) == 1:
        d['smallest_out'] = None
        d['all_in'] = elements[0]
        d['largest_out'] = None
    elif len(elements) == 2:
        d['smallest_out'] = elements[-1]
        d['all_in'] = math.gcd(d['smallest_out'], elements[0])
        d['largest_out'] = elements[0]
    else:
        gcd = elements[1]
        for element in elements[2:-1]:
            gcd = math.gcd(gcd, element)
        d['smallest_out'] = math.gcd(gcd, elements[-1])
        d['all_in'] = math.gcd(d['smallest_out'], elements[0])
        d['largest_out'] = math.gcd(gcd, elements[0])
    # print(d)
    return d


def get_optimal_denominations(salary_list, n):
    if n == 1:
        return 0
    salary_list.sort()
    s = sum(salary_list)
    even = [i for i in salary_list if i%2 == 0]
    odd = [i for i in salary_list if i%2 == 1]
    # print(even, odd, s)

    if len(even) == 0:
        odd_gcd = get_gcd(odd)
        return min((s - odd[0])//odd_gcd['smallest_out'], (s - odd[-1])//odd_gcd['largest_out'])
    elif len(odd) == 0:
        even_gcd = get_gcd(even)
        return min((s - even[0])//even_gcd['smallest_out'], (s - even[-1])//even_gcd['largest_out'])
    else:
        odd_gcd = get_gcd(odd)
        even_gcd = get_gcd(even)    


    if even_gcd['smallest_out'] is None and odd_gcd['smallest_out'] is None:
        return 1
    
    if even_gcd['smallest_out'] is not None:
        min_leaving_small_even_out = (s - even[0])//math.gcd(odd_gcd['all_in'], even_gcd['smallest_out'])
        min_leaving_large_even_out = (s - even[-1])//math.gcd(odd_gcd['all_in'], even_gcd['largest_out'])
        # print(min_leaving_large_even_out, min_leaving_small_even_out)
        # print(math.gcd(odd_gcd['all_in'], even_gcd['smallest_out']), math.gcd(odd_gcd['all_in'], even_gcd['largest_out']))
        min_even = min(min_leaving_large_even_out, min_leaving_small_even_out)
    
    if odd_gcd['smallest_out'] is not None:
        min_leaving_small_odd_out = (s - odd[0])//math.gcd(even_gcd['all_in'], odd_gcd['smallest_out'])
        min_leaving_large_odd_out = (s - odd[-1])//math.gcd(even_gcd['all_in'], odd_gcd['largest_out'])
        # print("\n\n", min_leaving_large_odd_out, min_leaving_small_odd_out)
        # print(math.gcd(even_gcd['all_in'], odd_gcd['smallest_out']), math.gcd(even_gcd['all_in'], odd_gcd['largest_out']))
        min_odd = min(min_leaving_large_odd_out, min_leaving_small_odd_out)
    
    if even_gcd['smallest_out'] is not None and odd_gcd['smallest_out'] is not None:
        return min(min_odd, min_even)
    elif even_gcd['smallest_out'] is None:
        return min((s - even[0])//odd_gcd['all_in'], min_odd)
    else:
        return min((s - odd[0])//even_gcd['all_in'], min_even)

T = int(input())
output = []

while T > 0:
    n = int(input())
    salary = [int(i) for i in input().strip().split()]
    output.append(get_optimal_denominations(salary, n) + 1)
    T -= 1

for o in output:
    print(o)
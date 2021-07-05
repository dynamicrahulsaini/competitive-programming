# CodeChef problem code: BENDSPF7
# solution link: https://www.codechef.com/viewsolution/47905329

def max_people(n,m):
    A = [int(0) for i in range(n)]
    B = A.copy()

    d_a=0
    d_b=0
    l = []
    for i in range(m):
        l = [int(j) for j in input().strip().split()]
        A[l[0]-1]+=1
        B[l[1]-1]+=1
    for i in range(n):
        if A[i]<n:
            d_a+=1
        if B[i]<n:
            d_b+=1
    return 2*min(d_a,d_b)


t = int(input().strip())

output = []

while(t):
    l = [int(i) for i in input().strip().split()]
    n = l[0]
    m = l[1]
    output.append(max_people(n,m))
    t-=1

for i in output:
    print(i)

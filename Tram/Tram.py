n, k = input().split()
n = int(n)
k = int(k)
for _ in range(k):
    if n % 10!=0:
        n=n-1
    else:
        n=n/10
print (int(n))
t = int(input())
for y in range(t):
    x = int(input())
    z = []
    p = []
    for b in range(2, x+1):
        if x % b == 0:
            z.append(b)
    for n in z:
        a = []
        for i in range(2, n):
            if n % i == 0:
                a.append(i)
        if not a:
            p.append(n)
    print(max(p))

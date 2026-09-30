porog = float(input())
n = int(input())
kv = 0
kv1 = 0
maxi = -1E17
a = []
for i in range(n):
    c = input()
    if c == 'error':
        kv += 1
    if c != 'error':
        q = float(c)
        a.append(q)
        if q > porog:
            kv1 += 1
        if q > maxi:
            maxi = q
sr = sum(a)/len(a)       
print(n)
print(kv)
print(kv1)
print(f'{maxi:.1f}')
print(f'{sr:.1f}')

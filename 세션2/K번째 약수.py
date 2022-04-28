N,K = map(int,input().split())
a=[]
for i in range(1,N+1): # 1부터!
    if N%i == 0:
        a.append(i)
a.sort() # a원본 리스트를 정렬시킨 것임
if len(a)<K:
    print(-1)
else:
    print(a[K-1])


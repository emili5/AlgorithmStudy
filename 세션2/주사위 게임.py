import sys
n = int(input())
max=-1247000000
for i in range(n):
    tmp = list(map(int,sys.stdin.readline().split()))
    # tmp.sort() #눈이 다른 경우 큰 숫자를 찾기 위해
    a,b,c = map(int,tmp) # 한 줄 n개 정수를 한 변수에 넣기 위해서는 리스트로 받은 다음 map으로 매칭시켜준다!
    if a==b and b==c: #같은 눈이 세 개가 나오면
        m = 1000*a+10000
    elif a==b or a==c :
        m = 1000+a*100
    elif b==c:
        m = 1000+b*100
    else:
        m = c*100
    if m>max:
        max=m
print(max)


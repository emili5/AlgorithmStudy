n = int(input())
a = list(map(int,input().split()))

def digit_sum(x):
    sum=0
    for i in str(x): # 받은 숫자를 문자화 시키는 함수 str()
        sum+=int(i) # 정수화 시켜서 합
    return sum

max = -1247000000 # 가장 작은 값으로 설정, 어떤 값이랑 비교해도 그 값이 최대가 되도록 하기 위해
for x in a:
    tot = digit_sum(x)
    if tot>max:
        max=tot
        res = x #숫자 출력해야 하므로 저장
print(res)
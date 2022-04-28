N, M = map(int, input().split())
n = [i + 1 for i in range(N + 1)]  # list내에서 for문으로 값 넣기
m = [i + 1 for i in range(M+1)]
# 합의 개수 카운트 하는 변수
cnt=[0]*(N+M)
max = -214700000
for i in range(1,N+1):
    for j in range(1,M+1):
        cnt[i+j]+=1 #개수 추가

#가장 많이 나온 값 탐색
for i in range(N+M+1):
    if cnt[i]>max:
        max=cnt[i]
# 최대값 출력
for i in range(N+M+1):
    if cnt[i]==max:
        print(i, end="")


import sys
n = int(input())
check = list(map(int,sys.stdin.readline().split()))
score=0
cnt=0 # 맞힌 개수 만큼 가중치를 점수에 더해야 하므로 설정
for x in check:
    if x==1:
        cnt+=1
        score+=cnt
    else:
        cnt=0
print(score)

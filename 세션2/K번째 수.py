T = int(input()) # 테스트 케이스
for t in range(T):      # 각 테스트 케이스 별로 읽어들임
    N, s, e, k = map(int, input().split())
    num = [int(i) for i in input().split()] # 여러 입력을 리스트로 만들고 싶을 때
    num = num[s-1:e]
    num.sort()
    print("#%d %d" %(t+1,num[k-1]))


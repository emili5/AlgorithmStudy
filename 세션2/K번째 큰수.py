N,K  = map(int,input().split())
a = list(map(int,input().split())) # 입력값을 리스트 형태로 받는다.
# 더한 값을 중복을 허용하지 않기 위해 set()자료형으로 받는다.
res = set()

#서로 겹치지 않는 인덱스 값을 위해 3중 for문 사용
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            res.add(a[i]+a[j]+a[k])
# 큰 수를 출력해야 하므로 sort해야 함
# 근데 set은 sort가 안되므로 리스트로 바꿔서 다시 sort
res = list(res)
# 내림차순으로 뽑고 싶으면 reverse = True로 설정
res.sort(reverse=True)
print(res[k-1])
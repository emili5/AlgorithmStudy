n = int(input())

ch=[0]*(n+1) #0~20인덱스의 배열 만들기 위해
cnt=0 # ch[i]가 0인 것의 개수 카운팅하는 변수
for i in range(2,n+1):
    if ch[i]==0:
        cnt+=1
        for j in range(i,n+1,i):
            ch[j]=1
print(cnt)

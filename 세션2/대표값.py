N = int(input())
a= list(map(int, input().split()))
avg = round(sum(a)/N) #round()가 반올림해주는 함수
# round(), round_half_even()은 딱 중간에 있으면 짝수 쪽으로 반올림하는 함수
min=abs(a[0]-avg)
for idx,s in enumerate(a):
    tmp = abs(s-avg)
    # 이전에 같은 점수가 없는 경우
    if tmp<min:
        min=tmp
        score=s # 점수도 저장해야 함
        res = idx+1
    # 같은 점수가 나온경우
    elif tmp==min:
        if s>score: # s>=score라고 하면 어떤 문제?-> 뒤에 같은 점수가 나오면 갱신한다.
            score=s
            res=idx+1
    print(avg,res)
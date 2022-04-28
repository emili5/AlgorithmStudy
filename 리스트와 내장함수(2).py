#리스트의 부분 리스트 출력
# list[:3]

# 인덱스 정보까지 같이 출력
# enumerate()
# (idx,value)의 튜플형태로 반환해줌
a=list(range(1,11))
for x in enumerate(a):
    print(x)
for x in enumerate(a):
    print(x[0],x[1])

# 이런방식으로 젤 많이 쓰임
for index,value in enumerate(a):
    print(index,value)

# 모든 iterator 반환값이 참이면 참을 반환하는 함수
# all()
if all(60>x for x in a):
    print('yes')

# 반환값이 하나라고 참이면 참을 반환하는 함수
# any
if any(11>x for x in a):
    print('yes')


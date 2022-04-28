import random as r
#  빈 리스트
a=[]
b=list()

# 1부터 10까지 리스트 생성
b = list(range(1,11))
print(b)

# 리스트에 요소 추가
# append()

# 특정 인덱스 위취에 요소 추가
# insert(idx,value)

# 가장 맨 뒤 자료를 빼고 싶음
# pop()
# 인자로 인덱스 번호를 넘기면 해당 인덱스의 값이 빠짐

# 값을 지정해서 지우고 싶음
# remove(value)

# 값의 인덱스 반환
# index(value)

# 리스트에 있는 모든 요소의 합 출력
# sum()

# 가지고 있는 인자 값들 중 가장 큰 값 찾기
# max(list)
# 가장 작은 값 찾기
# min(list)
# max(1,2,3,4,5)

# 요소를 랜덤으로 섞는 함수
# shuffle()
r.shuffle(b)
print(b)

# 리스트 요소 오름차순 정렬
# sort()
b.sort()

# 내림차순
# sort(reverse=True)
b.sort(reverse=True) # 리스트 자체를 정렬
print(b) # 후 출력

# 1차원 리스트
a = [0]*3

# 리스트 안 반복문으로 1차원 배열을 리스트로 만들어 2차원 배열을 만든다.
# 3x3
a = [[0]*3 for _ in range(3)]

#2차원 배열을 표 형식으로 확인
for x in a:
    print(x)

# 모든 요소에 접근
for x in a:
    for y in x:
        print(y,end=' ')
    print()

for i in range(len(a)):
    for j in a[i]:
        print(j)

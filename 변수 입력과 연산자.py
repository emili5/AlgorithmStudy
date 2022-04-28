# 여러 값을 입력 받아서 각 변수에 넣고 싶을 때
# input()으로 두 개 이상의 값을 입력받고 split()함수로 공백 기준으로 잘라서 변수에 대입
a,b = input().split()

# 입력받은 변수를 바로 정수화 시켜서 저장시키는 방식
# map이용
a,b = map(int,input().split())

# 정수를 한 번에 많이 입력받을 때 input()사용하지 않는다
# 한 개의 정수 입력받기

import sys
a = int(sys.stdin.readline()) # 한 줄을 읽고 이를 정수로 바꾸서 a에 저장
b = sys.stdin.readline().rstrip() # 한 줄을 읽고 다음 스페이스 빼고 문자열 저장

#여러 개의 정수를 한 줄에 입력 받아 리스트에 저장
data = list(map(int,sys.stdin.readline().split()))

#정수 n줄을 입력받아 리스트 저장
n = int(input()) #입력받을 줄 개수
data = [int(sys.stdin.readline()) for i in range(n)]


a = sys.stdin.readline() # readline()은 한 줄만 읽는다

#for문으로 한 줄 씩 입력받아 리스트에 저장
n = int(input())
for i in range(n):
    tmp = input().split()
    print(tmp)

# 출력결과
# 3
# 1 2 3
# ['1', '2', '3']
# 4 5 6
# ['4', '5', '6']
# 6 7 8
# ['6', '7', '8']

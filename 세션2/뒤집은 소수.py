n = int(input())
a = list(map(int,input().split()))

#숫자 뒤집을 때는 이렇게 쓰자!!
def reverse(x):
   return int(str(x)[::-1])

def isPrime(x):
    if x==1:    #1은 소수 아님
        return False
    for i in range(2,x//2+1): #소수는 1과 자기자신 제외하고 '2 x 자기자신'까지만 소수 존재
        if x%i==0:
            return False
    return True

for x in a:
    x = reverse(x)
    if isPrime(x):
        print(x, end=' ')
# 문자열의 모든 철자를 대문자로 만들어주는 내장 함수
# upper
# lower
msg = 'My name is JM'
print(msg.upper())
print(msg.lower())

# 문자열에서 특정 문자의 인덱스 번호 반환하는 내장함수
# find
print(msg.find('m'))
# 특정 문자 개수 반환
# count
print(msg.count('e'))

# 부분 문자열만 뽑아내고 싶음-[:]
print(msg[3:6])

# 문자열의 문자에 인덱스 번호로 접근하고 싶을 때
# len()함수 이용
for i in range(len(msg)):
    print(msg[i],end='')

# 문자열 내 문자가 대문자인지 아닌지 확인
# isupper()
for x in msg:
    if x.isupper():
        print('대문자:',x)
# 소문자는 islower()

# 문자가 알파벳이면 참
# isalpha()
for x in msg:
    if x.isalpha():
        print('알파벳:',x)


#문자의 아스키넘버 반환
# ord()
tmp='AZ'
for x in tmp:
    print(ord(x))

#정수값에 대응되는 문자 출력함수
# chr()
tmp=65
print(chr(tmp))
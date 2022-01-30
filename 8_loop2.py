from re import L


print("\n151")
list1 = [3, -20, -3, 44]
for i in list1:
    if i < 0:
        print(i)

print("\n152")
list1 = [3, 100, 23, 44]
for i in list1:
    if i % 3 == 0:
        print(i)

print("\n153")
list1 = [13, 21, 12, 14, 30, 18]
for i in list1:
    if i % 3 == 0 and i < 20:
        print(i)
# 너무 길어지면 조건에 괄호 써도 됨

print("\n154")
list1 = ["I", "study", "python", "language", "!"]
for i in list1:
    if len(i) >= 3:
        print(i)

print("\n155")
list1 = ["A", "b", "c", "D"]
for i in list1:
    if i.isupper():
        print(i)

print("\n156")
for i in list1:
    if i.islower():
        print(i)

# for i in list1:
#     if not i.isupper():
#         print(i)
# 논리연산자 not을 사용할 수도 있음

print("\n157")
list1 = ['dog', 'cat', 'parrot']
for i in list1:
    print(i[0].upper()+i[1:])
# +로 하면 문자열 띄어쓰기 없음

print("\n158")
list1 = ['hello.py', 'ex01.py', 'intro.hwp']
for i in list1:
    i = i.split(".")
    print(i[0])

print("\n159")
list1 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in list1:
    split = i.split(".")
    if split[1] == "h":
        print(i)

print("\n160")
for i in list1:
    split = i.split(".")
    if split[1] == "c" or split[1] == "h":
        print(i)
# for문 if문 안에서 변수 바인딩하면 내부에서만 쓸 수 있음

print("\n161")
for i in range(100):
    print(i)

print("\n162")
for i in range(2002,2051,4):
    print(i)

print("\n163")
for num in range(3, 31, 3):
    print(num)

print("\n164")
for num in range(99, -1, -1):
    print(num)
# for i in range(100):
#     print(99 - i)

print("\n165")
for num in range(10):
    print("0." + str(num))
for num in range(10) :
    print(num / 10)
# 계산은 컴퓨터가 하게 하자

print("\n166")
list1 = list(range(3, 28, 3))
# for dex, val in enumerate(list1):
#     print("3x"+str(dex), "=", str(val))

name = "홍길동"
age = 19
print(f"안녕하세요. {name}입니다. 나이는 {age}살입니다.")

for i in range(1, 10):
    print(f"3x{i} = {i*3}")
# for i in range(1, 10) :
#     print (3, "x", i, " = ", 3 * i)
# f string 쓰는 게 훨씬 나음
# 가독성이 좋고 빠름

print("\n167")
for i in range(1, 10, 2):
    print(f"3x{i} = {3*i}")

print("\n168")
hab = 0 # 이걸 for문 안에 작성하면 바인딩부터 다시 해서 값 초기화 됨
for i in range(1, 11):
    hab += i
    print(hab)

# a = 10
# a = a + 10
# # a += 10
# print(a) # ???

# 변수 += 값
# ->> 변수 = 변수 + 값
# -=, *=, %=, /=, //=(몫)

# hab += i
# hab = hab + 1

print("\n169")
hab = 0
for i in range(1, 11, 2):
    hab += i
print(hab) # for문 안에 쓰면 값도 여러 번 계속 출력

print("\n170")
gop = 1
for i in range(1, 11):
    gop *= i
print(gop)

print("\n171")
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(price_list[i])

print("\n172")
for i in range(len(price_list)):
    print(i, price_list[i])

print("\n173")
for i in range(len(price_list)):
    print((len(price_list)-1)-i, price_list[i])

print("\n174")
for i in range(1, 4):
    print(90 + i * 10, price_list[i])

print("\n175")
my_list = ["가", "나", "다", "라"]
for i in range(0,len(my_list)-1):
    print(my_list[i], my_list[i+1])
# len() = int
# print(type(len(my_list)))

print("\n176")
my_list = ["가", "나", "다", "라", "마"]
for i in range(0, 3):
    print(my_list[i], my_list[i+1], my_list[i+2])
# for i in range( len(my_list) - 2 ):
#     print(my_list[i], my_list[i+1], my_list[i+2])

print("\n177")
my_list = ["가", "나", "다", "라"]
for i in range(len(my_list)-1, 0, -1):
    print(my_list[i], my_list[i-1])
# 뒤에서부터 불러올 때!!!
# range 안에는 인덱스 범위 지정

print("\n178")
my_list = [100, 200, 400, 800]
for i in range(0,3):
    print(my_list[i+1]-my_list[i])

print("\n179")
my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(0, 4):
    print((my_list[i]+my_list[i+1]+my_list[i+2]) / 3)
    print(sum(my_list[i:i+3]) / 3)
# abs(): 절대값 구하는 함수
# for i in range(1, len(my_list) - 1):
#     print(abs(my_list[i-1] + my_list[i] + my_list[i+1]) / 3)

print("\n180")
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

# 자료 구조 밖에다가 선언
volatiliy = []
for i in range(len(low_prices)):
    volatiliy.append(high_prices[i] - low_prices[i])
print(volatiliy)

# 180~200 해야 됨
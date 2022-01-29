from turtle import right


print("\n101")
print(type(True))

# 비교연산자, 논리연산자의 값은 T 또는 F
print("\n102")
print(3 == 5)
print("False")
print(type(3==5))

print("\n103")
print(3 < 5)

print("\n104")
x = 4
print(1 < x < 5)

print("\n105")
print ((3 == 3) and (4 != 3))
# and 연산자는 둘 다 참이어야 참
# or 연산자는 둘 중 하나만 참이어도 참

print("\n106")
print(3 >= 4)
# 등호는 무조건 오른쪽

print("\n107")
if 4 < 3:
    print("Hello World")

print("\n108")
if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")
    
print("\n109")
if 1 :
    print ("1")
    print ("2")
else :
    print("3")
print("4")
# if 뒤 조건은 참 거짓만 판단
# 여기서 True는 bool 결과로 보면 된다
# True = 1 , False = 0, (나머지 숫자는 다 참)
# 빈 문자열, 빈 리스트, None, 0은 거짓
print(True + True + True)
print(bool(""))
print(bool(None))

print("\n110")
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")

#input() 표준 입력: 키보드로 받음, str로 들어옴
#print() 표준 출력: 모니터로 출력
print("\n111")
odo = input()
print(odo * 2)

print("\n112")
odo = input("입력하세요 >> ")
odo = int(odo)
print(odo + 10)

# % = 나머지를 반환해주는 연산자
print("\n113")
odo = int(input("숫자 입력 >> "))
if odo % 2 == 1:
    print("홀수")
else:
    print("짝수")

print("\n114")
user = int(input()) + 20
if user > 255:
    print(255)
else:
    print(user)

# user = input()
# print(min(int(user) + 20, 255))

print("\n115")
user = int(input()) - 20
if user < 0:
    print(0)
elif user > 255:
    print(255)
else:
    print(user)

print("\n116")
user = input(">> 현재시간:")
if user.endswith("00"):
    print("정각입니다")
else:
    print("정각이 아닙니다")

time = input("현재시간: ")
if time[-2:] == "00":
    print("정각 입니다.")
else:
    print("정각이 아닙니다.")

hour = time[:2]
minute = time[-2:]

# 리스트에 있는지 확인하는 연산자 in
print("\n117")
fruit = ["사과", "포도", "홍시"]
user = input("좋아하는 과일은? ")
if user in fruit:
    print("정답입니다")
else:
    print("오답입니다")

print("\n118")
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
user = input("투자 종목")
if user in warn_investment_list:
    print("투자 경고 종목입니다")
else:
    print("투자 경고 종목이 아닙니다")

# 딕셔너리는 in 하면 키값 비교함
print("\n119")
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("제가 좋아하는 계절은: ")
if user in fruit:
    print("정답입니다")
else:
    print("오답입니다")

# dict.values()로 값을 가져올 수 있다
print("\n120")
user = input("좋아하는 과일은? ")
if user in fruit.values():
    print("정답입니다")
else:
    print("오답입니다")

# islower() 문자의 소문자 여부 판별 T, F 출력
# upper(), lower()
print("\n121")
user = input("알파벳 입력: ")
if user.islower():
    print(user.upper())
else:
    print(user.lower())

print("\n122")
user = int(input("score: "))
if 100>= user > 80:
    print("grade is A")
elif user > 60:
    print("grade is B")
elif user > 40:
    print("grade is C")
elif user > 20:
    print("grade is D")
else:
    print("grade is E")
# 더 높은 수 조건으로 안 적어줘도 동작한다
# 근데 명시적으로 하는 게 더 정확함

print("\n123")
user = input("입력: ")
user = user.split(" ")

if user[1] == "달러":
    print(int(user[0]) * 1167, "원")

elif user[1] == "엔":
    print(int(user[0]) * 1.096, "원")

else:
    print(int(user[0]) * 171, "원")

환율 = {"달러": 1167, 
        "엔": 1.096, 
        "유로": 1268, 
        "위안": 171}
user = input("입력: ")
num, currency = user.split()
print(float(num) * 환율[currency], "원")

# variable1, variable2 = user.split()
# 나뉜 값 차례대로 담긴다

print("\n124")
number1 = int(input())
number2 = int(input())
number3 = int(input())
print(max(number1, number2, number3))

num1 = input("input number1: ")
num2 = input("input number2: ")
num3 = input("input number3: ")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num1 and num2 >= num3:
    print(num2)
else:
    print(num3)

print("\n125")
user = input()
telecom = {"011":"SKT", "016":"KT", "019":"LGU", "010":"알수없음"}
a, *b = user.split("-")
print(telecom[a])
# 딕셔너리의 키값을 넣으면 value를 출력한다!!

print("\n126")
user = input()
if 2 >= int(user[2]) >= 0:
    print("강북구")
elif 5 >= int(user[2]) >= 3:
    print("도봉구")
else:
    print("노원구")

우편번호 = input("우편번호: ")
우편번호 = 우편번호[:3]
if 우편번호 in ["010", "011", "012"]:
    print("강북구")
elif 우편번호 in ["014", "015", "016"]:
    print("도봉구")
else:
    print("노원구")

print("\n127")
user = input()
a, b= user.split("-")
user = int(b[0])
if user == 1 or user == 3:
    print("남자")
else:
    print("여자")

print("\n128")
user = input()
a, b= user.split("-")
user = b[1:3]
if user in ["00", "01", "03", "04", "05", "06", "07", "08"]:
    print("서울입니다")
else:
    print("서울이 아닙니다")
# 00, 01, 02 숫자로 하면 그냥 0, 1, 2 된다

주민번호 = input("주민등록번호: ")
뒷자리 = 주민번호.split("-")[1]
if 0 <= int(뒷자리[1:3]) <= 8:
    print("서울입니다.")
else:
    print("서울이 아닙니다.")

print("\n129")
user = input()
a, b = user.split("-")
a = list(map(int, list(a)))
b = list(map(int, list(b)))
number = ((a[0])*2 + a[1]*3 + a[2]*4 + a[3]*5 + a[4]*6 + a[5]*7 + b[0]*8 + b[1]*9 + b[2]*2 + b[3]*3 + b[4]*4 + b[5]*5)
if b[6] == 11 - (number & 11):
    print("유효한 주민번호입니다")
else:
    print("유효하지 않은 주민번호입니다")

print("\n130")
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
hello = int(btc["opening_price"]) + int(btc["max_price"]) - int(btc["min_price"])
if hello > int(btc["max_price"]):
    print("상승장")
else:
    print("하락장")
print("\n201")
def print_coin():
    print("비트코인")

print("\n202")
print_coin()

print("\n203")
for i in range(100):
    print_coin()

print("\n204")
def print_coins():
    for i in range(100):
        print("비트코인")

print("\n205")
def hello():
    print("Hi")

hello()

print("\n206")
def message() :
    print("A")
    print("B")

message()
print("C")
message()

print("A", "B", "C", "A", "B")

print("\n207")
print("A")

def message() :
    print("B")

print("C")
message()

print("A, C, B")

print("\n208")
print("A")
def message1() :
    print("B")
print("C")
def message2() :
    print("D")
message1()
print("E")
message2()

print("A", "C", "B", "E", "D")

print("\n209")
def message1():
    print("A")

def message2():
    print("B")
    message1()

message2()

print("B", "A")

print("\n210")
def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()

print("B", "C", "B", "C", "B", "C", "A")
# for문 밖에 있는 message1()은 한 번 출력

print("\n211")
def 함수(문자열) :
    print(문자열)

함수("안녕")
함수("Hi")

print("안녕", "Hi")

print("\n212")
def 함수(a, b) :
    print(a + b)

함수(3, 4)
함수(7, 8)

print(7, 15)

print("\n213")
# 함수 정의할 때 파라미터 썼으면 꼭 채워줘야 함

print("\n214")
# 문자열과 숫자는 더할 수 없음
# 문자열은 곱하기(여러 번 쓰기)만 가능

print("\n215")
def print_with_smile(smile):
    print(smile+":D")

print_with_smile("안녕")

print("\n216")
print_with_smile("안녕하세요")

print("\n217")
def print_upper_price(price):
    print(price * 1.3)

print_upper_price(1000)

print("\n218")
def print_sum(a, b):
    print(a+b)

print_sum(1, 2)

print("\n219")
def print_arithmetic_operation(a, b):
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")

print_arithmetic_operation(5, 1)

print("\n220")
def print_max(a, b, c):
    max_val = 0
    if a > max_val:
        max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    print(max_val)
print_max(7, 10, 3)
# if문 3개로 max_val에 값을 계속 바인딩하면서 비교

print("\n221")
def print_reverse(string):
    print(string[::-1])

print_reverse("안녕하세요")

print("\n222")
def print_score(score_list):
    hap = 0
    for i in score_list:
        hap += i
    print(hap / len(score_list))
print_score([1, 2, 3])
# 수행할 기능 다 def 안에 적기
# def, for 어디까지 걸리는지 보기 (인덴트 안까지)
# 문제 조건 잘 보기

print("\n223")
def print_even(even_list):
    for i in even_list:
        if i % 2 == 0:
            print(i)
print_even([1, 3, 2, 10, 12, 11, 15])
# 리스트 선언 안 해도 리스트로 만들어줌
# str 또는 데이터 집합만 반복문 가능
# 순서가 없는 set은 반복문 못 돌림
# str은 첫 글자부터

print("\n224")
def print_keys(mydict):
    for keys in mydict.keys():
        print(keys)
print_keys ({"이름":"김말똥", "나이":30, "성별":0})

print("\n225")
my_dict = {"10/26" : [100, 130, 100, 100], "10/27" : [10, 12, 10, 11]}
def print_value_by_key(my_dict, key):
    print(my_dict[key])
print_value_by_key(my_dict, "10/26")

print("\n226")
def print_5xn(string):
    print(string[:5])
    print(string[5:])

def print_5xn2(string):
    i = 0
    while i < len(string):
        # print(string[i: min(i + 5, len(string))])
        print(string[i:i+5])
        i += 5
        # 우와 왜 에러 안 나지 신기
        # 변수의 기능을 정확히 알아야 함

print_5xn("아이엠어보이유알어걸")
print_5xn2("아이엠어보이유알어걸아이엠어보이유알어걸아이엠어보이유")

def print_mxn(string, num):
    i = 0
    while i < len(string):
        print(string[i:i+num])
        i += num
print_mxn("아이엠어보이유알어걸", 3)
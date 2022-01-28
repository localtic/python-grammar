"""
    파이썬 변수
    1. 정수 Integer -> int
        - 1, 3, 1000, -89, 0
    2. 실수 floating point -> float
        - 1.99, 0.001, 1.0
    3. 문자열 string -> str
        - "김현지는 파이썬 천재", "이세계에서는 마케팅 직원인 내가 여기서는 파이썬 천재?!"
    4. 진리값(참거짓) boolean -> bool
        - True, False
    
"""

# 바인딩: 변수에 값을 넣는 과정
print("\n011")
삼성전자 = 50000
print("삼성전자 10주의 가격은", 삼성전자 * 10, "원", sep='')

print("\n012")
시가총액 = 298_000_000_000_000
현재가 = 50000
PER = 15.79
print("시가총액은",시가총액,"현재가는",현재가,"PER는",PER)

print("\n013")
s = "hello"
t = "python"
print(s,"!", sep='', end=' ')
print(t)
# print(s+"!", t)

print("\n014")
print(2+2*3)


# 변수의 자료형을 알기 위해서 type()
print("\n015")
a = "132"
print(type(a))

# 자료형은 형변환함수로 사용할 수 있다
print("\n016")
num_str = "720"
# num_int = int(num_str)
# print(num_int+1, type(num_int))
print(type(int(num_str)))

print("\n017")
num = 100
print(type(str(num)))

print("\n018")
a = "15.79"
print(type(float(a)))

print("\n019")
year = "2022"
year = int(year)
print(year, year-1, year-2)

print("\n020")
air_cost = 48584 * 36
print(air_cost)

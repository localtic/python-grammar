# 리스트: 순서가 있지만 수정 불가능한 자료 구조

print("\n071")
# list: []
# tuple: ()
# dictionary: {}
# set: {}
# 문자열: "", ''
# 튜플 리스트 직접 선언하거나 자료 형태로 호출 가능
my_variable = tuple()
my_variable = ()
print(my_variable, type(my_variable))

print("\n072")
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
print(movie_rank)

print("\n073")
number = (1, ) # 튜플은 값이 하나만 들어가면 헷갈려해서 , 해줘야 함
print(number, type(number))

print("\n074")
# t = (1, 2, 3)
# t[0] = 'a'
# 튜플은 수정이 안 돼서 할당도 안 됨

print("\n075")
t = 1, 2, 3, 4
print(type(t))
# 튜플은 괄호 없이도 동작한다

print("\n076")
t = ('a', 'b', 'c')
t = ('A', 'b', 'c')
print(t, type(t))

print("\n077")
interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = list(interest)
print(type(interest), interest)

print("\n078")
interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest = tuple(interest)
print(type(interest), interest)

print("\n079")
# a, b, c = 10, 20, 30
# a -> ?
# a, b, c = [10, 20, 30]
# a -> ?
temp = ("apple", "banana", "cake")
a, b, c = temp
print(a, b, c)

# =: 할당 연산자 
# 우측에 있는 값을 좌측에 할당하는 연산자

# range(): 어떠한 반복자(iterator)를 생성하는 함수
# 반복자: 순회가 가능한 자료구조
# range(시작, 끝+1, 간격)
print("\n080")
print(tuple(range(2, 99, 2)))

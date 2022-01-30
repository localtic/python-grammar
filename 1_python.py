# 한줄주석
# crtl + / 주석처리

# print() 화면에 출력하는 함수
# 함수를 호출하기 위해서는 ()괄호를 반드시 붙여야함
# 함수호출방법: 함수이름()
# 문자열: "", '', """ """, r"", f""
print("\n001")
print("Hello World") # print('Hello World')

print("\n002")
print("Mary's cosmetics")

print("\n003")
print('신씨가 소리질렀다. "도둑이야".')

# 큰따옴표 작은따옴표는 반대로 감싼다

print("\n004")
print('"C:\Windows"')

print("\n005")
print("안녕하세요.\n만나서\t\t반갑습니다.")

#\n 줄 바꿈 \t 탭(스페이스4)

print("\n006")
print("오늘은", "일요일")

#,로 열거하는데 띄어쓰기는 아무리 해도 1번만 된다
# : 콜론
# ; 세미콜론

print("\n007")
print("naver;kakao;sk;samsung")
print("naver", "kakao", "sk", "samsung", sep="*")
#sep로 열거 방식을 정할 수 있다

print("\n008")
print("naver","kakao","sk", "samsung", sep="/")

print("\n009")
print("first", end='')
print("second")
# end는 코드 실행 후 어떤 상태로 끝낼지 결정하는 인자 
# ;로 한 줄에서 구분되는데 잘 안 씀

print("\n010")
print(5/3)
print("5/3=",5/3, sep='')
# 계산은 파이썬이 해준다

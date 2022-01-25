print("\n021")
# 인덱싱 = 특정 위치의 값을 추출하는 것(문자열, 배열...)
# []
letters = "python"
# p t
print(letters[0], letters[2])

# 슬라이싱: 특정 범위의 값들을 추출하는 것
# [시작위치: 끝위치: 간격] [시작인덱스:끝인덱스:오프셋]
# 시작위치: 생략 -> 처음부터
# 끝위치: 생략 -> 끝까지
# 간격: 생략 -> 1
# 주의할 점) 끝위치는 포함하지 않는다.(포함하려면 끝위치 비워둬야 함)
# 인덱스 규칙
# 처음부터: 0, 1, 2, 3, ...
# 끝부터: ..., -3, -2, -1

print("\n022")
license_plate = "24가 2210"
print(license_plate[-4:])

print("\n023")
string = "홀짝홀짝홀짝"
print(string[::2])

print("\n24")
string = "PYTHON"
print(string[::-1])
# 끝위치에 적는건 포함안된다

print("\n025")
phone_number = "010-1111-2222"
print(phone_number[0:3],phone_number[4:8],phone_number[-4:])
# replace(): 문자열 치환
# replace(원래값, 바꿀값)
phone_number = phone_number.replace("-", " ")
print(phone_number)
# replace는 문자열이 쓸 수 있는 함수!

print("\n026")
phone_number = phone_number.replace(" ", "")
print(phone_number)

print("\n027")
url = "http://sharebook.kr"
print(url[-2:])
url_split = url.split('.')
print(url_split[-1])
#split는 입력한 기준을 중심으로 범위로 구분됨
#return값이 있는 애들은 변수에 할당

print("\n028")
lang = "python"
# lang[0] = "P"
print(lang)
new_lang = "P" + lang[1:]
# 문자열은 할당(item assignment)을 지원하지 않기 때문에 수정 불가능, 슬라이싱 활용

print("\n029")
string = 'abcdfe2a354a32a'
string = string.replace("a", "A")
print(string)

print("\n30")
# 리턴값을 받아주지 않으면 변경된 거 안 보임

print("\n031")
a = "3"
b = "4"
print(a + b)
# Ctrl + Alt + 화살표 위나 아래 하면 커서 늘릴 수 있음
# Ctrl + D 여러개 선택
# Ctrl + H 모든 글자 변경 시 사용

print("\n032")
print("Hi" * 3)
# 문자열 곱하기는 반복

print("\n033")
print("-" * 80)

print("\n034")
t1 = 'python'
t2 = 'java'
t3 = t1 + " " + t2 + " "
print(t3 * 4)

# 문자열 포맷팅 -> 문자열에 변수를 넣어서 출력하는 방법
# f-string
# .format
# % formatting -> 값의 데이터형에 따라서 포맷팅 방식이 달라진다.
# 정수는 %d / 문자열은 %s / 실수는 %f

# % formatting
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
문장 = "이름: %s 나이: %d"
print(문장 % (name1, age1))

# .format
# {} 안에 변수
문장 = "이름: {} 나이: {}"
print(문장.format(name1, age1))

# f-string
# f""
# {변수}
# 재사용성이 낮음
문장 = f"이름: {name1} 나이: {age1}"
print(문장)

print("\n036")
문장 = "이름: {} 나이: {}"
print(문장.format(name1, age1))
print(문장.format(name2, age2))

print("\n037")
print(f"이름:{name1} 나이:{age1}")
print(f"이름:{name2} 나이:{age2}")

print("\n038")
상장주식수 = "5,969,782,550"
상장주식수 = 상장주식수.replace(",", "")
print(int(상장주식수))

print("\n039")
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])
print(분기.split("(")[0])
# 원본을 사용하려면 재할당

# str.strip : 좌우에 입력한 문자를 없앤다.
# str.rstrip : 우측에 입력한 문자를 없앤다.
# str.lstrip : 좌측에 입력한 문자를 없앤다.
# 입력값이 없으면 공백을 없앤다.
print("\n40")
data = "   삼성전자    "
data1 = data.strip()
print(data1)

data2 = data.rstrip()
print(data2)

print("\n041")
ticker = "btc_krw"
ticker1 = ticker.upper()
print(ticker1)

print("\n042")
ticker2 = ticker1.lower()
print(ticker2)

print("\n043")
문자열 = "hello world"
문자열 = 문자열.capitalize()
print(문자열)

print("\n044")
file_name = "보고서.xlsx"
is_endswith_xlsx = file_name.endswith("xlsx")
print(is_endswith_xlsx)
# 참거짓 판별할 때는 is_로 이름지음

print("\n045")
is_endswith = file_name.endswith(("xlsx", "xls"))
print(is_endswith)
# 튜플은 ()로 묶는다

print("\n046")
file_name = "2020_보고서.xlsx"
is_startswith_2020 = file_name.startswith("2020")
print(is_startswith_2020)

print("\n047")
a = "hello world"
print(a.split())
# 공백은 " " 이렇게 안 해도 기본값()이 공백으로 처리됨

print("\n048")
ticker = "btc_krw"
print(ticker.split("_"))

print("\n049")
date = "2020-05-01"
date = date.split("-")
날짜 = f"연:{date[0]}\n월:{date[1]}\n일:{date[2]}"
print(날짜)
# date.split('-')를 바로 연월일 값에 넣어도 됨, 그럼 위에서 나누면 안 됨

print("\n050")
data = "039490     "
data = data.rstrip()
print(data)

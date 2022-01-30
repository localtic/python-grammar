print("\n131")
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
    print(변수)
# 리스트에 들어 있는 문자열이 한 라인에 하나씩 출력

print("\n132")
과일 = ["사과", "귤", "수박"]
for 변수 in 과일:
    print("###")
# for문: 들여쓰기된 코드(print() 부분)가 자료구조에 저장된 데이터 개수만큼 반복

print("\n133")
for 변수 in ["A", "B", "C"]:
    print(변수)

print("A");print("B");print("C")

print("\n134")
for 변수 in ["A", "B", "C"]:
    print("출력:", 변수)

print("출력:", "A")
print("출력:", "B")
print("출력:", "C")

print("\n135")
for 변수 in ["A", "B", "C"]:
    b = 변수.lower()
    print("변환:", b)

print("변환:", "a")
print("변환:", "b")
print("변환:", "c")

print("\n136")
for i in [10, 20, 30]:
    print(i)

print("\n137")
for i in [10, 20, 30]:
    print(i)

print("\n138")
for i in [10, 20, 30]:
    print(i)
    print("-------")

print("\n139")
for i in ["++++", 10, 20, 30]:
    print(i)

print("\n140")
for i in [1, 2, 3, 4]:
    print("-------")

print("\n141")
list1 = [100, 200, 300]
for i in list1:
    print(i+10)

print("\n142")
리스트 = ["김밥", "라면", "튀김"]
for i in 리스트:
    print("오늘의 메뉴:", i)

print("\n143")
리스트 = ["SK하이닉스", "삼성전자", "LG전자"]
print(len(리스트[0]))

for 값 in 리스트:
    print(len(값))
# i -> "SK하이닉스", "삼성전자", "LG전자"

# for i in range(3):
# range(0, 끝, 1) =  range(끝)
# list(range(0, 10, 2)) = [0, 2, 4, 6, 8] 끝 포함 X
# range는 generator를 만든다
# generator는 iterator를 생성한다
# iterator 반복자, 컨테이너에서 각 요소를 하나씩 꺼내 수행하는 객체
# 컨테이너 = list, tuple, set, str, dict
print(list(range(0, 10, 2)))
for i in range(len(리스트)):
    print(len(리스트[i]))


# enumerate() 인덱스와 값을 함께 반환
for 인덱스, 값 in enumerate(리스트):
    print(인덱스, 값)

#len() = 글자수 세는 함수
print("\n144")
리스트 = ['dog', 'cat', 'parrot']
for i in 리스트:
    print(i, len(i))

# 인덱싱을 잊지 말자
print("\n145")
for i in 리스트:
    print(i[0])

print("\n146")
리스트 = [1, 2, 3]
for i in 리스트:
    print("3 x", i)
# 아니면 str(i)도 가능

print("\n148")
리스트 = ["가", "나", "다", "라"]
for i in 리스트:
    print()

# 슬라이싱 [::]
print("\n148")
list1 = ["가", "나", "다", "라"]
for i in list1[1:]:
    print(i)

print("\n149")
for i in range(0,3,2):
    print(list1[i])
print()
# for 변수 in 리스트[::2]:
# 간격만!


print("\n150")
for i in list1[::-1]:
    print(i)

# 줄어드는 간격은 -1로 적음
# for i in range(-1,-5,-1):
#     print(list1[i])
# 밑의 방법처럼 많이 씀
for i in range(len(list1) - 1, -1, -1):
    print(list1[i])


"""
    리스트 반복문 3가지
    array = [3, 2, 1, 4, 5]
    index, value
    
    1. 리스트 반복
    for value in array:
        print(value)
    
    결과: 3 2 1 4 5
    
    2. range
    -> range(시작, 끝(포함x), 간격)
    -> range(끝)
    for index in range(길이): 
        print(array[index]) # 길이 -> len(array)
    
    for index in range(len(array)):
        print(array[index])
    
    3. enumerate -> index와 value 둘다 반환
    for index, value in enumerate(array):
        print(index, value)
    # 0 3
    # 1 2
    # 2 1
    # 3 4
    # 4 5
    
    list(range(???))
    for i in range(10):
        print(i)
"""


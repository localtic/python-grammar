# 리스트: 순서가 있고 수정 가능한 자료 구조
# 시퀀스(sequence): 순서가 있다, 뮤터블(mutable): 수정 가능하다
# 리스트: mutable sequence data structure
# 튜플: immutable sequence data structure

print("\n051")
# 비어있는 리스트를 선언하는 방법
# list1 = list()
# list1 = []
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank)

print("\n052")
movie_rank.append("배트맨")
print(movie_rank)

print("\n053")
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)
# insert에 인덱스 번호 바로 적으면 됨

print("\n054")
movie_rank.remove("럭키")
print(movie_rank)

# del movie_rank[3]
# print(movie_rank)

print("\n055")
del movie_rank[2:]
print(movie_rank)
# 리스트에서 원소 제거하는 법: remove, del

print("\n056")
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
langs = list() # 리스트 선언 안 해도 리스트로 동작함
langs = lang1 + lang2
print(langs)

print("\n057")
nums = [1, 2, 3, 4, 5, 6, 7]
print("max: ", max(nums))
print("min: ", min(nums))
# max, min은 파이썬 자체에 존재하는 함수, 리스트에 귀속되는 것 아님

print("\n058")
nums = [1, 2, 3, 4, 5]
nums_plus = nums[0] + nums[1] + nums[2] +nums[3] + nums[4]
print(nums_plus)
#sum(nums), 리스트 안에 값들 다 더해줌

print("\n059")
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))
#len 리스트 원소나 문자열 길이 셈

print("\n060")
nums = [1, 2, 3, 4, 5]
average = sum(nums) / len(nums)
print(average)
# 나누기를 해서 소수점 첫째자리까지 보인다

print("\n061")
price = ['20180728', 100, 130, 140, 150, 160, 170]
del price[0]
print(price)
# print(price[1:]) 안 없애고 하는 방법

print("\n062")
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

print("\n063")
print(nums[1::2])

print("\n064")
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

print("\n065")
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

print("\n066")
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))
# join: 리스트를 문자열로 만드는 함수
# "연결방식".join(리스트)

print("\n067")
print("/".join(interest))

print("\n068")
print("\n".join(interest))

print("\n069")
string = "삼성전자/LG전자/Naver"
interest = string.split("/")
print(interest)

print("\n070")
data = [2, 4, 3, 1, 5, 10, 9]
# 정렬함수: sort(), sorted()
# list.sort() -> 원본을 정렬
# sorted(list) -> 원본은 그대로 두고, 정렬된 리스트(문자열)을 반환
# 오름차순: 기본
# 내림차순: list.sort(reverse=True)

data = sorted(data)
print(data)

print(sorted(data, reverse=True))
# 리스트를 먼저 넘겨주고 오름차순 내림차순 선택



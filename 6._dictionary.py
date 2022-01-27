#
print("\n081")
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, b, c = scores
print(valid_score)

# *valid_score, _, _= scores 안 쓸 거라서 이름 이렇게 해도 됨

print("\n082")
a, b, *valid_score = scores
print(valid_score)

print("\n083")
a, *valid_score, c = scores
print(valid_score)

# 딕셔너리의 자료형 dict()
# {key:value, key2:value2} -> dict1[key]
# set이라는 애도 중괄호 쓴다 -> {1, 3, 5, 10, 11}
# 딕셔너리도 set도 순서는 없지만 딕셔너리는 key로 인덱싱이 가능
print("\n084")
temp = dict()
print(type(temp), temp)

temp = {}
print(type(temp), temp)

print("\n085")
아이스크림 = {"메로나":1000, "폴라포":1200, "빵빠레":1800}
print(아이스크림)
#key값은 변할 수 없는 걸로 해야 함: 문자열, tuple

print("\n086")
# temp_list = []
# 리스트에서 값 추가 -> append()
# temp_list.append(10)
# print(temp_list)
# 
# 사전에서 값 추가 -> 사전["새로운키"] = 새로운값
아이스크림["죠스바"] = 1200
아이스크림["월드콘"] = 1500
print(아이스크림)

print("\n087")
print(f"메로나 가격: {아이스크림['메로나']}")
# "" '' 겹치지 않게 쓰기, 딕셔너리의 인덱싱은 키값으로 한다

print("\n088")
아이스크림["메로나"] = 1300
print(아이스크림)

print("\n089")
아이스크림.pop("메로나")
print(아이스크림)
# 딕셔너리 삭제방법 del, pop
# dict.pop(키)
# del dict[키]

print("\n090")
#icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
#icecream['누가바']
# 없는 거 불러오면 당연히 에러가 난다

print("\n091")
inventory = {"메로나": [300, 20], "비비빅": [400, 3], "죠스바": [250, 100]}
print(inventory)

# 1.
inventory: dict[str, dict] = {
    "메로나": {
        "가격": 300,
        "재고": 20
    },
    "비비빅": {
        "가격": 400,
        "재고": 3,
    },
    "죠스바": {
        "가격": 250,
        "재고": 100
    }
}

# 2.
inventory: list[dict] = [
    {
        "이름": "메로나",
        "가격": 300,
        "재고": 20
    },
    {
        "이름": "비비빅",
        "가격": 400,
        "재고": 3,
    },
    {
        "이름": "죠스바",
        "가격": 250,
        "재고": 100
    },
]

# 어떤 자료형인지 적는 거 3.6부터 됨

print("\n092")
inventory = {
    "메로나": [300, 20],
    "비비빅": [400, 3],
    "죠스바": [250, 100]
    }
print(f"{inventory['메로나'][0]}원")
print(str(inventory["메로나"][0]) + "원")
# print(inventory["메로나"][0], "원")

print("\n093")
재고 = "%d 개"
print(재고 % inventory["메로나"][1])

print("\n094")
inventory["월드콘"] = [500,7]
print(inventory)


print(); print()
# keys(), values(), items() 함수
# keys(): 사전의 키들을 iterator로 반환하는 함수
# values(): 사전의 값들을 iterator로 반환하는 함수
# items(): 사전의 키와 값의 쌍을 iterator로 반환하는 함수
# iterator: 순회할 수 있는 자료구조 -> 반복문에서 사용가능
examples = {
    "a": [1, 2, 3],
    "b": 100,
    "c": "this is c",
    "d": -9.999
}

print(examples)

# keys() -> 인덱싱하고 싶으면 리스트로 형변환해야한다.
print(examples.keys(), type(examples.keys()))
print(list(examples.keys()))
# for key in examples.keys():
#     print("this is", key)

# values()
print("examples.values(): ", examples.values())

# items()
print("examples.items(): ", examples.items())


print("\n095")
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(list(icecream.keys()))

print("\n096")
print(list(icecream.values()))

print("\n097")
icecream = list(icecream.values())
print(sum(icecream))
# sum(icecream.values())도 가능

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)
# 사전에서 데이터를 추가하는 함수는 .update()
# 반환값 None

print("\n099")
# result = {(keys):(vals)}
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
print(dict(zip(keys, vals)))
print(list(zip(keys, vals)))
# zip(keys, vals) 활용 가능

print("\n100")
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
print(dict(zip(date, close_price)))


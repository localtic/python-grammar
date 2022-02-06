N = 137
sum_list = 0

for i in str(N):
    sum_list += int(i)

print(sum_list)

def sum_(N):
    return sum([int(i) for i in str(N)])
print(sum_(137))

# list comprehension
# 리스트의 원소들을 쉽게 만들 수 있음
# [{리스트에 들어갈 원소} for {아이템, 데이터, 원소, 인덱스} in {범위, iterator}]
a = []
for i in range(10):
    a.append(i)
print(a)

a = [i for i in range(10)]
print(a)

# dict comprehension
# dict = {key: value for data in iterator}
a = {i: i*2 for i in range(10)}
print(a)

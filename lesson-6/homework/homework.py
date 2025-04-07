1.
listl = [1, 1, 2]
list2 = [2, 3, 4]
from collections import Counter

def uncommon_elements(list1, list2):
    count1 = Counter(list1)
    count2 = Counter(list2)

    result = []

    for elem in count1:
        if elem not in count2:
            result.extend([elem] * count1[elem])

    for elem in count2:
        if elem not in count1:
            result.extend([elem] * count2[elem])

    return result

list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2
print(result)

from collections import Counter

list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]


count1 = Counter(list1)
count2 = Counter(list2)

all_keys = set(count1.keys()).union(count2.keys())

result = []
for key in all_keys:
    diff = abs(count1[key] - count2[key])
    result.extend([key] * diff)

print(result)


2.
txt = input("Matn yozing: ") # Misol uchun

result = ""
i = 0

while i < len(txt):
    result += txt[i]
    
    # Unli harflar ro'yxati
    unli = 'aeiouAEIOU'
    
    # Har uchinchi belgi va oxirgi belgi emas
    if (i + 1) % 3 == 0 and i != len(txt) - 1:
        # Agar hozirgi belgi unli bo'lsa yoki undan oldin underscore qo'yilgan bo'lsa
        if txt[i] in unli or (len(result) > 1 and result[-2] == '_'):
            if i + 1 < len(txt):
                result += txt[i + 1]
                result += "_"
                i += 1  # Keyingi belgi oldindan qo'shilgani uchun i ni oshiramiz
            # Agar oxirgi belgi bo'lsa, hech narsa qo'shmaymiz
        else:
            result += "_"
    i += 1

print(result)





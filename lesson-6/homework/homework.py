1.
listl = [1, 1, 2]
list2 = [2, 3, 4]
dif Extend(list1, list2):
    list=list1.extend(list2)
    result list

list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2
print(result)


list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
dif Union(list1, list2):
    list=list1.union(list2)
    result list




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





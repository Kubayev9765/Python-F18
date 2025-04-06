1.
mevalar = ["Apple", "Banana", "Cherry", "Mango", "Orange"]
print(mevalar[2])  

2.
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
new_list = list1 + list2
print(new_list)

3.
my_list=[3,5 ,9,5,21,8,12,45,65]
Urta_index = len(my_list) // 2
Narija = [my_list[0], my_list[Urta_index], my_list[-1]]
print(Narija)

4.
kinolar = ["O'tgan kunlar", "Shaytanat", "Shum bola", "Navda", "Qashqirlar makoni"]
my_tupl=tuple(kinolar)
print(my_tupl)

5.
shaharlar = ["Samarqand", "Xorazm", "Paris", "Toshkent", "Parij"]
if "Paris" in shaharlar:
    print("Parij ro'yhatda mavjud!")
else:
    print("Parij ro'yhatda mavjud emas.")

6.
my_list = [1, 66, 2, 91,  3, 77, 4, 5]
my_list_2 =my_list.copy() 
print(my_list_2)

7.
my_list = [1, 66, 2, 91,  3, 77, 4, 5]
if len(my_list)>1:
    my_list[0], my_list[-1]=my_list[-1], my_list[0]
    print(my_list)
else:
  print(my_list)

8.
my_tupl=(1, 2, 3, 4, 5, 6, 7, 8, 9, 11)
tupl=my_tupl[3:8]
print(tupl)

9.
ranglar=["oq", "qizil", "ko'k", "sariq", "ko'k"]
kuk_rang=ranglar.count("ko'k")
print(kuk_rang)

10.
animals = ("tiger", "elephant", "lion", "zebra", "giraffe")
lion_index = animals.index("lion")
print(lion_index)

11.
tuple1 = (9, 22, 35)
tuple2 = (43, 55, 69)
umumiy_tuple = tuple1 + tuple2
print(umumiy_tuple)

12.
my_list = [14, 43, 2, 54, 33, 45, 52]
my_tuple = (15, 65, 27, 76, 39, 40)
list_length = len(my_list)
tuple_length = len(my_tuple)
print(list_length, tuple_length)

13.
my_tuple=(43, 56, 87, 93, 100)
my_List=list(my_tuple)
print(my_List)

14.
eng_kattasi = max(my_tuple)
eng_kichigi = min(my_tuple)
print("Eng katta qiymat: ", eng_kattasi)
print("Eng kichik qiymat: ", eng_kichigi)

15.
cars_tuple = ("Merccedes", "BMW", "Audi", "Porsha")
reverse_car = tuple(reversed(cars_tuple))
print(reverse_car)









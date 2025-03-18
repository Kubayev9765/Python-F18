1. Sort a Dictionary by Value
my_list=[9,7,3,4,1,2]
my_list=sorted(my_list)
print(my_list)

2. Add a Key to a Dictionary

my_dic={0: 10, 1: 20}
my_dic[2]=30
print(my_dic)

3. Concatenate Multiple Dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

my_dic=dic1.update(dic2)
dic1.update(dic3)
print(dic1)

4. Generate a Dictionary with Squares
my_dic={1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

for dic in my_dic.items():
        (x,y)=dic
        print(x,':',y)

5. Dictionary of Squares (1 to 15)
my_dic={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}


for dic in my_dic.items():
        (x,y)=dic
        print(x,':',y)


Set Exercises
1. Create a Set
my_set={320,32,23,24,1,3,5,100}
print(my_set)

2. Iterate Over a Set


3. Add Member(s) to a Set
my_set={320,32,23,24,1,3,5,100}
my_set.update([8,7,6])
print(my_set)

4. Remove Item(s) from a Set
my_set={320,32,23,24,1,3,5,100}
my_set.update([8,7,6])
print(my_set)
my_set.remove(100)
my_set.remove(320)
print(my_set)

5. Remove an Item if Present in the Set
my_set={320,32,23,24,1,3,5,100}
my_set.update([8,7,6])
my_set.discard(100)
my_set.discard(320)
my_set.discard(500)
print(my_set)


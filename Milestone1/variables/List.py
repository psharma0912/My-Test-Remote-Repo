#%%
username=['psharma','avyas', 'charvey', 'yanweilu']
print(type(username))
print(len(username))
print(type(username[0]))
print(len(username[-1]))
# %%
phrase1 = 'Clean Couch'
phrase2 = 'Giant Table'
if phrase1[0]==phrase2[0]:
    print('The strings start with the same letter')
else:
    print('They don\'t ')

# %%
my_string1 = 'This is a short phrase'
my_string2 = 'This is actually a significantly longer phrase than the previous one'
print(my_string1.split()[::-1])
print(' '.join(my_string1.split()[::-1]))
print(' '.join(my_string2.split()[::-1]))


# %%
lst1=[1,2,3,'python',3.4, (10,20,30)]
lst2=[0]*10
print(lst1)
print(lst2)
lst1.append(lst2)
print(lst1)
#4th element of list1 Nand list2
print(lst1[3])
print(lst2[3])
print(type((lst1[3],lst2[3])))
print(list((lst1[3],lst2[3])))

# %%
plate=["G06 WTR", "WL11 WFL", "QW68 PQR"]
for i in plate:
    print(i.split()[0][-2:])
print(type(i.split()[0][-2:]))
for i in plate:
    print(int(i.split()[0][-2:]))
print(type(i))

# %%
name_1='poonam sharma' 
name_2='ananya vyas'
print(set(name_1))
print(set(name_2))
''.join(set(name_1).intersection(set(name_2)))


# %%
x=['Hello', 'world']
for i in x:
    print(i.capitalize())
# %%
[i.capitalize() for i in x]
# %%
[i for i in range(101) if (i%5)==0]
# %%
#Use a dictionary comprehension to create a map between every 
# integer up to 15 and it's value squared
squares={i:i**2 for i in list(range(16))}
print(squares)

# %%
#Now, use a dictionary comprehension to create a dictionary that does the inverse! (hint: iterate over squares.items(), where squares is the
# name of the dict you made in the above challenge)
squares.items()
squares.keys()
squares.values()

# %%
towns = [{'name': 'Manchester', 'population': 58241}, 
         {'name': 'Coventry', 'population': 12435}, 
         {'name': 'South Windsor', 'population': 25709}]
print(type(towns))

print('The towns are:',[i['name'] for i in towns])

# print('Name of towns in the city are:',
#       [town['name'] for town in towns])
# print('Population of each town in the city are:',
#       [town['population'] for town in towns])

# %%

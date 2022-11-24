#%%
a = 42 
b = 25

def sum(a,b):
    return a+b
def diff(a,b):
    return a-b
def prod(a,b):
    return a*b
def div(a,b):
    return a%b

    
print(f' Sum is {sum(a,b)}')
print(f' Diff is {diff(a,b)}')
print(f' Product is {prod(a,b)}')
print(f' Division is {div(a,b)}')

a=4.2
print(type(a+b))
#because a is float so the addition is float
# %%
#Modulus operator
x=30
if x%3==0:
    print('% is modulus operator')
else:
    print('% is not a modulus operator')

# %%
#Normal and floor division
x=34
y=10
print(x/y)
print(x%y)
print(x//y)#integer value of the quotient
#%%
x=1 + 2 * 3 - 4 / 6 * (6 + 7) * 8 ** 9
print(x)
#%%
num1=37
num2=52
x=num1+num2
y=num1*num2
print(x)
print(y)


num1=8
num2=3
x=num1+num2
y=num1*num2
print(x)
print(y)
#%%
num = 23 
text_num = '57'
decimal_num = 98.3
print(type(num))
print(type(text_num))
print(type(decimal_num))
print(num+decimal_num)

print(dir(str))
x=[1,2,3,4,5]

# %%

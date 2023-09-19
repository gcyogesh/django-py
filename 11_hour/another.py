def greetings_function():
    print('welcome home yogesh')

greetings_function() 


def hero(name,age):
    
    print('helolo yogehs ' +name +'yo are not good '+ str(age))
name = input("enter your name:")    
age= input("enter your age")
hero(name, age)    



def yogesh_gg(*name):
    print('hello worrld '+name)
yogesh_gg("john","ram","sita")

def monkey_yg():

    return 5+4

print(monkey_yg())



def hero_yg(num1, num2):
    return num1+num2

print(hero_yg(44,22))



def not_yg():
    return 4+4

print(not_yg())

def hey_yg(pagal, pagall):
    return (pagal+pagall)
print(hey_yg(44,55))

def hency_yg(noo, yess):
    return noo+yess
noo=int(input("enter first number you want :"))
yess=int( input("enter second number you want :"))
print(hency_yg(noo, yess))

a= 43
b=43

if a==b:
    print(str(a) + 'is greater then' +str(b))
    
else:
    print('hello')


a='tim'
b='tim'

if a==b:
    print(str(a) + ' is equal to ', str(b))

a= True
b='tim'

if a== True:
    print('a is true')
    
    
    
a=4
b=6
if a>=b:
    print("You are correct")   
elif a<=b:
    print("YOu are not correct") 
    
else:
    print('leave it')    


value = input("Enter a  value :")


if type(value)== str:
    print(value + 'is a string')
elif type(value)== int:
    print(value ='is a interger')    
elif type(value)== list:
    print(value +' is a list')  

else:
    print('We don\'t know the data type of ' + value)    


value = int(input("enter a number:"))

if value%10 == 0:
    print(value, 'can be divided by 10')
else:
    print("it cannot be divided by 10")    



mydict = {
    'name': 'tim',
    'nationality':'nepal',
    'ghar':'nepal',
    'friends': ['peter', 'parker'],
}


# print((mydict))

x= mydict
print(x)


i =2
while i <6:
    print(i)
    # i= i+1
    i+=1
    

for i in range(6):
    print('hello world')
    
for letter in 'hello':
    print("letter")
    
mylist = ['jj','hh'] 

for i in mylist:
    print(i)
    
    
def hero_fun(yogesh):
    print('hello world'+ yogesh)    
hero_fun(hero_fun)
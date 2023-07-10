print('welcome back sohail')

complexNum = 2 + 3j
print(complexNum.imag)
print(complexNum.real)

list = ['sohail', 'data scientist', 12]
fun = 'sohail vadepav'
print(fun[5],fun[8],fun[7],fun[8],fun[9],fun[10])

#fun[5] = 'd' #immutable object

print('ask 1 : what is your age?')
# age = int(input())

age = 9
if age >= 18 :
    print('Conrgatulations!')
elif age < 18:
    print('kya re bhik mangya')
else:
    print("please enter valid input")
    
i = 1
n = 20
while i < n :
    print(i)
    i += 1
    if i == 4:
        break
else:
    print('completed')
    
for list in list :
    print(list)
    
for i in range(1,100000,1):
    print(i,'love you Taslim...!!!')
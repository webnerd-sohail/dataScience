print('data structures')

str = "sohail vadapav"
#slicing in string

print(str[0:6])
print(str[:len(str)+1:3])
print(len(str))

print(str[::1]) #same output
print(str[::]) #same output

print(str[::-1])
print(str[2:13:-1]) #blank output
print(str[8:0]) #koi sense hain iss baat ki?
print(str[14::-1]) #this Make some sense
print(str[-1:-15:-1])
print(str[:-16:])
print(str[:-16:-2])
print(str[-14])

for char in str:
    if char == 'a':
        print(char)

print(str.find('a'))
print(str.find('sohail'))
print(str.count('a'))
print(str.upper())
print(str.title())
print(str.capitalize())

print(str + " centre")
       
        
    
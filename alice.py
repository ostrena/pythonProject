name = "alice"
print (name)

age = "17"
print (age)

print (5* 'alice')

a= input("сколько тебе лет")
print(a)
b=input ("Как тебя зовут?")
print(b)
print ("Привет", b)

age = int(input("Сколько тебе лет"))
if age < 17:
    print ("к такому ответу я не была готова")
elif age == 17:
    print ("наслаждайся юношескими годами...")
else:
    print ("оо, тебе на пенсию пора")

t="Alice"
print(t[2:-1])
print(t[::-1])
print(t[2::])
print(t[::])

long= input ('как тебя зовут')
f= len(long)
print (f)

Al=input("возраст")
g= int(Al)
summa=0
nesumma=1
while g>0:
    digit=g%10
    summa=summa+digit
    nesumma=nesumma*digit
    g=g//10
    print("сумма",summa)
    print("произведение",nesumma)


d= "name"
print(d.title())
print(d.lower())
print(d.upper())

while True:
    input_age = input("возраст")
    if not input_age.isnumeric():
        print("не число")
    elif not 0 < int(input_age) <= 150:
        print("a lot")
    else:
        print("ok")
        break

name= input("имя")

if all(x.isalpha() or x.isspace() for x in name):
    print("ok")
else:
    print("not ok")

j= int(input("Сколько будет 25+2*2?"))
if j==29:
    print("ok")
else:
    print("not ok")












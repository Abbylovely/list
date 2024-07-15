Weather="sunny"
if Weather=="sunny":
    print("a smiley face")
else:
    print("a sad face")
Age=int(input("what is your age? "))
if Age<=12:
    print("You are a kid")
elif Age<18:
    print("You are a teenager")
else:
    print("you are an adult")

for i in range(1,10,2):
    print(i)
print("even numbers between 20 to 30")
for i in range(20,31,2):
    print(i)
print("\n")
X=1
X=X+1
print(X)
Count=10
while Count<=10:
    print(Count)
    Count=Count+1
A=1
while A<=10:
    print(A)
    A=A+20
print("\n")
def greet(name):
    print("hi",name)
greet("Lauren")
greet("Abby")
print("\n")
def Add(number1,number2):
    print("Add=",number1+number2)
Add(5,9)
Add(10,9)
def Area(lenght,breath):
    area=lenght*breath
    print("Area=",area)
Area(2,10)


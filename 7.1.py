import turtle as tur
tur.shape('turtle')

b=50
a=input()
for i in range(len(a)):
    if a[i]=='l':
       tur.goto(-b, 0)
    elif a[i]=='r':
       tur.goto(b, 0)
    elif a[i]=='d':
       tur.goto(0, -b)
    elif a[i]=='u':
       tur.goto(0, b)
    elif a[i]=='+':
        tur.pendown()
    elif a[i]=='-':
        tur.penup()
tur.goto(0, 0)
input()


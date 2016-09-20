import turtle as tur
tur.shape('turtle')
ang=0

def cur_ang(a, ang):
    while ang!=a:
        tur.right(90)
        ang +=90
        if ang>360:
            ang -=360
    return ang
b=50
a=input()
for i in range(len(a)):
    if a[i]=='l':
        ang=cur_ang(180,ang)
        tur.forward(b)
    elif a[i]=='r':
        ang=cur_ang(360,ang)
        tur.forward(b)
    elif a[i]=='d':
        ang=cur_ang(90, ang)
        tur.forward(b)
    elif a[i]=='u':
        ang=cur_ang(270, ang)
        tur.forward(b)
    elif a[i]=='+':
        tur.pendown()
    elif a[i]=='-':
        tur.penup()
tur.goto(0, 0)
input()


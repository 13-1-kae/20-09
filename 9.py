import turtle as tur
tur.shape('turtle')

def draw_circle(r):
  u = 6
  dx= r * 3.14/180*u
  for i in range(700):
    tur.forward(dx)
    r = r + 0.1
    dx= r * 3.14/180*u
    tur.right(u)
draw_circle(15)
input()
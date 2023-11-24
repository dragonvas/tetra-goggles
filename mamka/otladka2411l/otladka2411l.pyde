'''
Снежана решила сделать простой проект —
четыре кругляша расходятся из цента
по четырём разным направлениям:
лево, право, верх и низ
'''


x1 = 0
y1 = 0
x2 = 0
y2 = 0

def setup():
    size(600,400)
    background(200,300,100)
    strokeWeight(20)
    stroke(255)

def draw():
    global x1, x2, y1, y2
    background(200,300,100)
    translate(300, 200)
    point(x1, 0)
    point(0, y1)
    point(x2, 0)
    point(0, y2)
    x1 = x1 + 1
    x2 = x2 - 1
    y1 = y1 + 1
    y2 = y2 - 1

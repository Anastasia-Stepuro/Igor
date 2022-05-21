f_y = 500
iz_x = 10
iz_y = 15
y = 300
x = 300
def setup():
    size (666,666)
    
def draw():
    global x, iz_x,iz_y,y,f_y
    background(74,161,229)
    stroke(255,0,0)
    strokeWeight(50)
    point(x,y)
    x = x + iz_x
    y = y + iz_y
    if y <= 0 or y >= 666:
        iz_y = -iz_y
    if x <= 0:
        iz_x = -iz_x
    if x >= 666:
        x = 300
        y = 300
    rectMode(CORNER)
    rect (600,f_y,10,100)
    if (600<x+25<610)and (f_y < y < f_y + 100):
        iz_x = -iz_x
def keyPressed():
    global f_y
    if (key == "w" or key == "W" or key == "ц" or key == "Ц") and f_y > 0 : 
        f_y = f_y - 10
    elif (key == "s" or key == "S" or key == "ы" or key == "Ы") and f_y + 100 <666:
        f_y = f_y + 10

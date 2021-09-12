# 绘制雪景，将分为三块来实现，1.绘画窗口；2。绘制雪花；3，绘制雪地
from turtle import *
from random import *

# 绘制窗口

setup(800, 600, None, None)
bgcolor('black')  # 设置背景颜色

# 绘制雪花
def drawsnow():
    """1.雪花形状
    2.雪花颜色：随机
    3.雪花位置：随机"""
    hideturtle()
    pensize(2)
    for i in range(80):
        r, g, b = random(), random(), random()  # rgb默认是0-1之间
        pencolor((r, g, b))
        penup()
        setx(randint(-350, 350))  # 设置起始位置
        sety(randint(1, 250))
        pendown()
        snowsize = randint(10, 14)  # 设置雪花大小
        snowshape = randint(8, 12) # 设置雪花片的片数
        # 具体绘制一朵雪花
        for i in range(snowshape):
            forward(snowsize)
            backward(snowsize)
            right(360/snowshape)
        
    
# 绘制雪地
def drawground():
    hideturtle()
    for i in range(300):
        pensize(randint(5, 10))
        x = randint(-400, 350)
        y = randint(-280, -1)
        r, g, b = -y/280, -y/280,-y/280
        pencolor(r, g, b)
        penup()
        goto(x, y)
        pendown()
        forward(randint(40, 100))


tracer(False) # 把绘制过程关闭        
drawsnow()
drawground()

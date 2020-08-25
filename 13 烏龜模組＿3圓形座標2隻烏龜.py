import turtle #(匯入烏龜)
Howard1 = turtle.Turtle() #創造烏龜為Howaqrt
Howard1.pensize(5)
Howard1.screen.reset() #清空話不#turtle.color()改色（不只１隻）
import turtle #(匯入烏龜)
Howard2 = turtle.Turtle() #創造烏龜為Howaqrt
#turtle.shape()改型（不只１隻）
#Howard1.color()改色（只有１隻）
#Howard1.shape()改型（只有１隻）
#Howard1.penup()無痕移動
#Howard1.pendown()
Howard1.color('green')
Howard1.shape('turtle')
Howard1.speed(10.5)
Howard1.penup()
Howard1.goto(0,0)#########座標1
Howard1.pendown()
i = 0
while i<360:
    Howard1.forward(1)
    Howard1.right(1)
    i = i+1  #以迴圈畫一個圓形
Howard1.penup()
Howard1.goto(80,0)############座標2
Howard1.pendown()
k = 0
while k<360:
    Howard1.forward(1)
    Howard1.right(1)
    k = k+1  #以迴圈畫一個圓形
Howard1.penup()             #######座標3
Howard1.goto(40,40*(3**0.5))#定位三源最高點連成正三角形，已定位座標準卻畫出，此正三角形邊常80，高20根號3
Howard1.pendown()
h = 0
while h<360:
    Howard1.forward(1)
    Howard1.right(1)
    h = h+1  #以迴圈畫一個圓形
  ################以下第二隻(Howard2)#################  
    
Howard2.color('red')
Howard2.shape('turtle')
Howard2.pensize(5)
Howard2.speed(10.5)
Howard2.penup()
Howard2.goto(80,0)#########座標1
Howard2.pendown()
a = 0
while a<360:
    Howard2.forward(1)
    Howard2.right(1)
    a = a+1  #以迴圈畫一個圓形
Howard2.penup()
Howard2.goto(160,0)############座標2
Howard2.pendown()
b = 0
while b<360:
    Howard2.forward(1)
    Howard2.right(1)
    b = b+1  #以迴圈畫一個圓形
Howard2.penup()               #######座標3
Howard2.goto(120,40*(3**0.5))#定位三源最高點連成正三角形，已定位座標準卻畫出，此正三角形邊常80，高20根號3
Howard2.pendown()
c = 0
while c<360:
    Howard2.forward(1)
    Howard2.right(1)
    c = c+1  #以迴圈畫一個圓形

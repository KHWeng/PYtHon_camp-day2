import turtle #(匯入烏龜)
Howard = turtle.Turtle() #創造烏龜為Howaqrt
Howard.screen.reset() #清空話不#turtle.color()改色（不只１隻）
#turtle.shape()改型（不只１隻）
#Howard.color()改色（只有１隻）
#Howard.shape()改型（只有１隻）
#Howard.penup()無痕移動
#Howard.pendown()
Howard.color('green')
Howard.shape('turtle')
Howard.speed(10.5)
Howard.penup()
Howard.goto(0,0)
Howard.pendown()
i = 0
while i<360:
    Howard.forward(1)
    Howard.right(1)
    i = i+1  #以迴圈畫一個圓形
Howard.penup()
Howard.goto(80,0)
Howard.pendown()
k = 0
while k<360:
    Howard.forward(1)
    Howard.right(1)
    k = k+1  #以迴圈畫一個圓形
Howard.penup()
Howard.goto(40,40*(3**0.5))#定位三源最高點連成正三角形，已定位座標準卻畫出，此正三角形邊常80，高20根號3
Howard.pendown()
h = 0
while h<360:
    Howard.forward(1)
    Howard.right(1)
    h = h+1  #以迴圈畫一個圓形

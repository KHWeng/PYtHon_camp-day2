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

i = 0
while i<360:
    Howard.forward(1)
    Howard.right(1)
    i = i+1  #以迴圈畫一個圓形
Howard.penup()
Howard.forward(75)
Howard.pendown()
k = 0
while k<360:
    Howard.forward(1)
    Howard.right(1)
    k = k+1  #以迴圈畫一個圓形
Howard.penup()
Howard.right(135)
Howard.forward(55)
Howard.right(45)
Howard.pendown()
h = 0
while h<360:
    Howard.forward(1)
    Howard.right(1)
    h = h+1  #以迴圈畫一個圓形

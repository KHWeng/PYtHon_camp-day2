import turtle #(匯入烏龜)
Howard = turtle.Turtle() #創造烏龜為Howaqrt
Howard.screen.reset() #清空話不
Howard.forward(100)
Howard.left(90)
Howard.forward(100)
Howard.left(90)
Howard.forward(100)
Howard.left(90)
Howard.forward(100)
Howard.left(90) #畫正方形
i = 0
while i<4:
     Howard.forward(100)
     Howard.right(90)
     i = i+1  #以迴圈畫另一個正方形
     

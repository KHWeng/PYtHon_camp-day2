import random
ans = random.randint(1,20)
i = 0
while i < 5:
    num = int(input('please type a number!'))
    if i==4 and num != ans :# 因為三一律，此判斷是應放在最上面！！
        print("You are faild") 
        print("正確答案是",ans)
    elif ans > num:
        print("你猜得太小")
    elif ans < num:
        print("你猜得太大")
    elif  ans == num:
        if i<3: #　i加了１才會是實際次數，所以i<3事實上是猜３次以內！！！！！！！
            print("你才花",i+1,"次就猜中了相當之厲害呀!!!會不會太沒救?！")
        else :
            print("你花了",i+1,"次才猜中欸！會不會太沒救?！")
        break
    i = i+1
    
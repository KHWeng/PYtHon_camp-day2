engscore = int(input("Enter your ENGLISH score Here:"))
mathscore = int(input("Enter your MATH score Here:"))
if (engscore>=90 and mathscore >=90)or (engscore == 100 or mathscore == 100):
    print ("恭喜得到獎學金!")
if (engscore<60 and mathscore <60)or (engscore == 0 or mathscore == 0):
    print ("感謝貢獻獎學金!")
if ((engscore<90 and engscore>=60) and (mathscore<90 and mathscore<60))or (engscore <60 or mathscore <60):
    print ("下次還有獎學金!")
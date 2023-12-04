# wap to check the grade according to the marks given b user 

# marks              grade
# >90                A 
# >80 and =>90       B 
# >=60 and <=80      C 
# below 60           D 

mk = int(input("Enter the marks obtained by Studen = "))
if(mk>90):
    print(f'Your Grade is "A" According to your {mk} marks.')
    print("Very Good Work, Maintain the highest score in future")
elif(80<mk<=90):
    print(f'Your Grade is "B" According to your {mk} marks.')
    print("Good Work, Maintain the score in future")
elif(60<=mk<=80):
    print(f'Your Grade is "C" According to your {mk} marks.')
    print("Fair Work, You have ability to obtain more marks")
    print("Keep it up")
else:
    print(f'Your Grade is "D" According to your {mk} marks.')
    print("Not a good Work, You have to work hard")
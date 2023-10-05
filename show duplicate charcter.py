str1=input ("enter the string")
val=""
for i in str1:
   if str1.count(i)>=2 and i not in val:
       val+=i
print (val)

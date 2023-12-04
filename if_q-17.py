'''
wap to check whether a character is vowel or not
'''

chr = (input("Enter the character: "))
vow = "aeiouAEIOU"
if chr in vow:
    print(f'{chr} is a vowel')
else:
    print(f'{chr} is not a vowel')
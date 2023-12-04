#Write a function to tell user if he/she is able to vote or not.
def vote_or_not(user_age):
    if(user_age>=18):
        return 'Yes, User can give vote.'
    else:
        return 'No, User cannot give vote.'
    
user_age = int(input("Enter your age: "))
vote = vote_or_not(user_age)

print(vote)
from string import ascii_letters,digits,punctuation
from random import choice,randint

welcome_message="""
    welcome to "strong password generator"
    
    in this App,you will enter your desired password
    length and then a random password of this length
    will be generated. this pass will cosists of 
    letters(upper and lower ),numbers and special
    characters.
    """
random_letter=1
random_digit=2
random_punctuation=3

print(welcome_message)

password_length=int(input("enter your desired password length:"))

password=""
for num in range (password_length):
    random_character=""
    option=randint(1,3)
    
    if option==1:
        random_character=choice(ascii_letters)
    elif option==2:
        random_character=choice(digits)
    elif option==3:
        random_character=choice(punctuation)
        
    password=password+random_character
    
print("your password is:",password) 

                    
    
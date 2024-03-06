#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HP
#
# Created:     04/03/2024
# Copyright:   (c) HP 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import time
import random
words = ["Matron","Abbacy","Carbon"]
nos = random.randint(0, 99)
nos_1 = random.randint(100,999)
# vowels_ = ["@","3","1","0","^"]
# vowels = ['a','e','i','o','u']
# A="@"
while True :
    print("This is a password maker")
    print("Here I will create an 8 digit password for you")
    pass_strength = input("How strong do you want your password to be ? (easy/hard) : ")
    if pass_strength == "easy" :
        random_pass = random.choice(words)
        password = random_pass + str(nos)
        print("Your password is "+ str(password) + ",make sure not to forget it!!")
        time.sleep(3)

    elif pass_strength == "hard" :
        randomPass= random.choice(words)
        if "a" and "o" in randomPass :
            new_pass = randomPass.replace("a","@")
            new_pass_1 = new_pass.replace("o","0") + str(nos_1)
            print("Your password is "+ str(new_pass_1) + ",make sure not to forget it!!")
            time.sleep(3)
    else :
        print("You might have entered something except easy or hard. Please try again")
        time.sleep(3)

    play_again = input("Do you Want create another password? (yes/no) : ")
    if play_again != "yes" :
        print("Thanks for using the password maker!")
        break








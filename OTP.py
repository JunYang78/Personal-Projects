import pyautogui
import time
import random

chars = "abcdefghijklmnopqrstuvwxyz"
chars_list = list(chars)

password = pyautogui.password("Enter a Password : ")

guess_password = ""

while(guess_password != password):
    guess_password = random.choices(chars_list, k=len(password))

    print("DECRYPTING"+ str(guess_password)+ "PASSWORD")

    if(guess_password == list(password)):
        print("Your password is : "+ "".join(guess_password))
        break
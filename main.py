import random
import string
import customtkinter as ctk
# User Number Input Is Taken First
#uni = input("Input the amount of letters your password shoud have: ")
#uni = int(uni)
uni = 10
#Initial Letter Select
randomlettersupperase = string.ascii_uppercase
randomletterslowercase = string.ascii_lowercase
randomnumbers = string.digits
#Functions For Lowercase & Uppercase
def generateLowerString():
    randomstringlower = ''.join(random.choices(randomletterslowercase + randomnumbers, k = uni)) # Lowercase random alphanumeric string
    print(f"Your randomly generated password is: {randomstringlower}")
    lowercase_output = ctk.CTkLabel(root, text=randomstringlower)
    lowercase_output.pack()    

def generateUpperString():
    randomstringupper = ''.join(random.choices(randomlettersupperase + randomnumbers, k = uni)) # Uppercase random alphanumeric string
    print(f"Your randomly generated password is: {randomstringupper}")
    uppercase_output=ctk.CTkLabel(root,text=randomstringupper)
    uppercase_output.pack()
# GUI THEMEING
ctk.set_default_color_theme("dark-blue")

# GUI 
root = ctk.CTk()
root.geometry("600x500")
main_title= ctk.CTkLabel(root,text="Password Generator")
main_title.pack()
button_lowercase = ctk.CTkButton(root , text="Generate Lowercase Password",command=generateUpperString)
button_lowercase.pack()
button_uppercase= ctk.CTkButton(root,text="Generate Uppercase Passowrd", command=generateLowerString)
button_uppercase.pack()
root.mainloop()

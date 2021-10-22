import random
import secrets 

#Master password
master_pass = "janides15!"

#choices
choices = {
  1: "Add a new password",
  2: "Get password",
  3: "Get website",
  4:"Change password"
}
#database
data_base = {

}

print(" Welcome to the Password Generator 2.0!")
print("Guaranteed to keep your passwords safe")
#Take the input from the user for the master password
enter_MP = input("Please enter the Master Password Now")

#is the Master password correct
if str(enter_MP) == master_pass:
  for key, value in choices.items():
    print(str(key) + ":" + value)
  choice_User = int(input("Enter the number next to the options: "))
  if choice_User == 1:
    new_website = input("What is the name of the website: ")
    if new_website in data_base:
      print("Website is already listed")
    else:
      new_password = secrets.token_hex(16)
      print(new_password)
      use_password = str(input("Do you want to use this password? yes or no "))
      if use_password == "yes":
        data_base[new_website] = new_password 
      elif use_password == "no":
        user_chosen_pass =str(input("Enter your own password"))
      


char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456$%@"

while 1:
  password_len = int(input("How long do you want your password to be?:  "))
  password_count = int(input("How many passwords would you like?: "))
  for x in range(0, password_count):
    password = ""
    for x in range(0,password_len):
      password_char = random.choice(char)
      password      = password + password_char
    print("Here's your password : ", password)



# Validate whether password contains
# alphabets and numbers
username=input("Enter user name: ")
password=input("Enter password: ")

user_alpha=False
user_digit=False

for ch in username:
    if ch.isalpha():
        user_alpha=True
    if ch.isdigit():
        user_digit=True
pass_alpha=False
pass_digit=False
for ch in password:
    if ch.isalpha():
        pass_alpha=True
    if ch.isdigit():
        pass_digit=True
if (username.isalnum() and password.isalnum() and pass_alpha and pass_digit):
    print("Valid Credentials")
else:
    print("Invalid Credentials")

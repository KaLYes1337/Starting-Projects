# Validate user input:
# 1.Username is no more than 12 character
# 2.Username must NOT contain any spaces
# 3.Username must NOT contain any digits

username = input("Please enter username: ")

if len(username) > 12:
    print("Username must be no more than 12 characters!")
elif username.isdigit() == False:
    print("Username must not contain any digits!")
elif username.count(" ") >= 1:
    print("Username must not contain any spaces")
else:
    print(f"Welcome {username}!")

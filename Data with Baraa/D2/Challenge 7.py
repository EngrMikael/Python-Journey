# 1. Check if the user's name is not empty and the age is greater than or equal to 18.
# 2. Check if the password is at least 8 characters long and does not contain spaces.
# 3. Check if the email contains the "@" symbol and ends with '.com'.
# 4. Check if the username is a string, is not None, and is less than 5 characters long.
# 5. Check if the user is either an admin or a moderator, and either they're not banned or they've verified their email.

user1 = ["Jhrt", "ThisIsMyPass", "22", "jhrtemail@gmail.com", "Eseng01", "Admin", True]        # verified = True
user2 = ["Duke", "ThisIsMyPass", "17", "dukeemail@gmail.com", "Dok22", "Moderator", False]    # verified = False

choice = input("Enter your username: ")

if choice == user1[4] or choice == user2[4]:
    password = input("Enter your password: ")

    # determine which user
    user = user1 if choice == user1[4] else user2

    if password == user[1]:
        name_valid = user[0] != "" and user[0] is not None
        age_valid = int(user[2]) >= 18
        password_valid = len(user[1]) >= 8 and " " not in user[1]
        email_valid = "@" in user[3] and user[3].endswith(".com")
        username_valid = isinstance(user[4], str) and user[4] is not None and len(user[4]) < 5
        role_valid = (
            user[5] in ["Admin", "Moderator"]
            and (user[6] or user[5] != "Banned")
        )

        print(f"""
Name valid: {name_valid}
Age valid: {age_valid}
Password valid: {password_valid}
Email valid: {email_valid}
Username valid: {username_valid}
Role valid: {role_valid}
Role: {user[5]}
        """)

    else:
        print("Access Denied: Incorrect Password")
else:
    print("Access Denied: Username Not Found")


# my original code for reference:
    
# user1 = ["Jhrt", "ThisIsMyPass", "22", "jhrtemail@gmail.com", "Eseng01", "Admin"]
# user2 = ["Duke", "ThisIsMyPass", "17", "dukeemail@gmail.com", "Dok22", "Moderator"]

# choice = input("Enter your username: ")

# if (choice == user1[4] or choice == user2[4]):
#     password = input("Enter your password: ")
#     if (choice == user1[4] and password == user1[1]):
#         print(f"Name: {user1[0] is not None}\nAge: {int(user1[2]) >= 18}\npassword: {len(user1[1]) >= 8}\nemail: {(user1[3].find('@')) is not 0}\nusername: {(isinstance(user1[4], str) and not None and int(len(user1) < 5)) is True}\nrole: {user1[5]}")
#     elif (choice == user2[4] and password == user2[1]):
#         print(f"Name: {user2[0] is not None}\nAge: {int(user2[2]) >= 18}\npassword: {len(user2[1]) >= 8}\nemail: {(user2[3].find('@')) is not 0}\nusername: {(isinstance(user2[4], str) and not None and int(len(user2) < 5)) is True}\nrole: {user2[5]}")
#     else:
#         print("Access Denied: Incorrect Password")
# else:
#     print("Access Denied: Username Not Found")




# hahahahaha i did not include .com, and verified 
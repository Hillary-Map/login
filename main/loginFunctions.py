import random


def information_update(userName, state):
    """to be used in logging function to make changes in each account
       for each login (copying all accounts and only updating that of userName
       Depending on state this method can also delete an account
    """
    if state == "update":
        with open("users.txt", 'r') as f:
            with open("users.txt", 'r+') as file1:
                for i in range(len(f.readlines())):
                    f.seek(0)
                    user_info = f.readlines()[i]
                    copy_line = "{} {} {} {} {} {}\n".format(user_info.strip().split(" ")[0], user_info.strip().split(" ")[1], user_info.strip().split(" ")[2],
                    user_info.strip().split(" ")[3], user_info.strip().split(" ")[4], user_info.strip().split(" ")[5])
                    #Updating

                    if user_info.strip().split(" ")[0] == userName:
                       current_userInfo = "{} {} {} {} {} {}\n".format(user_info.strip().split(" ")[0], user_info.strip().split(" ")[1],
                       user_info.strip().split(" ")[2], user_info.strip().split(" ")[3], user_info.strip().split(" ")[4], int(user_info.strip().split(" ")[5])+1)
                       file1.write(current_userInfo)

                    else:
                        file1.write(copy_line)
    elif state == "delete":
        with open("users.txt", "r") as mainFile:
            with open("userCopy.txt", "w") as file:
                # Copying all lines into a dummy txt file before deleting the
                # txt file
                for i in range(len(mainFile.readlines())):
                    mainFile.seek(0)
                    user_info = mainFile.readlines()[i]
                    copy_line = "{} {} {} {} {} {}\n".format(user_info.strip().split(" ")[0], user_info.strip().split(" ")[1], user_info.strip().split(" ")[2],
                    user_info.strip().split(" ")[3], user_info.strip().split(" ")[4], user_info.strip().split(" ")[5])
                    file.write(copy_line)

        with open("userCopy.txt", "r+") as file:
            with open("users.txt", "w") as mainFile:
                # restoring to the main file and deleting
                for i in range(len(file.readlines())):
                    file.seek(0)
                    user_info = file.readlines()[i]
                    copy_line = "{} {} {} {} {} {}\n".format(user_info.strip().split(" ")[0], user_info.strip().split(" ")[1], user_info.strip().split(" ")[2],
                    user_info.strip().split(" ")[3], user_info.strip().split(" ")[4], user_info.strip().split(" ")[5])
                    file.write(copy_line)
                    if user_info.strip().split(" ")[0] == userName:
                        print(f"{userName}'s account successfully deleted...")
                    else:

                        mainFile.write(copy_line)


def login():
    """Note we use a boolean Loop_continuation statement in order to
       activate the break while loop statement"""
    loop_continuation = True
    user_name = input("Enter your user name: ")
    if user_name.lower() == "q":
        print("Thanks for using Quatron systems...")
        loop_continuation = False
    else:
        password = input("Enter your password: ")
        with open("users.txt", 'r') as f:
            match = False
            # looping all the lines and checking credentials match
            for i in range(len(f.readlines())):
                f.seek(0)
                user_info = f.readlines()[i]
                if user_name == user_info.strip().split(" ")[3] and password == user_info.strip().split(" ")[4]:
                    match = True
                    break
            if match:
                print("Access granted....")
                print("Welcome "+user_info.strip().split(" ")[0]+" :)")
                #update
                information_update(user_info.strip().split(" ")[0], "update")
                user_status = input("perform your tasks\n x - to exit\n d - delete account")
                if user_status.lower() == "x":
                    loop_continuation = False
                    print("Thanks for using Quatron systems see you next time ...")
                elif user_status.lower() == "d":
                    #delete account
                    information_update(user_info.strip().split(" ")[0], "delete")
            else:
                print("Input error check your password and user name and retry.....")
    return loop_continuation


def create_account():
    """Note we use a boolean Loop_continuation statement in order to
       activate the break while loop statement"""
    loop_continuation = True
    key_value = random.randint(1000, 9999)
    print("Your assigned key Value= "+str(key_value))
    key = input("Enter your verification key: ")
    if key.lower() == "q":
        print("Thanks for using Quatron systems...")
        loop_continuation = False
    # Encryption key check
    elif key == str(key_value):
        name = str(input("Enter your first name: ")).strip()
        if name.lower() == "q":
            print("Thanks for using Quatron systems...")
            loop_continuation = False
        if loop_continuation:
            surname = str(input("Enter your surname: ")).strip()
            age = input("Enter your age: ").strip()
            user_name = str(input("Enter your User name: ")).strip()
            password = str(input("Enter your password: ")).strip()
            status = 0
            with open("users.txt", 'a') as f:
                user_info = "{} {} {} {} {} {}".format(name, surname, int(age), user_name, password, status)
                f.write(user_info+"\n")
                print("Account created successfully...")
                #break

    else:
        print("Invalid key Value! Try again...")

    return loop_continuation


def display():
    print("---------------------")
    with open("users.txt", "r") as f:
        for i in range(len(f.readlines())):
            f.seek(0)
            user_info = f.readlines()[i]
            display_string = "{} {} {}".format(str(user_info.strip().split(" ")[0]),
                                               str(user_info.strip().split(" ")[1]),
                                               str(user_info.strip().split(" ")[2]))
            print(display_string)
    print("----------------------")



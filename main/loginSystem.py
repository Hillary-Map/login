from loginFunctions import *
#################################

userExit = False
userChoice = "a"
#################################
while userChoice.lower() != "q" and not userExit:
    print("Welcome to Quatron Systems")
    userChoice = input("LogIn - press L\nCreate New Account - press N\nDisplay - d\nQuit - q\n")

    # Creating an Account
    if userChoice.lower() == "n":
        loop_continuation = create_account()
        if not loop_continuation:
            userChoice = "q"
            break
    # Logging in
    elif userChoice.lower() == "l":
        login_cont = login()
        if not login_cont:
            userChoice = "q"
            break

    elif userChoice.lower() == "q":
            print("Thanks for using Quatron systems...")
            break

    elif userChoice.lower() == "d":
        display()
    else:
        print("Unsupported input")
        break


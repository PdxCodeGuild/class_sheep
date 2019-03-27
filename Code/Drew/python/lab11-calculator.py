while True:
    user_in = input("Enter an arithmetic expression:\n")
    try:
        print(eval(user_in))
        break
    except:
        print("Try again.")
        continue

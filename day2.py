import re
def password_checker():
    print("Welcome to the Password Checker program\n")
    print("Remember to use lowercase letters, uppercase letters, symbols, numbers; length should be greater than 8")
    while True:
        s=str(input("\nEnter Password: "))
        #pattern=re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*()_\-]).{8,}$")
        if len(s)<8:
            print("Weak; length too small")
        elif not re.search(r"[a-z]", s):
            print("Weak: no lowercase letter used.")
        elif not re.search(r"[A-Z]", s):
            print("Weak: no uppercase letter used")
        elif not re.search(r"[0-9]", s):
            print("Weak: no number used")
        elif not re.search(r"[@#$%^&*()_!-]", s):
            print("Medium: can do better, use a special character!")

        #if pattern.search(s):
            #print("Strong! Well Done!")
        #    break
        #else: 
            #print("Weak Passowrd, meet all conditions.")
        else:
            print("Strong Password, well done!")
            break
password_checker()

    
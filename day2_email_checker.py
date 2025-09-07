import re
def email_checker():
    s=str(input("Enter email to check: "))
    pattern=re.compile(r"^[^\._](?!.*\.\.)[a-zA-Z0-9_\.)+@[a-zA-Z0-9\-]+(\.[a-z]{2,})+$")
    if pattern.search(s):
        print("Valid email")
    else:
        print("Invalid email")
email_checker()

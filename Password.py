print("Password Checking Functions")
password=input("Enter Password:")
def check_password(p):
    is_upper=False
    is_num=False
    is_digit=False
    if len(p)==8:
        for ch in password:
            if ch.isupper():
                is_upper=True
            elif ch.isdigit():
                is_digit=True
            elif not ch.isalnum():
                is_num=True
        return p
    else:
        print("Password must have 8 charachters")
set_password=check_password(password)
print(set_password)
import time as t

thin_line = "---" * 15
line = "━━━" * 15
thick_line = "===" * 15
count = 0
accounts = []

actions = (
    "===Actions===",
    "",
    "1 | Logout",
    "2 | Change Password",
    "3 | Change Username",
    "4 | Delete Account",
)

def error(msg):
    print(f"\n{thick_line}")
    print(msg)
    print(f"{thick_line}\n")
    
class Account:
    def __init__(self, user, password, age):
        self.user = user
        self.password = password
        self.age = age
    
    def login_info(self, user, password):
        print("Username:")
        print(user)
        
        print("\nPassword:")
        print(password)
    
while True:
    print("===Welcome===")

    if count != 0:
        print("\nNew User? (y/n)")
        new_user = input(" - ").strip().lower()
    
        while new_user not in ["y", "n"]:
            error("Answer with \"y\" for yes or \"n\" for no!")
        
            print("New User? (y/n)")
            new_user = input(" - ").strip().lower()

    else:
        error("Create an Account first!")
        new_user = "y"
    
    if new_user == "y":
        print(f"{line}\n")
        
        print("===Registrate===")
        
        print("\nUsername:")
        user = input()
        
        print(f"\n{thin_line}\n")
        
        while True:
            print("Password:")
            password = input()
            
            if not password:
                error("This can't be Empty!")
                continue
        
            print("\nConfirm Password:")
            confirm = input()
            
            if not confirm:
                error("This can't be Empty!")
                continue
                
            if password == confirm:    
                break
            
            else:
                error("Passwords don't Match!")    
                continue
            
        print(f"\n{line}\n")
        
        while True:
            try:
                print("Your Age:")
                age = int(input())
                print(f"\n{line}\n")
                break
                
            except ValueError:
                error("Input a Number!")    
        
        if age <= 5:
            error("You are too Young!")
            print(f"{line}\n")
            continue
        
        count += 1
        
        acc = Account(user, password, age)
        accounts.append(acc)

    else:
        print(f"\n{line}\n")
        
        print("===Login===")    
        
        print("\nUsername:")
        user = input()
        
        print("\nPassword:")
        password = input()
        
        for account in accounts:
            if user == account.user:
                if password == account.password:
                    error("Login Success!")
                    print(f"{line}\n")
                    
                    while True:
                        for listActions in actions:
                            print(listActions, flush = True)
                            t.sleep(0.05)
                        
                        action = input("\nAction: ").strip()
                    
                        while action not in ["1", "2", "3", "4"]:
                            error("Use the Numbers \"1-4\"!")
                        
                            action = input("Action:")
                            
                        print(f"\n{line}\n")
                    
                        if action == "1":
                            break
                        
                        if action == "2":
                            while True:
                                print("New Password:")
                                new_password = input()
                            
                                if new_password == account.password:
                                    error("The New Password can't be the Same as the Old One!")
                                    continue
                            
                                print("\nConfirm Password:")
                                confirm = input()
                            
                                if new_password == confirm:
                                    break
                                    
                                else:    
                                    error("Passwords don't Match!")
                        
                        if action == "3":
                            pass
                        
                        if action == "4":
                            pass
                        
                        print(f"\n{line}\n")    
                            
                else:
                    error("Invalid Info!")    
            else:
                error("Invalid Info!")
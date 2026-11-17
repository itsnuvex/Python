#Copy/Paste into external IDE (like Xed - Editor) for the best Experience

import random as r
import string as s
import time as t

thin_line = "---" * 15
line = "━━━" * 15
thick_line = "===" * 15
newPassword = "y"

def error(msg):
    print(f"\n{thick_line}")
    print(msg)
    print(f"{thick_line}\n")


while newPassword == "y":
    characters = s.ascii_letters + s.digits
    
    print("===Password Generator===")

    print("\nAdd Special Characters? (y/n)")
    special = input(" - ").strip().lower()

    while special not in ["y", "n"]:
        error("Answer with \"y\" for yes or \"n\" for no!")

        print("Add Special Characters? (y/n)")
        special = input(" - ").strip().lower()   

    if special == "y":     
        characters += s.punctuation

    print(f"\n{thin_line}\n")    

    print("How long should the password be? (5-100)")

    while True:
        try:
            length = int(input(""))

            if not 5 <= length <= 100:
                error("Number must be Between 5-100!")
                continue

            break
        except ValueError:
            error("Use Numbers only!")    

    print(f"\n{line}\n")

    for _ in range(length):
        print(r.choice(characters), end = "", flush = True) 
        t.sleep(0.1)

    print(f"\n\n{line}\n")    

    print("Generate New Password? (y/n)")
    newPassword = input(" - ").strip().lower()

    while newPassword not in ["y", "n"]:
        error("Answer with \"y\" for yes or \"n\" for no!")

        print("Generate New Password? (y/n)")
        newPassword = input(" - ").strip().lower()

    print(f"\n{line}\n")    
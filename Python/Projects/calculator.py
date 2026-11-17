#Copy/Paste into external IDE (like Xed - Editor) for the best Experience

import time as t

thin_line = "---" * 15
line = "━━━" * 15
thick_line = "===" * 15
new_calculation = "y"

modes = (
    "===Modes===",
    "",
    "+  | Add 2 Numbers",
    "-  | Subtract 2 Numbers",
    "*  | Multiply 2 Numbers",
    "** | Multiply by the Power",
    "/  | Divide 2 Numbers",
    "%  | Divide 2 Numbers and shows the Rest",
)

def error(message):
    print(f"\n{thick_line}")
    print(message)
    print(f"{thick_line}\n")


while new_calculation == "y":
    for listModes in modes:
        print(listModes, flush = True)
        t.sleep(0.05)
		
    print(f"\n{thin_line}\n")

    print("===Calculator===")

    print("\nShow Rounded Result? (y/n)")
    rounded = input(" - ").strip().lower()

    while rounded not in ["y", "n"]:
        error("Answer with \"y\" for yes or \"n\" for no!")

        print("Show Rounded Result? (y/n)")
        rounded = input(" - ").strip().lower()

    print(f"\n{thin_line}\n")
    
    print("Free or 2 Number Input? (1/2)")
    type = input()
     
    while type not in ["1", "2"]:
        error("Answer with \"1\" or \"2\"!")
        
        print("Free or 2 Number Input? (1/2)")
        type = input().strip()
        
    print(f"\n{line}\n")
    
    if type == "1":
        while True:
            try:
                print("Your Formular:")
                formular = input().strip()
                result = eval(formular)
                
                break
            except:
                error("Syntax Error!")
        
        print(f"\n{line}\n")
        
        if result % 1 != 0:
            print(f"{formular} = {result}")
            
        else:
            print(f"{formular} = {int(result)}")    
            
        if rounded == "y" and result % 1 != 0:
                print(f"\n{thin_line}\n")
                print(f"{formular} = {int(result)}")    
        
    else:    
        while True:
            try:
                print("First Number:")
                first_number = float(input())

                if first_number == 0:
                    break

                if not first_number:
                    error("This can't be Empty!")
                    continue

                break
            except ValueError:
                error("Use Numbers only!")

        print()

        while True:
            try:
                print("Second Number:")
                second_number = float(input())

                if second_number == 0:
                    break

                if not second_number:
                    error("This can't be Empty!")
                    continue

                break
            except ValueError:
                error("Use Numbers only!")

        print(f"\n{line}\n")

        print("Choose Calculator mode (+, -, *, **, /, %):")
        mode = input().strip()

        while mode not in ["+", "-", "*", "**", "/", "%"]:
            error("Use \"+\", \"-\", \"*\", \"**\", \"/\", \"%\"!")

            print("Choose calculator mode (+, -, *, **, /, %):")
            mode = input().strip()

        print(f"\n{line}\n")

        if mode == "+":
            result = first_number + second_number

        elif mode == "-":
            result = first_number - second_number

        elif mode == "*":
            result = first_number * second_number

        elif mode == "**":
            result = first_number ** second_number

        elif mode == "/":
            if second_number == 0:
                error("You can't divide with \"0\"!")
                result = None

            else:
                result = first_number / second_number

        elif mode == "%":
            if second_number == 0:
                error("You can't divide with \"0\"!")
                result = None

            else:
                result = first_number % second_number

        if result is not None:
            if first_number % 1 == 0:
                first_number = int(first_number)

            if second_number % 1 == 0:
                second_number = int(second_number)
    
            if result % 1 == 0:
                result = int(result)

            print(f"{first_number} {mode} {second_number} = {result}")
        
            if rounded == "y" and result % 1 != 0:
                print(f"\n{thin_line}\n")
                print(f"{first_number} {mode} {second_number} = {int(result)}")

    print(f"\n{line}\n")

    print("New Calculation? (y/n)")
    new_calculation = input(" - ").strip().lower()

    while new_calculation not in ["y", "n"]:
        error("Answer with \"y\" for yes or \"n\" for no!")

        print("New Calculation? (y/n)")
        new_calculation = input(" - ").strip().lower()

    print(f"\n{line}\n")
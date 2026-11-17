import time as t
import calculator
import timer
import password_gen
import qrcode_gen

thin_line = "---" * 15
line = "━━━" * 15
thick_line = "===" * 15

actions = (
    "===Actions===",
    "",
    "1 | calculator",
    "2 | timer",
    "3 | password_gen",
    "4 | qrcode_gen",
    "5 | exit",
)

def error(msg):
    print(f"\n{thick_line}")
    print(msg)
    print(f"{thick_line}\n")


while True:
    for list_actions in actions:
        print(list_actions, flush = True)
        t.sleep(0.05)

    print(f"\n{thin_line}\n")

    print("===Tools===\n")
    action = input("Action: ").strip().lower()

    while action not in ["1", "2", "3", "4", "5","calculator", "timer", "password_gen", "qrcode_gen", "exit"]:
        error("Use the Numbers \"1-5\" or \"calculator\", \"timer\", \"password_gen\", \"qrcode_gen\", \"exit\"!")

        action = input("Action: ").strip().lower()

    print(f"\n{line}\n")

    if action == "calculator" or action == "1":
        calculator.start()

    elif action == "timer" or action == "2":
        timer.start()

    elif action == "password_gen" or action == "3":
        password_gen.start()    
        
    elif action == "qrcode_gen" or action == "4":
        qrcode_gen.start()

    elif action == "exit" or action == "5":
        print("Exiting...")

        print(f"\n{line}\n")
        break    
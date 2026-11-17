def start():
    import time as t

    thin_line = "---" * 15
    line = "━━━" * 15
    thick_line = "===" * 15
    new_timer = "y"

    def error(msg):
        print(f"\n{thick_line}")
        print(msg)
        print(f"{thick_line}\n")


    while new_timer == "y":
        print("===Timer===\n")

        while True:
            try:
                print("Enter Timer Length:")
                length = float(input())

                if length <= 0:
                    error("Number can't be 0 or Negative!")
                    continue

                break
            except ValueError:
                error("Use Positive Numbers only!")

        print(f"\n{thin_line}\n")

        print("What Mode? (sec, min, h)")
        mode = input("Mode: ").strip().lower()

        while mode not in ["sec", "min", "h"]:
            error("Answer with \"sec\", \"min\", \"h\"!")

            mode = input("Mode: ").strip().lower()

        print(f"\n{line}\n")

        while length >= 0:
            if mode == "sec":
                print(f"\r\033[K{length:02.2f}", end = "")
                t.sleep(0.01)
                length -= 0.01

            elif mode == "min":
                print(f"\r\033[K{length:03.2f}", end = "")
                t.sleep(1)
                
                if length % 1 == 0:
                    length -= 0.41

                else:
                    length -= 0.01

            elif mode == "h":
                print(f"\r\033[K{length:03.2f}", end = "")
                t.sleep(60)
                
                if length % 1 == 0 :
                    length -= 41

                else:
                    length -= 0.01    

        print(f"\n\n{line}\n")
        print("Timer Finished!")
        print(f"\n{thin_line}\n")

        print("New Timer? (y/n)")
        new_timer = input(" - ").strip().lower()

        while new_timer not in ["y", "n"]:
            error('Answer with \"y\" for yes or \"n\" for no!')

            print("New Timer? (y/n)")
            new_timer = input(" - ").strip().lower()

        print(f"\n{line}\n")    
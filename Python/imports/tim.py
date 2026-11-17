import time as t

def timer(mode = "s", length = 0):
    while length >= 0:
        if mode == "s":
            print(f"\r\033[K{length:02.2f}", end = "")
            t.sleep(0.01)
            length -= 0.01

        elif mode == "m":
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
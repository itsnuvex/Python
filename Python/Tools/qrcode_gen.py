def start():
    import qrcode as qc

    line = "━━━" * 15
    thick_line = "===" * 15
    new_qrcode = "y"
    
    def error(msg):
        print(f"\n{thick_line}")
        print(msg)
        print(f"{thick_line}\n")

    while new_qrcode == "y":
        url = input("Your URL: ")

        while not url:
            error("Enter a URL!").strip()
    
            url = input("Your URL: ")
   
        print(f"\n{line}\n") 
    
        qr = qc.QRCode(border = 1)
        qr.add_data(url)
        qr.make()

        qr.print_ascii()

        img = qc.make(url)
        img.save("QrCode.png")
        
        print(f"\n{line}\n")
        
        print("Generate New QrCode? (y/n)")
        new_qrcode = input(" - ").strip().lower()
        while new_qrcode not in ["y", "n"]:
            error("Answer with \"y\" for yes or \"n\" for no!")
            
            print("Generate New QrCode? (y/n)")
            new_qrcode = input(" - ").strip().lower()
        
        print(f"\n{line}\n")
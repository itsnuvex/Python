import random as r
import string as s

def pas(symbol = "a", length = 0):
    password = ""
    
    if symbol == "a":
        symbol = s.ascii_letters + s.digits + s.punctuation
        
    elif symbol == "s":
        symbol = s.ascii_letters
    
    elif symbol == "sd":
        symbol = s.ascii_letters + s.digits
    
    elif symbol == "sp":
        symbol = s.ascii_letters + s.punctuation
        
    elif symbol == "d":
        symbol = s.digits 
    
    elif symbol == "p":
        symbol = s.punctuation    
        
    for _ in range(length):
        password += r.choice(symbol) 
    
    return password    
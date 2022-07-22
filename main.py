from ast import main
from curses import nl
import random
import string
if __name__=="__main__":
    p1=string.ascii_lowercase
    #print(p1)
    p2=string.ascii_uppercase
    #print(p2)
    p3=string.digits
    #print(p3)
    p4=string.punctuation
    #print(p4)
    #passlen=int(input("Enter password length: "))
    passlen=128
    p=[]
    p.extend(list(p1))
    p.extend(list(p2))
    p.extend(list(p3))
    p.extend(list(p4))
    #print(p)
    random.shuffle(p)
    #print(p)
    print("".join(p[0:passlen]))
    
    #other method 
    print("".join(random.sample(p,5)))

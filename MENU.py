print()
print()
print("\033[93mWELCOME TO Big Bang Burgers💥\033[0m")
print()

final = 0

while (True):
    print("SELECT YOUR ORDER!")
    print()
    print("1.🍔 BURGER  - $7")
    print("2.🍟 FRIES   - $3")
    print("3.🥤 COKE    - $1")
    print()
    print("\033[95mPRESS 4 for CHECKOUT\033[0m")
    print()

    n = int(input("Enter your choice: "))
    
    if(n>0 and n<=3):
        q=int(input("Enter quantity: "))
        print()
        
    if (n == 1):
        final = q * 7 + final
        
        print("\033[92mYour current bill is: $\033[0m", final)
        print()
        print("\033[96mWould you like to add anything?\033[0m")
        print()

    elif (n == 2):
        final = q * 3 + final
        
        print("\033[92mYour current bill is: $\033[0m", final)
        print()
        print("\033[96mWould you like to add anything?\033[0m")
        print()

    elif (n == 3):
        final = q * 1 + final
    
        print("\033[92mYour current bill is: $\033[0m", final)
        print()
        print("\033[96mWould you like to add anything?\033[0m")
        print()

    elif (n == 4):
        
        print()
        break
       

    else:
        print("Invalid input")

print("\033[94mTHANK YOU for choosing Big Bang Burgers 💗\033[0m")
print("\033[94m    VISIT AGAIN 🤍    \033[0m")
print()
print("\033[92mYour final bill is: $\033[0m", final)
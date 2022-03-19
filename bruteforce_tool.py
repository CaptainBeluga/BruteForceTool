import time

thread = 0
found = False

try:
    password_list = "password.txt"

    password_to_hack = "baseball" #insert your password
    
    with open(password_list,'r') as file:	
        for line in file:
            for word in line.split():
                if found == False:
                    thread = thread + 1
                    print(f"[+] {thread} Attempt = TRY: {word}\n\n")
                    time.sleep(0.1)
                    
                    if(password_to_hack == word):
                        print()
                        print("Password Found = {}\n\n".format(word))
                        found = True

    input("\n\n\n<<<Program Finished>>>\n\n\n")


except FileNotFoundError:
    print()
    print("Password List NOT Found. Try Again!")
except AttributeError:
    print()
    print("")

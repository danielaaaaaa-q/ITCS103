import sys

def opt():
    print("\n")
    print("""=== DREAMS FILE MANAGER ===
        
1. Read inspiring messages
2. Add a new inspiring message
3. Rewrite the entire file
4. Exit

    """)


while True:
    opt()
    option = int(input("Enter your choice: "))
    if option == 1:
        file = open("dreams.txt", "r")
        content = file.read()
        print("\n")
        print("--- Inspiring messages ---\n\n", content)
        file.close()
        continue
    elif option == 2:
        new_message = input("Enter your new inspiring line: ")
        file = open("dreams.txt", "a")
        file.write("\n" + new_message)
        file.close()
        print("\nNew inspiring message added successfully!")
        continue
    elif option == 3:
        print("Warning!!! This will overwrite the entire file.")
        confirm = input("Type YES to confirm: ")
        if confirm == "YES":
            new_set = input("Write your new set of inspiring messages: ")
            file = open("dreams.txt", "w")
            file.write(new_set)
            file.close()
            print("\nFile has been overwritten.")
        else:
            print("\nOperation cancelled.")
            continue
        continue
    elif option == 4:
        sys.exit()
        break
    else:
        print("\nInvalid option. Please try again.")
        continue

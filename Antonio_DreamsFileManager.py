import openpyxl as op

print("""=== DREAMS FILE MANAGER ===
      
      1. Read inspiring messages
      2. Add a new inspiring message
      3. Rewrite the entire file
      4. Exit

      """)

read = int(input("Enter your choice: "))

if read == 1:
    
#write menu driven program using files for the following operations:
#1. Write a file
#2. Read a file
#3. Append a file
#4. Exit

from file_operations import operation1,operation2,operation3

while True:
    print("1. Write a file\n2. Read a file\n3. Append a file\n4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        file_name = input("Enter the file name: ")
        lines = int(input("Enter the number of lines:"))
        content = input("Enter the content: ")
        operation1.write_into_file(file_name, content)
        print("Line 1 written successfully")
        for _ in range(lines-1):
            content = input("Enter the content: ")
            operation3.append_into_file(file_name, content)  
            print(f"Line {_+2} written successfully")
    elif choice == 2:        
        file_name = input("Enter the file name: ")
        operation2.read_the_file(file_name)
    elif choice == 3:
        file_name = input("Enter the file name: ")
        lines = int(input("Enter the number of lines:"))
        for _ in range(lines):
            content = input("Enter the content: ")
            operation3.append_into_file(file_name, content)
            print(f"Line {_+1} appended successfully")
    elif choice == 4:
        break
    else:
        print("Invalid choice")

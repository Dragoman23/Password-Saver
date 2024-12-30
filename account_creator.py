# Get user input
username = input("username: ")
password = input("password: ")

# Create and write to the file
file_name = username + 'file2.txt'
with open(file_name, 'w') as file:
    file.write(password)
    

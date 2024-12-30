import os

# Get user input for username and password
user = input("Username: ")
entered_pass = input("Password: ")
file_name = user + 'file2.txt'

try:
    # Try to read the file to validate the entered password
    with open(file_name, 'r') as file:
        password = file.read().strip()  # Strip any extra whitespace

    if entered_pass == password:
        # Prepare the file name where user-password pairs will be saved
        save_file_name = user + "savedpassword.txt"

        # Check if the file already exists
        file_exists = os.path.isfile(save_file_name)

        if not file_exists:
            # If the file does not exist, create it
            try:
                with open(save_file_name, 'x') as file:
                    pass  # No content is written to the file
                print(f"File '{save_file_name}' created successfully.")
            except FileExistsError:
                # File already exists; no need to create a new file
                pass
            except PermissionError:
                # Handle permission errors
                print(f"Error: Permission denied to create the file '{save_file_name}'.")
                exit()  # Exit if there are permission issues
            except IOError as e:
                # Handle other I/O errors
                print(f"Error: An I/O error occurred. {e}")
                exit()  # Exit if there is an I/O error

        # Handle user options after file creation or verification
        while True:
            options = input("Input 'add' if you want to add a user-password pair and 'open' if you want to read your saved password file: ").strip()
            if options == 'add':
                user2 = input("Please input your username for a website (e.g., google_(username)): ")
                password2 = input("Please input your password for a website (e.g., google_(password)): ")
                
                # Open the file in append mode to add new entries
                with open(save_file_name, 'a') as file:
                    file.write("username: " + str(user2) + '\n')
                    file.write("password: " + str(password2) + '\n')
                print("User-password pair added successfully.")

            elif options == 'open':
                # Open and read the saved passwords from the file
                with open(save_file_name, 'r') as file:
                    saved_passwords = file.read()
                    print("Saved passwords:\n" + saved_passwords)

            elif options == 'end':
                break
                    
            else:
                print("Invalid option. Please input 'add' or 'open'.")

except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
except IOError as e:
    print(f"Error: Unable to read or write to file '{file_name}'. {e}")

# The correct way to open a file and read its contents.
# This creates the file object and assigns it to the variable 'file'.
try:
    with open('animaux.txt', 'r', encoding='UTF-8') as file:
        # Now you can use the 'file' variable to work with the file
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: The file 'animaux.txt' was not found.")

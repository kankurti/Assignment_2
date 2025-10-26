# The 'with' statement automatically closes the file after the block is finished.
# 'r' mode opens the file for reading.
try:
    with open('my_file.txt', 'r') as file:
        # The file.read() method reads the entire content of the file
        # and returns it as a single string.
        file_content = file.read()
        
        # Print the content to the console
        print("--- File Content ---")
        print(file_content)

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

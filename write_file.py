# The 'with' statement handles file closing automatically.
# 'w' mode opens the file for writing (creates or overwrites it).
with open('my_file.txt', 'w') as file:
    file.write("Hello, this is my first line written to a file.\n")
    
print("Content has been written to my_file.txt")

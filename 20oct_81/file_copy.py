with open("C:/Users/Shivani/Pycharm/start/20oct_81/concatenate_n_str.py", 'r') as source_file:
    source_code = source_file.read()

# Define the name of the copy file
copy_file_name = "C:/Users/Shivani/Pycharm/start/20oct_81/copy_of_self.py"

# Write the source code to the copy file
with open(copy_file_name, 'w') as copy_file:
    copy_file.write(source_code)

print(f"Copy of the source code saved as '{copy_file_name}'")
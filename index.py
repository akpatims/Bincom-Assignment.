import os
import re

# Create a text file with your full name
with open("my_name.txt", "w") as file:
    file.write("John Doe Smith")

# Function to read and extract names
def extract_names(file_path):
    with open(file_path, "r") as file:
        full_name = file.read().strip()
    
    # Split the full name into parts
    names = full_name.split()
    
    # Extract first, middle (if any), and last names
    first_name = names[0]
    middle_name = names[1] if len(names) > 2 else None
    last_name = names[-1]
    
    return first_name, middle_name, last_name

# Print local file path
file_path = os.path.abspath("my_name.txt")
print("Local file path:", file_path)

# Extract names
first_name, middle_name, last_name = extract_names(file_path)
print("First Name:", first_name)
print("Middle Name:", middle_name)
print("Last Name:", last_name)

# Extract baby name using regex
baby_name_pattern = r"\b[a-zA-Z]+\b"  # Matches words containing only letters
with open(file_path, "r") as file:
    text = file.read()
    baby_name = re.findall(baby_name_pattern, text)[0]

print("Baby Name:", baby_name)

# Sort algorithm and binary search
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

names_list = [first_name, middle_name, last_name]
names_list.sort()

# Search for a name using binary search
search_name = "John"  # Example search name
result = binary_search(names_list, search_name)
if result != -1:
    print(f"{search_name} found at index {result} in the sorted list.")
else:
    print(f"{search_name} not found in the sorted list.")

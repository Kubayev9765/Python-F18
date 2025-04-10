1.
def Sum_Zero (a, b):
 
    try:
        sum=a/b
        print(f"Natija: {sum}")
    except ZeroDivisionError:
        print("0 soniga bo'lish mumkin emas")
  
a = float(input("1- sonni kiriting: "))
b = float(input("2- sonni kiriting: "))
Sum_Zero(a, b)

2.
def Butun_son():
    Son = input("Son kiriting: ")
    if not Son.strip().lstrip('-').isdigit():
        raise ValueError("Kiritilgan son butun son emas.")
    return int(Son)

try:
    number = Butun_son()
    print(f"Butun son kiriting!: {number}")
except ValueError as e:
    print(f"Xatolik: {e}")

3.
def open_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:\n", contents)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

# Example usage
filename = input("Enter the name of the file to open: ")
open_file(filename)

4.
def get_number(prompt):
    value = input(prompt)
    try:
        # Attempt to convert to float (to allow decimal inputs)
        return float(value)
    except ValueError:
        raise TypeError(f"Invalid input '{value}'. Expected a numerical value.")

def main():
    try:
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        print(f"You entered: {num1} and {num2}")
    except TypeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()


5.
def open_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File contents:")
            print(contents)
    except PermissionError:
        print(f"Permission denied: You do not have the rights to access '{filename}'.")
    except FileNotFoundError:
        print(f"File not found: '{filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
file_path = input("Enter the path to the file you want to open: ")
open_file(file_path)

6.
def access_list_element(my_list, index):
    try:
        # Try to access the element at the given index
        element = my_list[index]
        print(f"Element at index {index}: {element}")
    except IndexError:
        
        print(f"Error: Index {index} is out of range for the list.")

sample_list = [10, 20, 30, 40, 50]
access_list_element(sample_list, 2)
access_list_element(sample_list, 10)


7.
def main():
    try:
        number = input("Please enter a number: ")
        print(f"You entered: {number}")
    except KeyboardInterrupt:
        print("\nInput cancelled by user.")

if __name__ == "__main__":
    main()

8.
def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result of {a} divided by {b} is: {result}")
    except ArithmeticError as e:
        print(f"An arithmetic error occurred: {e}")

num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))

divide_numbers(num1, num2)

9.
def read_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            print("File content:\n", content)
    except UnicodeDecodeError:
        print("Error: Could not decode the file due to an encoding issue.")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
read_file('example.txt')

10.
def perform_list_operation():
    my_list = [1, 2, 3, 4, 5]

    try:
        # Attempting to use a non-existent method 'append_all'
        my_list.append_all([6, 7, 8])
    except AttributeError as e:
        print(f"AttributeError caught: {e}")
        print("Attempting valid operation instead...")

        # Correct method to append multiple elements
        my_list.extend([6, 7, 8])

    print("Updated list:", my_list)

if __name__ == "__main__":
    perform_list_operation()

11.
def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print("File Content:\n")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = 'example.txt'  # Replace this with your file path
read_file(file_path)

12.
def read_first_n_lines(filename, n):
    try:
        with open(filename, 'r') as file:
            for i in range(n):
                line = file.readline()
                if not line:
                    break  # Stop if end of file is reached
                print(line.strip())
    except FileNotFoundError:
        print(f"The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    filename = input("Enter the filename: ")
    n = int(input("Enter the number of lines to read: "))
    read_first_n_lines(filename, n)

13.
def append_text_to_file(filename, text_to_append):
    with open(filename, 'a') as file:
        # Append the text to the file
        file.write(text_to_append + '\n')
    
    with open(filename, 'r') as file:
        content = file.read()
        print("Current content of the file:")
        print(content)

filename = "example.txt"
text_to_append = "This is the new text that will be appended."

append_text_to_file(filename, text_to_append)

14.
def read_last_n_lines(file_name, n):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        
        if len(lines) < n:
            return lines
        else:
            return lines[-n:]

# Example usage:
file_name = 'your_file.txt'
n = 5  
last_n_lines = read_last_n_lines(file_name, n)


for line in last_n_lines:
    print(line, end="")


15.
def read_file_into_list(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()  # Read all lines into a list
    return lines


file_path = 'your_file.txt'  # Replace with your file path
lines = read_file_into_list(file_path)


for line in lines:
    print(line.strip())

16.
def read_file_to_variable(file_path):
    # Initialize an empty list to store lines
    lines = []
    
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read each line and store it in the list
        for line in file:
            lines.append(line.strip())  # .strip() removes leading/trailing whitespace
    
    return lines

file_path = 'your_file.txt'  # Replace with the path to your file
lines = read_file_to_variable(file_path)

for line in lines:
    print(line)

17.
def read_file_to_array(file_name):
    # Initialize an empty list to store the lines
    lines_array = []
    
    try:
        # Open the file in read mode
        with open(file_name, 'r') as file:
            # Iterate over each line in the file
            for line in file:
                # Strip the newline characters and append to the list
                lines_array.append(line.strip())
    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return lines_array

file_name = "example.txt"  # Replace with your file name
lines = read_file_to_array(file_name)

print(lines)

18.
def find_longest_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Find the length of the longest word(s)
    max_length = max(len(word) for word in words)
    
    # Collect all words that have the maximum length
    longest_words = [word for word in words if len(word) == max_length]
    
    return longest_words


sentence = "The quick brown fox jumped over the lazy dog"
longest_words = find_longest_words(sentence)

print("Longest word(s):", longest_words)

19.
def count_lines_in_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
        return 0

filename = 'example.txt'  # Replace with the path to your text file
line_count = count_lines_in_file(filename)
print(f"The number of lines in the file is: {line_count}")

20.
def count_word_frequency(file_path):
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read the content of the file
        text = file.read()
    
    text = ''.join(e if e.isalnum() else ' ' for e in text).lower()
    
    words = text.split()
    
    word_freq = {}
    
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    return word_freq

file_path = 'example.txt'  # Replace with your file path

word_frequencies = count_word_frequency(file_path)

for word, freq in word_frequencies.items():
    print(f'{word}: {freq}')

21.
import os

def get_file_size(file_path):
    try:
        # Get the file size
        file_size = os.path.getsize(file_path)
        print(f"The size of the file '{file_path}' is {file_size} bytes.")
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
        
file_path = 'example.txt'  # Replace with the path to your file
get_file_size(file_path)

22.
my_list = ["apple", "banana", "cherry", "date"]

with open("output.txt", "w") as file:
    # Iterate through the list and write each item to the file
    for item in my_list:
        file.write(item + "\n")

print("List has been written to 'output.txt'")

23.
def copy_file(source, destination):
    try:
        with open(source, 'r') as src_file:
            with open(destination, 'w') as dest_file:
                content = src_file.read()
                dest_file.write(content)
        print(f"Content copied successfully from {source} to {destination}.")
    except FileNotFoundError:
        print(f"Error: The file {source} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

source_file = 'source.txt'
destination_file = 'destination.txt'
copy_file(source_file, destination_file)

24.
def combine_lines(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

        for line1, line2 in zip(lines1, lines2):
            out.write(line1.strip() + " " + line2)

combine_lines('file1.txt', 'file2.txt', 'combined_output.txt')

25.
import random

def read_random_line(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()  # Read all lines from the file
            if lines:  # Ensure the file isn't empty
                return random.choice(lines).strip()  # Choose a random line
            else:
                return "The file is empty."
    except FileNotFoundError:
        return "File not found."

filename = 'your_file.txt'  # Replace with your file's path
print(read_random_line(filename))

26.
def check_if_file_closed(file_path):
    try:
        file = open(file_path, 'r')
        
        print(f"Is the file closed before closing? {file.closed}")
        
        file.close()
        
        print(f"Is the file closed after closing? {file.closed}")
        
    except FileNotFoundError:
        print(f"The file at {file_path} does not exist.")

file_path = 'example.txt'
check_if_file_closed(file_path)

27.
def remove_newlines(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            content = infile.read().replace('\n', '')  # Remove all newline characters

        with open(output_file, 'w') as outfile:
            outfile.write(content)

        print(f"Newlines removed. Clean content saved to '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_filename = 'input.txt'     # Replace with your input file path
output_filename = 'output.txt'   # Replace with your desired output file path

remove_newlines(input_filename, output_filename)

28.
def count_words_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            contents = file.read()
            words = contents.split()
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        return "The file was not found."
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    result = count_words_in_file(file_path)
    print(f"Word Count: {result}")

29.
import os

def extract_characters_from_files(file_paths):
    all_characters = []
    
    for path in file_paths:
        try:
            with open(path, 'r', encoding='utf-8') as file:
                contents = file.read()
                characters = list(contents)
                all_characters.extend(characters)
        except FileNotFoundError:
            print(f"File not found: {path}")
        except Exception as e:
            print(f"Error reading {path}: {e}")
    
    return all_characters

# Example usage
if __name__ == "__main__":
    # Example: Enter file paths separated by commas
    file_input = input("Enter paths to text files (comma-separated): ")
    file_list = [f.strip() for f in file_input.split(",")]
    
    character_list = extract_characters_from_files(file_list)
    print(f"Total characters extracted: {len(character_list)}")
    print("First 100 characters (for preview):")
    print(character_list[:100])  # show first 100 for preview

30.
import string
import os

def generate_alphabet_files(directory="."):
    # Get all uppercase letters A to Z
    letters = string.ascii_uppercase
    
    for letter in letters:
        file_name = f"{letter}.txt"
        file_path = os.path.join(directory, file_name)
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(f"This is file {file_name}\n")
            print(f"Created: {file_path}")
        except Exception as e:
            print(f"Error creating {file_path}: {e}")

if __name__ == "__main__":
    generate_alphabet_files()

31.
import string

def write_alphabet_to_file(filename, letters_per_line):
    alphabet = string.ascii_uppercase  # Use .ascii_lowercase if you want lowercase
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for i in range(0, len(alphabet), letters_per_line):
                line = alphabet[i:i + letters_per_line]
                file.write(line + '\n')
        print(f"File '{filename}' created with {letters_per_line} letters per line.")
    except Exception as e:
        print(f"Error creating file: {e}")

# Example usage
if __name__ == "__main__":
    filename = input("Enter the filename to create: ")
    try:
        letters_per_line = int(input("Enter the number of letters per line: "))
        write_alphabet_to_file(filename, letters_per_line)
    except ValueError:
        print("Please enter a valid number.")










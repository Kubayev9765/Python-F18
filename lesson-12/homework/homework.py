1
import threading
import math

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Worker function for each thread
def check_primes(start, end, result):
    primes_in_range = []
    for num in range(start, end):
        if is_prime(num):
            primes_in_range.append(num)
    result.extend(primes_in_range)

# Main program
def find_primes_in_range(start, end, num_threads):
    # Split the range into chunks for each thread
    step = (end - start) // num_threads
    threads = []
    results = []

    # Start threads
    for i in range(num_threads):
        chunk_start = start + i * step
        chunk_end = start + (i + 1) * step if i != num_threads - 1 else end
        thread_result = []
        results.append(thread_result)
        thread = threading.Thread(target=check_primes, args=(chunk_start, chunk_end, thread_result))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    # Combine results from all threads
    all_primes = []
    for result in results:
        all_primes.extend(result)

    return all_primes

# Input from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
num_threads = int(input("Enter the number of threads to use: "))

# Find and print prime numbers in the range
primes = find_primes_in_range(start, end, num_threads)
print(f"Prime numbers in the range [{start}, {end}]: {primes}")

2.
import threading
from collections import defaultdict
import os

# Worker function to process a portion of the file
def process_chunk(file_chunk, result_dict):
    word_count = defaultdict(int)
    for line in file_chunk:
        words = line.strip().split()
        for word in words:
            word_count[word.lower()] += 1
    
    # Update the global word count dictionary
    with threading.Lock():
        for word, count in word_count.items():
            result_dict[word] += count

# Function to split file into chunks for threading
def process_file_in_threads(file_path, num_threads):
    # Read the file and divide into chunks
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Divide the lines into chunks
    chunk_size = len(lines) // num_threads
    threads = []
    results = defaultdict(int)
    
    # Create threads to process each chunk
    for i in range(num_threads):
        start = i * chunk_size
        # If it's the last chunk, it takes the rest of the lines
        end = (i + 1) * chunk_size if i != num_threads - 1 else len(lines)
        file_chunk = lines[start:end]
        
        thread = threading.Thread(target=process_chunk, args=(file_chunk, results))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    return results

# Main program
def main():
    file_path = input("Enter the path to the text file: ")
    num_threads = int(input("Enter the number of threads to use: "))
    
    if not os.path.exists(file_path):
        print("❌ File not found. Please check the path and try again.")
        return
    
    # Process the file using threads
    word_counts = process_file_in_threads(file_path, num_threads)
    
    # Display the word counts
    print("\nWord occurrences in the file:")
    for word, count in sorted(word_counts.items()):
        print(f"{word}: {count}")

# Run the program
if __name__ == "__main__":
    main()

import threading
from collections import defaultdict
import os

# Function to process a portion of the file and count word occurrences
def count_words_in_chunk(file_path, start, end, word_counts):
    with open(file_path, 'r') as f:
        # Move the file pointer to the start position
        f.seek(start)
        chunk = f.read(end - start)  # Read the chunk of text

        # Process the chunk and update word counts
        words = chunk.split()
        local_counts = defaultdict(int)

        for word in words:
            local_counts[word.lower()] += 1

        # Lock and update the shared word count dictionary
        with word_counts_lock:
            for word, count in local_counts.items():
                word_counts[word] += count

# Main program to divide the file processing among multiple threads
def count_words_in_file(file_path, num_threads):
    # Get the file size
    file_size = os.path.getsize(file_path)
    
    # Calculate the size of each chunk for each thread
    chunk_size = file_size // num_threads
    
    # Initialize the dictionary to store word counts
    word_counts = defaultdict(int)
    
    # Lock to prevent race conditions when updating word counts
    global word_counts_lock
    word_counts_lock = threading.Lock()
    
    # Create and start threads
    threads = []
    for i in range(num_threads):
        # Determine the start and end positions for each thread
        start = i * chunk_size
        end = (i + 1) * chunk_size if i != num_threads - 1 else file_size
        thread = threading.Thread(target=count_words_in_chunk, args=(file_path, start, end, word_counts))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    
    return word_counts

# Input from the user
file_path = input("Enter the path of the text file: ")
num_threads = int(input("Enter the number of threads to use: "))

# Count words in the file using threading
word_counts = count_words_in_file(file_path, num_threads)

# Display the word counts
print("\nWord occurrences in the file:")
for word, count in sorted(word_counts.items(), key=lambda item: item[1], reverse=True):
    print(f"{word}: {count}")

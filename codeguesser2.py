import time
import random
import concurrent.futures

# Configurable Variables
MAX_NUMBER = 999999999999999999999999999999999999999  # The maximum number to be guessed (e.g., 10^10)
MAX_CORES = 15  # Maximum number of cores
WAIT_SECONDS_BEFORE_NEXT = 5  # Number of seconds to wait before starting the next process after a correct result

# Function for binary search, used by each thread
def binary_search(start, end, target):
    attempts = 0
    while start <= end:
        mid = (start + end) // 2
        attempts += 1
        if mid == target:
            return attempts
        elif mid < target:
            start = mid + 1
        else:
            end = mid - 1
    return attempts

# Function that starts the entire process
def start_game(target):
    print(f"Number to guess has been generated: {target}")
    
    # Start time with higher precision
    start_time = time.perf_counter()

    # Optimized approach with threads instead of processes
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_CORES) as executor:
        # Feeding the pool with tasks (start and end range for all threads)
        step = MAX_NUMBER // MAX_CORES  # Determine the range for each thread
        futures = [executor.submit(binary_search, i * step + 1, (i + 1) * step, target) for i in range(MAX_CORES)]
        
        attempts = [future.result() for future in concurrent.futures.as_completed(futures)]

    # Only print the number of attempts and the total time
    min_attempts = min(attempts)  # Use min() on the list of attempts
    
    # Calculate total time
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    
    print(f"The number was guessed in {min_attempts} attempts.")
    print(f"The number was guessed in a total of {elapsed_time:.10f} seconds.\n")
    
    # Wait before the next game starts (waiting time after the result)
    print(f"Waiting {WAIT_SECONDS_BEFORE_NEXT} seconds before starting the next attempt.")
    time.sleep(WAIT_SECONDS_BEFORE_NEXT)

# Main function to start the game with a changeable number
def main():
    print(f"Maximum Number: {MAX_NUMBER}")
    print(f"Maximum Cores: {MAX_CORES}")
    print(f"After the result, the program will wait {WAIT_SECONDS_BEFORE_NEXT} seconds before starting the next attempt.")
    
    while True:
        # Here you can change the number to be guessed
        target_number = random.randint(1, MAX_NUMBER)  # A number between 1 and MAX_NUMBER
        start_game(target_number)

if __name__ == "__main__":
    main()

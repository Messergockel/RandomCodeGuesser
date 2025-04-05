# RandomCodeGuesser
This Python script is a performance-optimized number guessing game that utilizes multi-threading for fast execution. The goal of the game is to guess a randomly generated number using binary search. It splits the search range across multiple threads to speed up the process.

#Features
Multi-threading support: Utilizes Python's concurrent.futures.ThreadPoolExecutor to run the binary search in parallel across multiple threads.

Configurable settings: Easily adjust the maximum number to guess, number of cores, and the waiting time between attempts.

The game measures and displays the number of attempts and total time it takes to guess the number.


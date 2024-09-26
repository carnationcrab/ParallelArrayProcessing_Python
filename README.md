# Parallel Array Processing in Python

This program is designed to model simple implicit parallelism using Python's `concurrent.futures.ThreadPoolExecutor`. The program demonstrates how multi-threading can be used to speed up the process of summing a large array. It achieves this by dividing the work into chunks and processing them concurrently.

## What it does:
- Utilizes multi-threading to achieve parallelism.
- Divides a large array into chunks and processes them in parallel.

## How it works:
- The program generates an array of integers from 1 to 1,000,000.
- This array is divided into a thread count quantity of equal-sized chunks.
- Using `ThreadPoolExecutor`, each chunk is processed concurrently by a separate thread to calculate its sum.
- The chunk sums are then combined to form the total sum.

## Running the program:
Run the script in `testingParallelism.py` using Python:
`python thread_test.py`

The program will start, and you’ll see detailed logs of the execution steps.

To run without logs, change log level from INFO to WARN.

![image](https://github.com/user-attachments/assets/a63364bd-51f1-410c-94be-438769a8f379)

import logging
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.INFO, format='%(threadName)s: %(message)s')
programName = "Thread Test in Python"


def startupLog():
    logging.info('_ START. ______________________________________________________________')
    logging.info(f'Starting {programName}...')
    logging.info('The purpose of this program is to showcase simple IMPLICIT PARALLELISM.')
    logging.info('                                                                       ')
    logging.info('_ INFO: _______________________________________________________________')
    logging.info('The program takes a large array and breaks it into 4 chunks.'           )
    logging.info('It adds up those chunks using ThreadPoolExecutor, in tandem.'           )
    logging.info('Then it sums all the chunk sums up to form the total sum.'              )
    logging.info('_______________________________________________________________________')


def programStartLog():
    logging.info('                                                                       ')
    logging.info(f'> SUM A LARGE ARRAY CONCURRENTLY: >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    logging.info('                                                                       ')


def sumLargeArray():
    programStartLog()

    # Create a largeArray of numbers from 1 to 1,000,000.
    largeArray = [i for i in range(1, 1000001)]
    logging.info(f'Created a large array of integers (all ints from 1 to 1,000,000).')
    
    # Call the parallelSum function to calculate the total sum using implicit parallelism.
    result = parallelSum(largeArray)
    
    print(f'THE TOTAL SUM OF THE ARRAY IS: {result}')


# Takes a portion of the array and calculates the sum of its elements.
def partialSum(chunkArray):
    logging.info(f'Starting sum of chunk with {len(chunkArray)} elements...')

    chunkSum = sum(chunkArray)

    logging.info(f'Finished sum of chunk: {chunkSum}')
    return chunkSum


def parallelSum(largeArray, threadCount=4):
    
    # Calculate size of each chunk based on # of threads using floor division
    chunkSize = len(largeArray) // threadCount
    logging.info(f'Determined chunk size should be {chunkSize}.')

    
    # Divide the original array into chunks. Each chunk is a sublist of the largeArray.
    chunks = [largeArray[i * chunkSize:(i + 1) * chunkSize] for i in range(threadCount)]
    logging.info(f'Divided array into {threadCount} chunks, with approximately {chunkSize} elements each.')

    # Create a ThreadPoolExecutor with 'threadCount' # of workers (threads).
    with ThreadPoolExecutor(max_workers=threadCount) as executor:
        # Use the executor to apply the 'partialSum' fn to each chunk in parallel.
        logging.info('Submitting summing tasks to thread pool executor')
        results = executor.map(partialSum, chunks)

    # Sum results from each thread
    total = sum(results)
    logging.info(f'Total sum calculated: {total}')
    return total


def programCompleteLog():
    logging.info('________________________________________________________________ END. _')


def main():
    startupLog()
    sumLargeArray()
    programCompleteLog()


main()





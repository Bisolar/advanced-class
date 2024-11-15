import asyncio
import requests
import time
import threading

# urls = ["https://www.arise.tv/", "https://www.tvcnews.tv/", "https://www.channelstv.com/"]

# async def fetch_data(url):
#     response = requests.get(url)
#     await asyncio.sleep(5)
#     print(response.status_code)

# async def main():
#     urls = ["https://www.arise.tv/", "https://www.tvcnews.tv/", "https://www.channelstv.com/"]
#     tasks = [fetch_data(url) for url in urls]

#     result = await asyncio.gather(*tasks)
#     print("result:", result)

# asyncio.run(main())

# for threading
# def type_numbers():
#     for I in range(6):
#         print(I)

# def type_letter():
#     for x in ["a", "b", "c", "d", "e","f"]:
#         print(x)

# task_1 = threading.Thread(target= type_numbers)
# task_2 = threading.Thread(target= type_letter)

# event = threading.Event(target= task_1)
# event.run()
# print(event)

# multiprocessing
from multiprocessing import Pool

def calculate_square(n):
    print(f"Calculating square of {n}")
    time.sleep(2)
    return n * n

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    with Pool(processes=2) as pool:
        results = pool.map(calculate_square, numbers)

        print("Squares:", results)
    


    

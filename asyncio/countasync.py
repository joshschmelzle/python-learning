# countasync.py

# Path: asyncio\countasync.py
# This is an asynchronous program showing how to use asyncio.sleep()
#   and asyncio.gather() to run multiple coroutines concurrently.

import asyncio
import time

async def count(duration):
    print("Before await")
    await asyncio.sleep(duration)
    print("After await")

async def main():
    duration = 0.500
    await asyncio.gather(count(duration), count(duration), count(duration), count(duration), count(duration))
    print("We slept for {} seconds between each before and after".format(duration))

if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.3f} seconds.")

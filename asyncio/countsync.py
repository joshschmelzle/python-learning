# countsync.py

# Path: asyncio\countsync.py
# Compare this snippet to asyncio\countasync.py

import time

def count(duration):
    print("Before sleep")
    time.sleep(duration)
    print("After sleep")

def main():
    duration = 0.500
    for _ in range(3):
        count(duration)
    print("We slept for {} seconds between each before and after".format(duration))

if __name__ == "__main__":
    s = time.perf_counter()
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
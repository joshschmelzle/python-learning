import asyncio

# @asyncio.coroutine  # this way of defining a coroutine will be removed in py3.10
# def py34_coro_work():
#     """Generator-based coroutine, older syntax"""
#     yield "stuff"
async def py35_coro_work():
    """Native coroutine, newer and modern syntax"""
    # You should be writing native coroutines for the sake of being explicit!
    return "stuff"
async def do_something():
    """This is a coroutine"""
    # pause here and come back to do_something() when work() is ready
    w = await py35_coro_work()
    return w

if __name__ == "__main__":
    resp = asyncio.run(do_something())
    print(resp)
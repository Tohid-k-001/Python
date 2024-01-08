import time
import asyncio
import requests

async def function1():
    await asyncio.sleep(4)
    url="http://pngimg.com/uploads/anime_girl/anime_girl_PNG88.png"
    r=requests.get(url)
    open("anime1.png","wb").write(r.content)
    print("function1")

async def function2():
    url="http://pngimg.com/uploads/anime_girl/anime_girl_PNG88.png"
    r=requests.get(url)
    open("anime2.png","wb").write(r.content)
    await asyncio.sleep(2)
    print("function2")

async def function3():
    url="http://pngimg.com/uploads/anime_girl/anime_girl_PNG88.png"
    r=requests.get(url)
    open("anime3.png","wb").write(r.content)
    await asyncio.sleep(5)
    print("function3")

async def main():
    l=await asyncio.gather(
        function1(),
        function2(),
        function3()
    ) # --> run parallel
    print(l)

    #--> here when func 1 runs it took 7 sec. so it runs func2 and func3
    # task=asyncio.create_task(function1())
    # await function1()
    # await function2()
    # await function3()
    # # the above doesn't give proper management runs serially
   

asyncio.run(main())
   



